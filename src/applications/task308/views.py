from django.views.generic import TemplateView


class Task308View(TemplateView):
    template_name = "task308/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.request.GET.get("digit")
        context["show_text"] = f"--> {solution(data)}" if data else "Input digit..."

        return context


def solution(digit):
    if is_number(digit) and wrong_words(digit):
        float_digit = float(digit)
        cube_digit = float_digit ** 3
        answer = round(cube_digit, 2)
    else:
        answer = "Wrong input!"
    return answer


def wrong_words(n: str) -> bool:
    if n.lower() != "nan" and n.lower() != "inf" and n.lower() != "-inf":
        answer = True
    else:
        answer = False
    return answer


def is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False
