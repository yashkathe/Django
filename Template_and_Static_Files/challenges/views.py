from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january" : "start the year nicely",
    "february" : "approach professor for RA",
    "march": "search for internship",
    "april": None
}

def index(request):

    list_items = ""

    months = monthly_challenges.keys()

    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_by_number(request, month):

    months = list(monthly_challenges.keys())

    if month > len(months): return HttpResponseNotFound("Invalid number")

    # redirect_month = months[month - 1]
    # return HttpResponseRedirect("/api/" + redirect_month)
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):

    try:   
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize()
        })
    except: 
        raise Http404()
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
