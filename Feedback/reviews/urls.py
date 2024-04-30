from django.urls import path

from . import views

urlpatterns = [
    path("", views.review),
    # path("", views.ReviewView.as_view()), # for class based views
    path("thank-you", views.thank_you, name="thank-you-page")
]
