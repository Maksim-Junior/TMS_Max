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
        b"a {"
        b"color:#F0FFF0;"
        b"}"
        b"a:hover {"
        b"color:#800000;"
        b"}"
        b"</style>"
        b'<meta charset="utf-8">'
        b"</head>"
        b"<body bgcolor='#696969'>"
        b"<h1 style='text-align:center;color:#F5F5DC;font-family: courier, monospace'>It's my project!</h1>"
        b"<hr style='border-width: 2px;border-color:#800000;'>"
        b"<h2 style='text-align:center;color:#F0FFF0;font-style:italic;'>"
        b"<a style='text-decoration: none;'; href='https://www.pexels.com/search/animals/'>"
        b"-->Some animals photo(click)<--</a></h2> "
        b"<h2 style='color:#FFA07A'>What is Python?</h2>"
        b"<p style = 'color:#E6E6FA;font-family: courier, monospace;'>Python is an interpreted, object-oriented, "
        b"high-level programming language with dynamic semantics. Its high-level built in data structures,"
        b" combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development,"
        b" as well as for use as a scripting or glue language to connect existing components together."
        b" Python's simple, easy to learn syntax emphasizes readability and therefore reduces"
        b" the cost of program maintenance. Python supports modules and packages,"
        b" which encourages program modularity and code reuse."
        b"The Python interpreter and the extensive standard library are available in source or binary"
        b" form without charge for all major platforms, and can be freely distributed.</p>"
        b"</body>"
        b"</html>"вв
    )

    start_response(status, list(headers.items()))

    yield payload
