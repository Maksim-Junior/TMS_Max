from django.views.generic import TemplateView


class Task311View(TemplateView):
    template_name = "task311/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.request.GET.get("gmail")
        context["show_text"] = solution(data) if data else "Input your Gmail!"

        return context


def solution(gmail: str) -> str:
    if gmail[-10:] == "@gmail.com":
        address = gmail
    else:
        address = "DOMAIN NAME is not supported"

    return address
