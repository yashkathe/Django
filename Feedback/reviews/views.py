from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View

from .forms import ReviewForm
# from .models import Review

# Create your views here.

"""
Class Based Views
"""

# class ReviewView(View):
    
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "reviews/review.html", {"form": form})

#     def post(self, request):
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")
#         else:
#             return render(request, "reviews/review.html", {"form": form})


def review(request):

    if request.method == "POST":
        form = ReviewForm(request.POST)

        """
        for updating exisitng data
        """
        # exisitng_data = Review.objects.get(id=1)
        # form = ReviewForm(request.POST, instance=exisitng_data)

        if form.is_valid():
            # review = Review(
            #     user_name=form.cleaned_data["user_name"],
            #     review_text=form.cleaned_data["review_text"],
            #     rating=form.cleaned_data["rating"],
            # )
            # review.save()

            """
            when we directly use ModelForm
            """
            form.save()

            return HttpResponseRedirect("/thank-you")

    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {"form": form})


def thank_you(request):
    return render(request, "reviews/thank_you.html")
