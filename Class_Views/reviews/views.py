from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from .forms import ReviewForm
from .models import Review

# Create your views here.

class ReviewView(View):

    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {"form": form})

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        else:
            return render(request, "reviews/review.html", {"form": form})


class ThankYouView(TemplateView):

    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        context['message'] = "this is a dynamic value"  
        return context
    
class ReviewsListView(ListView):

    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews" #name of variable passed to template (default object_list)
    
# class SingleReviewView(TemplateView):

#     template_name="reviews/single_review.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
        
#         review_id = kwargs["id"]
#         review = Review.objects.get(id=review_id)

#         context["review"] = review 
#         return context
    
class SingleReviewView(DetailView):
    
    template_name="reviews/single_review.html"
    model = Review
