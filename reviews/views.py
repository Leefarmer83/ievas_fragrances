from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from profiles.models import UserProfile
from .forms import ReviewForm
from django.http import JsonResponse
from django.template.loader import render_to_string


@login_required
def add_review_form(request, product_id):
    data = dict()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        product = get_object_or_404(Product, pk=product_id)
        user_profile = get_object_or_404(UserProfile, user=request.user)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_profile = user_profile
            instance.product = product
            instance.save()
            
            data["form_is_valid"] = True
            
            data["html_success"] = render_to_string(
                "reviews/includes/review_success.html",
                request=request,
            )
            data["html_review"] = render_to_string(
                "products/includes/product_reviews.html",
                request=request,
                context={"product": product}
            )
            data["html_rating"] = render_to_string(
                "products/includes/product_rating.html",
                request=request,
                context={"product": product}
            )
        else:
            data["form_is_valid"] = False
    else:
        form = ReviewForm()
    context = {"form": form, "product_id": product_id}
    data["html_modal"] = render_to_string(
        "reviews/includes/add_review_form.html",
        context,
        request=request,
    )

    return JsonResponse(data)


def add_review(request, product_id):
    data = dict()
    form = ReviewForm()
    context = {"form": form, "product_id": product_id}
    data["html_modal"] = render_to_string(
        "reviews/includes/add_review_form.html",
        context,
        request=request,
    )
    return JsonResponse(data)
