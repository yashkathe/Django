from django.urls import path

from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank-you", views.ThankYouView.as_view(), name="thank-you-page"),
    path("reviews", views.ReviewsListView.as_view()),
    path("reviews/<int:pk>", views.SingleReviewView.as_view())
]
