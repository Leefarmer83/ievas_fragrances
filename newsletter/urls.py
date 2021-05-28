from newsletter.views import add_subscriber, add_subscriber_form
from django.urls import path

urlpatterns = [
    path("add_subscriber/", add_subscriber, name="add_subscriber"),
    path(
        "add_subscriber_form/", add_subscriber_form, name="add_subscriber_form"
    ),
]
