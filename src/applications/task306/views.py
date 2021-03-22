from django.views.generic import TemplateView


class Task306View(TemplateView):
    template_name = "task306/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.request.GET.get("age")
        context["show_text"] = solution(data) if data else "Input your age!"

        return context


def solution(age):
    try:
        age = int(age)
        if age < 0:
            answer = "Wrong input"
        elif age < 18:
            answer = "CocaCola"
        else:
            answer = "Beer"

        return answer

    except ValueError:
        not_digit = "Wrong input"
        return not_digit
