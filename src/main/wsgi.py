import sentry_sdk

from framework.util.settings import get_setting
from main.custom_types import RequestT
from main.pages.function_for_pages import environ_formation
from main.pages.system_pages import division_zero_page, not_found_page, error_500_page
from main.pages.web_pages import tasks_page, lesson3_page, task_306_page, task_307_page, task_308_page, task_310_page, \
    task_311_page, lesson4_page, task_404_page, task_406_page, task_407_page, lesson5_page, task_501_page, \
    task_502_page, task_503_page, task_504_page, index_page, environ_page, lesson7_page, task_702_page

sentry_sdk.init(get_setting("SENTRY_DSN"), traces_sample_rate=1.0)

HANDLERS = {
    '/': index_page,
    '/environ/': environ_page,
    '/e/': division_zero_page,
    '/tasks/': tasks_page,
    '/tasks/lesson3/': lesson3_page,
    '/tasks/lesson3/task306/': task_306_page,
    '/tasks/lesson3/task307/': task_307_page,
    '/tasks/lesson3/task308/': task_308_page,
    '/tasks/lesson3/task310/': task_310_page,
    '/tasks/lesson3/task311/': task_311_page,
    '/tasks/lesson4/': lesson4_page,
    '/tasks/lesson4/task404/': task_404_page,
    '/tasks/lesson4/task406/': task_406_page,
    '/tasks/lesson4/task407/': task_407_page,
    '/tasks/lesson5/': lesson5_page,
    '/tasks/lesson5/task501/': task_501_page,
    '/tasks/lesson5/task502/': task_502_page,
    '/tasks/lesson5/task503/': task_503_page,
    '/tasks/lesson5/task504/': task_504_page,
    '/tasks/lesson7/': lesson7_page,
    '/tasks/lesson5/task702/': task_702_page,
}


def application(environ, start_response):
    request = RequestT(
        method=environ["REQUEST_METHOD"],
        path=environ["PATH_INFO"],
        query_string=environ["QUERY_STRING"],
    )
    headers = {
        "Content-type": "text/html",
    }

    web_page = HANDLERS.get(request.path, not_found_page)

    try:
        response = web_page(request)
    except Exception:
        response = error_500_page(request)

    show_environ = environ_formation(environ)

    start_response(response.status, list(headers.items()))

    show_web_page = response.payload.format(environ=show_environ).encode()

    yield show_web_page
