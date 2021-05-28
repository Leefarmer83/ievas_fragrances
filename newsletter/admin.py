from django.contrib import admin

# Register your models here.
from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "date_added",
    )


admin.site.register(Subscriber, SubscriberAdmin)
