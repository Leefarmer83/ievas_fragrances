from newsletter.views import add_subscriber
from django.urls import path

urlpatterns = [path("add_subscriber", add_subscriber, name="add_subscriber"), ]
