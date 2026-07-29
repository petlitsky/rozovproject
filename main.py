import time
from hx711_gpiozero import HX711

print("1. Запуск теста HX711...")

try:
    # Важно: имена параметров строго 'dout' и 'sck'
    hx = HX711(dout=24, sck=25)
    print("2. Датчик успешно инициализирован.")
    
    print("3. Пробуем прочитать 5 значений:")
    for i in range(5):
        val = hx.value
        print(f"  Замер {i+1}: {val}")
        time.sleep(0.5)

except Exception as e:
    print(f"❌ Ошибка: {e}")

print("4. Тест завершен.")