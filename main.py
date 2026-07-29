from hx711_gpiozero import HX711
from time import sleep

# Правильная инициализация для пинов: DT = 24, SCK = 25
scale = HX711(select_pin=24, clock_pin=25)

print("Инициализация...")
init_reading = scale.value
sleep(1)

# Введите известный вес для калибровки
known_weight = float(input("Введите вес эталона в граммах: "))
rel_reading = scale.value
scale_ratio = known_weight / (rel_reading - init_reading)
sleep(1)

# Бесконечный цикл чтения веса
while True:
  current_weight = (scale.value - init_reading) * scale_ratio
  print(f"Вес: {current_weight:.2f} г")
  sleep(1)
