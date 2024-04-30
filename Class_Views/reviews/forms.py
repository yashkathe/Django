from django import forms

from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(
#         label="User Name",
#         required=True,
#         max_length=30,
#         error_messages={
#             "required": "Your name can't be empty",
#             "max_length": "Please enter shorter name",
#         },
#     )

#     review_text = forms.CharField(
#         label="Your Feedback", widget=forms.Textarea, max_length=200
#     )

#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


"""
Infer Form from our database Model
"""

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            "user_name" : "Your name",
            "review_text" : "Your FeedBack",
            "rating": "Your Rating"
        }
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty"
            }
        }