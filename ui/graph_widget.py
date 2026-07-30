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
        self.x_data = []
        self.y_data = []
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
        
        layout.addWidget(self.plot_widget)
        
        # Линия графика
        self.plot_line = self.plot_widget.plot(
            pen=pg.mkPen(color='#00ff88', width=2)
        )
        
        # Заливка под графиком
        from pyqtgraph import PlotDataItem, FillBetweenItem, mkBrush
        self.plot_fill = FillBetweenItem(
            self.plot_line,
            PlotDataItem([], pen=pg.mkPen(color='#00ff88', width=0)),
            brush=mkBrush(color=(0, 255, 136, 50))
        )
        self.plot_widget.addItem(self.plot_fill)
        
        # Текст для отображения текущего значения
        from pyqtgraph import TextItem
        self.value_text = TextItem(
            text="0.0",
            color='w',
            anchor=(1, 0)
        )
        self.plot_widget.addItem(self.value_text)
        
    def add_data_point(self, value):
        """Добавление новой точки данных"""
        self.time_counter += 0.1
        self.x_data.append(self.time_counter)
        self.y_data.append(value)
        
        # Ограничиваем количество точек
        if len(self.x_data) > self.max_points:
            self.x_data.pop(0)
            self.y_data.pop(0)
        
        # Обновление графика
        if len(self.x_data) > 1:
            self.plot_line.setData(self.x_data, self.y_data)
            
            # Обновляем заливку
            from pyqtgraph import PlotDataItem
            self.plot_fill.setData(
                PlotDataItem(self.x_data, self.y_data),
                PlotDataItem(self.x_data, [0] * len(self.y_data))
            )
            
            # Обновление текста с текущим значением
            last_x = self.x_data[-1] if self.x_data else 0
            last_y = self.y_data[-1] if self.y_data else 0
            self.value_text.setText(f"{last_y:.2f}")
            self.value_text.setPos(last_x, last_y)
            
            # Автоматическое масштабирование по Y
            if len(self.y_data) > 1:
                y_min = min(self.y_data)
                y_max = max(self.y_data)
                padding = (y_max - y_min) * 0.1 if y_max > y_min else 1
                self.plot_widget.setYRange(y_min - padding, y_max + padding)
    
    def clear(self):
        """Очистка графика"""
        self.x_data.clear()
        self.y_data.clear()
        self.time_counter = 0
        self.plot_line.setData([], [])
        
        from pyqtgraph import PlotDataItem
        self.plot_fill.setData(
            PlotDataItem([], []),
            PlotDataItem([], [])
        )
        self.value_text.setText("0.0")
        self.value_text.setPos(0, 0)