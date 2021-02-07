from typing import Dict

from main.custom_types import HandlerT, RequestT
from tasks import tasks
from tasks.lesson3 import lesson3, task306, task307, task308, task310, task311
from tasks.lesson4 import lesson4, task404, task406, task407
from tasks.lesson5 import lesson5, task501, task502, task503, task504
from tasks.lesson7 import lesson7, task702, task703
from . import index, error_test
from .system_pages import handle_404

urlpatterns: Dict[str, HandlerT] = {
    '/': index.handler,
    '/e/': error_test.handler,
    '/tasks/': tasks.handler,
    '/tasks/lesson3/': lesson3.handler,
    '/tasks/lesson3/task306/': task306.handler,
    '/tasks/lesson3/task307/': task307.handler,
    '/tasks/lesson3/task308/': task308.handler,
    '/tasks/lesson3/task310/': task310.handler,
    '/tasks/lesson3/task311/': task311.handler,
    '/tasks/lesson4/': lesson4.handler,
    '/tasks/lesson4/task404/': task404.handler,
    '/tasks/lesson4/task406/': task406.handler,
    '/tasks/lesson4/task407/': task407.handler,
    '/tasks/lesson5/': lesson5.handler,
    '/tasks/lesson5/task501/': task501.handler,
    '/tasks/lesson5/task502/': task502.handler,
    '/tasks/lesson5/task503/': task503.handler,
    '/tasks/lesson5/task504/': task504.handler,
    '/tasks/lesson7/': lesson7.handler,
    '/tasks/lesson5/task702/': task702.handler,
    '/tasks/lesson5/task703/': task703.handler,
}


def get_handler(request: RequestT) -> HandlerT:
    handler = urlpatterns.get(request.path, handle_404)

    return handler
