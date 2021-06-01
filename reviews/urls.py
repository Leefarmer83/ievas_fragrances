from reviews.views import add_review, add_review_form
from django.urls import path

urlpatterns = [
    path("add_review/<product_id>/", add_review, name="add_review"),
    path(
        "add_review_form/<product_id>/",
        add_review_form,
        name="add_review_form",
    ),
]
