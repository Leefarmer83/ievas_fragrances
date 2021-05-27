from newsletter.forms import SubscriberForm


def subform(request):
    form = SubscriberForm()
    return {'subscribe_form': form}
