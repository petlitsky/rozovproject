# ui/graph_widget.py
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt
import pyqtgraph as pg
from collections import deque


class GraphWidget(QWidget):
    """Виджет для отображения графиков в реальном времени"""
    
    def __init__(self, parent=None, max_points=200):
        super().__init__(parent)
        self.max_points = max_points
        
        # Данные для каждой линии
        self.lines_data = {}  # {name: {'x': [], 'y': [], 'line': None, 'color': None}}
        self.time_counter = 0
        
        self._setup_ui()
        
    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Создаем виджет для графика
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setBackground('#1e1e1e')
        self.plot_widget.showGrid(x=True, y=True, alpha=0.3)
        self.plot_widget.setLabel('left', 'Значение', units='')
        self.plot_widget.setLabel('bottom', 'Время', units='с')
        self.plot_widget.setXRange(0, 10)
        
        # Стиль осей
        self.plot_widget.getAxis('left').setTextPen('w')
        self.plot_widget.getAxis('bottom').setTextPen('w')
        
        # Разрешаем перемещение по X, но запрещаем по Y
        self.plot_widget.setMouseEnabled(x=True, y=False)
        self.plot_widget.setMenuEnabled(False)
        
        layout.addWidget(self.plot_widget)
        
        # Легенда
        self.plot_widget.addLegend()
        
        # Текст для отображения текущего значения (будет обновляться реже)
        from pyqtgraph import TextItem
        self.value_text = TextItem(
            text="",
            color='w',
            anchor=(1, 0)
        )
        self.plot_widget.addItem(self.value_text)
        
    def add_line(self, name, color):
        """Добавление новой линии на график"""
        if name not in self.lines_data:
            pen = pg.mkPen(color=color, width=2)
            line = self.plot_widget.plot([], [], pen=pen, name=name)
            self.lines_data[name] = {
                'x': [],
                'y': [],
                'line': line,
                'color': color
            }
    
    def add_data_point(self, name, value):
        """Добавление новой точки для конкретной линии"""
        if name not in self.lines_data:
            return
        
        self.time_counter += 0.1
        data = self.lines_data[name]
        data['x'].append(self.time_counter)
        data['y'].append(value)
        
        # Ограничиваем количество точек
        if len(data['x']) > self.max_points:
            data['x'].pop(0)
            data['y'].pop(0)
        
        # Обновляем линию
        if len(data['x']) > 1:
            data['line'].setData(data['x'], data['y'])
    
    def add_data_points(self, data_dict):
        """Добавление точек для нескольких линий одновременно"""
        self.time_counter += 0.1
        
        for name, value in data_dict.items():
            if name not in self.lines_data:
                continue
            
            data = self.lines_data[name]
            data['x'].append(self.time_counter)
            data['y'].append(value)
            
            # Ограничиваем количество точек
            if len(data['x']) > self.max_points:
                data['x'].pop(0)
                data['y'].pop(0)
            
            # Обновляем линию
            if len(data['x']) > 1:
                data['line'].setData(data['x'], data['y'])
    
    def update_text(self, text):
        """Обновление текста с текущими значениями"""
        self.value_text.setText(text)
        if self.lines_data:
            # Находим последнюю точку по времени
            max_x = 0
            max_y = 0
            for data in self.lines_data.values():
                if data['x'] and data['x'][-1] > max_x:
                    max_x = data['x'][-1]
                    max_y = data['y'][-1]
            self.value_text.setPos(max_x, max_y)
    
    def clear(self):
        """Очистка графика"""
        self.time_counter = 0
        for data in self.lines_data.values():
            data['x'].clear()
            data['y'].clear()
            data['line'].setData([], [])
        self.value_text.setText("")
        self.value_text.setPos(0, 0)
    
    def clear_line(self, name):
        """Очистка конкретной линии"""
        if name in self.lines_data:
            data = self.lines_data[name]
            data['x'].clear()
            data['y'].clear()
            data['line'].setData([], [])