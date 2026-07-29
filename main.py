from hx711_gpiozero import HX711
from time import sleep

# ЗАМЕНИТЕ ЭТО ЗНАЧЕНИЕ НА ВАШ СКАЛИРУЮЩИЙ КОЭФФИЦИЕНТ
SCALE_RATIO = 0.00234  

# Инициализация датчика на пинах 24 и 25
scale = HX711(select_pin=24, clock_pin=25)

print("Очистите весы. Идет автоматическое обнуление...")
sleep(2)  # Даем датчику стабилизироваться

# Запоминаем и выводим значение пустой тары
init_reading = scale.value  
print(f"-> Значение пустой тары (init_reading): {init_reading}")
print("Весы готовы к работе!")

try:
    while True:
        # Рассчитываем чистый вес
        current_weight = (scale.value - init_reading) * SCALE_RATIO
        
        # Сглаживаем околонулевые колебания от шума
        if abs(current_weight) < 0.1: 
            current_weight = 0.0
            
        print(f"Вес: {current_weight:.2f} г")
        sleep(0.5)

except KeyboardInterrupt:
    print("\nПрограмма остановлена.")
