import sentry_sdk

from framework.util.settings import get_setting

sentry_sdk.init(get_setting("SENTRY_DSN"), traces_sample_rate=1.0)


def application(environ, start_response):
    if environ["PATH_INFO"] == "/e/":
        division = 1 / 0

    status = "200 OK"

    headers = {
        "Content-type": "text/html",
    }

    payload = (
        b"<!DOCTYPE html>"
        b"<html>"
        b"<head>"
        b"<title>Maksim</title>"
        b"<style>"
        b"body {" 
        b"background: #333;"
        b"}"
        b"<style>"
        b'<meta charset="utf-8">'
        b"</head>"
        b"<body>"
        b"<h1 style='text-align:center'>It's my project!</h1>"
        b"<hr style='border: 2px solid white;'>"
        b"<p>This is a template project.</p>"
        b"</body>"
        b"</html>"
    )

    start_response(status, list(headers.items()))

    yield payload
