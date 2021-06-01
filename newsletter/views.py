from newsletter.forms import SubscriberForm
from django.http import JsonResponse
from django.template.loader import render_to_string


def add_subscriber(request):
    data = dict()
    form = SubscriberForm()
    context = {"form": form}
    data["html_modal"] = render_to_string(
        "newsletter/includes/subscribe_form.html",
        context,
        request=request,
    )
    return JsonResponse(data)


def add_subscriber_form(request):
    data = dict()
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            data["form_is_valid"] = True
            data["html_success"] = render_to_string(
                "newsletter/includes/subscribe_success.html",
                request=request,
            )
        else:
            data["form_is_valid"] = False
    else:
        form = SubscriberForm()
    context = {"form": form}
    data["html_modal"] = render_to_string(
        "newsletter/includes/subscribe_form.html",
        context,
        request=request,
    )

    return JsonResponse(data)
