# ui/multi_graph_widget.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout
from PySide6.QtCore import Qt
import pyqtgraph as pg
from collections import deque


class MultiGraphWidget(QWidget):
    """Виджет для отображения 4 графиков одновременно"""
    
    def __init__(self, parent=None, max_points=200):
        super().__init__(parent)
        self.max_points = max_points
        
        # Данные для каждого графика
        self.torque_data = deque(maxlen=max_points)
        self.force_data = deque(maxlen=max_points)
        self.current_data = deque(maxlen=max_points)
        self.temp_data = deque(maxlen=max_points)
        self.time_counter = 0
        
        self._setup_ui()
        
    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Создаем сетку 2x2 для графиков
        grid = QGridLayout()
        grid.setSpacing(2)
        
        # Настройки для каждого графика
        self.plots = []
        self.lines = []
        
        colors = ['#00ff88', '#ff8800', '#0088ff', '#ff0088']
        names = ['Момент (Н·м)', 'Усилие (Н)', 'Ток (А)', 'Температура (°C)']
        
        for i in range(4):
            plot_widget = pg.PlotWidget()
            plot_widget.setBackground('#1e1e1e')
            plot_widget.showGrid(x=True, y=True, alpha=0.3)
            plot_widget.setLabel('left', names[i], units='')
            plot_widget.setLabel('bottom', 'Время', units='с')
            plot_widget.setXRange(0, 10)
            
            # Стиль осей
            plot_widget.getAxis('left').setTextPen('w')
            plot_widget.getAxis('bottom').setTextPen('w')
            
            # Отключаем управление мышью
            plot_widget.setMouseEnabled(x=False, y=False)
            plot_widget.setMenuEnabled(False)
            
            # Линия графика
            line = plot_widget.plot(
                pen=pg.mkPen(color=colors[i], width=2)
            )
            
            # Текст с текущим значением
            from pyqtgraph import TextItem
            value_text = TextItem(
                text="0.0",
                color='w',
                anchor=(1, 0)
            )
            plot_widget.addItem(value_text)
            
            # Добавляем в сетку
            row = i // 2
            col = i % 2
            grid.addWidget(plot_widget, row, col)
            
            self.plots.append({
                'widget': plot_widget,
                'line': line,
                'text': value_text,
                'data': deque(maxlen=max_points)
            })
        
        layout.addLayout(grid)
        
    def add_data_point(self, torque, force, current, temp):
        """Добавление новых точек для всех датчиков"""
        self.time_counter += 0.1
        
        # Данные для каждого графика
        all_data = [torque, force, current, temp]
        
        for i, data in enumerate(all_data):
            self.plots[i]['data'].append(data)
            x_data = list(range(len(self.plots[i]['data'])))
            y_data = list(self.plots[i]['data'])
            
            # Обновляем линию
            self.plots[i]['line'].setData(x_data, y_data)
            
            # Обновляем текст
            if y_data:
                self.plots[i]['text'].setText(f"{y_data[-1]:.2f}")
                self.plots[i]['text'].setPos(len(y_data) - 1, y_data[-1])
            
            # Автомасштабирование
            if len(y_data) > 1:
                y_min = min(y_data)
                y_max = max(y_data)
                padding = (y_max - y_min) * 0.1 if y_max > y_min else 1
                self.plots[i]['widget'].setYRange(y_min - padding, y_max + padding)
                # Показываем последние 10 секунд (100 точек при 10 Гц)
                x_min = max(0, len(y_data) - 100)
                x_max = max(10, len(y_data))
                self.plots[i]['widget'].setXRange(x_min, x_max)
    
    def clear(self):
        """Очистка всех графиков"""
        self.time_counter = 0
        for plot in self.plots:
            plot['data'].clear()
            plot['line'].setData([], [])
            plot['text'].setText("0.0")
            plot['text'].setPos(0, 0)