# ui/graph_widget.py
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt, QTimer
import pyqtgraph as pg
import numpy as np
from collections import deque


class GraphWidget(QWidget):
    """Виджет для отображения графиков в реальном времени"""
    
    def __init__(self, parent=None, max_points=200):
        super().__init__(parent)
        self.max_points = max_points
        self.data = deque(maxlen=max_points)
        self.timestamps = deque(maxlen=max_points)
        self.time_counter = 0
        
        self._setup_ui()
        self._setup_graph()
        
    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
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
        self.plot_fill = pg.FillBetweenItem(
            self.plot_line,
            pg.PlotDataItem([], pen=pg.mkPen(color='#00ff88', width=0)),
            brush=pg.mkBrush(color=(0, 255, 136, 50))
        )
        self.plot_widget.addItem(self.plot_fill)
        
        # Текст для отображения текущего значения
        self.value_text = pg.TextItem(
            text="0.0",
            color='w',
            anchor=(1, 0)
        )
        self.plot_widget.addItem(self.value_text)
        
    def add_data_point(self, value):
        """Добавление новой точки данных"""
        self.time_counter += 0.1  # Шаг 0.1 секунды
        self.data.append(value)
        self.timestamps.append(self.time_counter)
        
        # Обновление графика
        if len(self.data) > 1:
            x_data = list(self.timestamps)
            y_data = list(self.data)
            
            self.plot_line.setData(x_data, y_data)
            self.plot_fill.setData(
                pg.PlotDataItem(x_data, y_data),
                pg.PlotDataItem(x_data, [0] * len(y_data))
            )
            
            # Обновление текста с текущим значением
            last_x = x_data[-1] if x_data else 0
            last_y = y_data[-1] if y_data else 0
            self.value_text.setText(f"{last_y:.2f}")
            self.value_text.setPos(last_x, last_y)
            
            # Автоматическое масштабирование по Y
            if len(y_data) > 1:
                y_min = min(y_data)
                y_max = max(y_data)
                padding = (y_max - y_min) * 0.1 if y_max > y_min else 1
                self.plot_widget.setYRange(y_min - padding, y_max + padding)
    
    def clear(self):
        """Очистка графика"""
        self.data.clear()
        self.timestamps.clear()
        self.time_counter = 0
        self.plot_line.setData([], [])
        self.plot_fill.setData(
            pg.PlotDataItem([], []),
            pg.PlotDataItem([], [])
        )
        self.value_text.setText("0.0")
        self.value_text.setPos(0, 0)