import time
start_time = 0
is_running = False

def start():
    """Запустить секундомер"""
    global start_time, is_running
    start_time = time.time()
    is_running = True
    print("Секундомер запущен")
    
def stop():
    """Остановить секундомер"""
    global is_running
    if is_running:
        end_time = time.time()
        elapsed = end_time - start_time
        is_running = False
        print(f"Прошло времени: {elapsed:.2f} секунд")
        return elapsed
    else:
        print("Секундомер не запущен")
        return 0

def show():
    """Показать текущее время"""
    global start_time, is_running
    if is_running:
        current_time = time.time() - start_time
        print(f"Текущее время: {current_time:.2f} секунд")
        return current_time
    else:
        print("Секундомер не запущен")
        return 0