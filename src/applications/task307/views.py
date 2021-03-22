from django.views.generic import TemplateView


class Task307View(TemplateView):
    template_name = "task307/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.request.GET.get("string")
        context["show_text"] = solution(data) if data else "Input string..."

        return context


def solution(string):
    if len(string) > 5:
        answer = f'"{string}"'
    elif len(string) < 5:
        answer = "Need more!"
    else:
        answer = "It is five"

    return answer
