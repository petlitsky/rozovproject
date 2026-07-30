# ui/graph_widget.py
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt, QTimer
import pyqtgraph as pg
import time


class GraphWidget(QWidget):
    """Виджет для отображения графиков в реальном времени"""
    
    def __init__(self, parent=None, max_points=300):
        super().__init__(parent)
        self.max_points = max_points
        
        # Данные для каждой линии
        self.lines_data = {}  # {name: {'x': [], 'y': [], 'line': None, 'color': None}}
        self.is_auto_scroll = True  # Флаг автоматического скролла
        self.start_time = None  # Время старта в секундах с начала эпохи
        
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
        
        # Отключаем автосмещение при перемещении мышью
        self.plot_widget.sigRangeChanged.connect(self._on_range_changed)
        
        layout.addWidget(self.plot_widget)
    
    def _get_current_time(self):
        """Получение текущего времени в секундах с начала эпохи"""
        return time.time()
    
    def _on_range_changed(self, plot, ranges):
        """Обработка изменения диапазона (пользователь переместил график)"""
        if self.plot_widget.getViewBox().mouseEnabled()[0]:
            self.is_auto_scroll = False
    
    def add_line(self, name, color):
        """Добавление новой линии на график"""
        if name not in self.lines_data:
            pen = pg.mkPen(color=color, width=2)
            line = self.plot_widget.plot([], [], pen=pen)
            self.lines_data[name] = {
                'x': [],
                'y': [],
                'line': line,
                'color': color
            }
    
    def add_data_point(self, name, value):
        """Добавление новой точки для конкретной линии с реальным временем"""
        if name not in self.lines_data:
            return
        
        # Используем реальное время с начала эпохи
        current_time = self._get_current_time()
        
        # Если это первая точка - запоминаем время старта
        if self.start_time is None:
            self.start_time = current_time
        
        # Относительное время в секундах от старта программы (реальное!)
        relative_time = current_time - self.start_time
        
        data = self.lines_data[name]
        data['x'].append(relative_time)
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
        current_time = self._get_current_time()
        
        if self.start_time is None:
            self.start_time = current_time
        
        relative_time = current_time - self.start_time
        
        for name, value in data_dict.items():
            if name not in self.lines_data:
                continue
            
            data = self.lines_data[name]
            data['x'].append(relative_time)
            data['y'].append(value)
            
            # Ограничиваем количество точек
            if len(data['x']) > self.max_points:
                data['x'].pop(0)
                data['y'].pop(0)
            
            # Обновляем линию
            if len(data['x']) > 1:
                data['line'].setData(data['x'], data['y'])
    
    def update_view(self):
        """Обновление вида графика (автоскролл)"""
        if self.is_auto_scroll and self.lines_data:
            # Берем первую линию для определения времени
            first_line = next(iter(self.lines_data.values()))
            if first_line['x']:
                max_time = first_line['x'][-1]
                min_time = max(0, max_time - 10)
                self.plot_widget.setXRange(min_time, max_time, padding=0)
    
    def set_auto_scroll(self, enabled):
        """Включить/выключить автоскролл"""
        self.is_auto_scroll = enabled
        if enabled:
            self.update_view()
    
    def clear(self):
        """Очистка графика"""
        for data in self.lines_data.values():
            data['x'].clear()
            data['y'].clear()
            data['line'].setData([], [])
        # Сбрасываем время старта при очистке
        self.start_time = None