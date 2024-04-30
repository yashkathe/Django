from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from .forms import ProfileForm
from .models import UserProfile

# Create your views here.

# def store_file(file):
#     with open("temp/image.jpg", "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)


class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {"form": form})

    def post(self, request):
        # request.POST

        submitted_form = ProfileForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            profile = UserProfile(image=request.FILES["user_image"])
            profile.save()
            return HttpResponseRedirect("/profiles")
        else:
            return render(
                request, "profiles/create_profile.html", {"form": submitted_form}
            )


class ListProfilesView(View):
    def get(self, request):
        profiles = UserProfile.objects.all()
        print(profiles[0].image)
        return render(request, "profiles/user_profiles.html", {"profiles": profiles})
