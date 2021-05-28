from django import forms

from .models import Subscriber


class SubscriberForm(forms.ModelForm):
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(
            attrs={"placeholder": "Your email", "class": "form-control"}
        ),
    )

    class Meta:
        model = Subscriber
        fields = ["email"]
