from hx711_gpiozero import HX711
from time import sleep

# Инициализация датчика с новыми пинами: DT = 24, SCK = 25
scale = HX711(dout=24, pdsck=25)

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
