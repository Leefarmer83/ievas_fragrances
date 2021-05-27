from newsletter.forms import SubscriberForm
from django.shortcuts import redirect


def add_subscriber(request):

    redirect_url = request.POST.get("redirect_url")
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect(redirect_url)
