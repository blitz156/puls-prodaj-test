import requests
from django.http import JsonResponse
from django_redis import get_redis_connection


# Функция, которая достанет данные по урлу из кеша,
# либо сходит за ними на один из прокси серверов
def external_proxy(request, *args, **kwargs):
    cache_con = get_redis_connection('default')

    result_src = 'cache'
    result = cache_con.get(request.path)
    if result:
        # Если получилось достать из кеша
        result = result.decode('utf-8')
    else:
        # Если в кеше нет, идем на один из прокси серверов

        # Определением прокси сервера занимается отдельный инстанс приложения,
        # он должен быть только в одном экземпляре с одним воркером
        proxy_server = requests.get('http://calculate-proxy-server:8001/proxy_address').content.decode('utf-8')
        result_src = 'external-proxy = {}'.format(proxy_server)

        # После того, как получили адрес прокси сервера идем к нему за данными
        result = requests.get('{ip}{path}'.format(ip=proxy_server, path=request.path)).content.decode('utf-8')

        # Кладем данные в кеш на одну минуту
        cache_con.set(request.path, result, 60)

    return JsonResponse({'result': result, 'result_src': result_src})
