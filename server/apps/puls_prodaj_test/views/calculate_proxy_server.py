import time
from django.http import HttpResponse


PROXIES = ['http://52.88.38.63', 'http://188.127.251.4:32911']
ONE_PROXY_CALLS_BY_MINUTE = 30

current_proxy_index = -1
last_minute_start = None
current_proxy_calls = 0


# Функция, которая распределяем нагрузку между прокси серверами

# Если количество запросов достигло лимита,
# то делает задержку на отдачу прокси сервера
def calculate_proxy_server(request, *args, **kwargs):
    global current_proxy_index, last_minute_start, current_proxy_calls

    current_proxy_calls += 1
    # Если количество запросов превышено, то делаем задержку
    if current_proxy_calls > len(PROXIES) * ONE_PROXY_CALLS_BY_MINUTE:
        wait_time = 60 - (time.time() - last_minute_start)
        time.sleep(wait_time)

    # Если последняя минуты истекла или не была определена, то определяем новую
    if last_minute_start == None or last_minute_start < time.time() - 60:
        last_minute_start = time.time()
        current_proxy_calls = 0

    # Определяем индекс прокси сервера
    current_proxy_index += 1
    if current_proxy_index >= len(PROXIES):
        current_proxy_index = 0

    return HttpResponse(PROXIES[current_proxy_index])
