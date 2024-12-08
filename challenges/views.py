from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# Create your views here.

monthlyChallenges={
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes everyday!",
    "march": "Learn Django for at least 20 minutes everyday!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes everyday!",
    "june": "Learn Django for at least 20 minutes everyday!",
    "june": "Walk for at least 20 minutes everyday!",
    "july": "Eat no meat for the entire month!",
    "august":  "Learn Django for at least 20 minutes everyday!",
    "september": "Walk for at least 20 minutes everyday!",
    "october": "Eat no meat for the entire month!",
    "november":  "Learn Django for at least 20 minutes everyday!",
    "december": "Walk for at least 20 minutes everyday!",
}
def monthly_challengeN(request, month):
   
   months = list(monthlyChallenges.keys())
   
   if month > len(months):
      return HttpResponseNotFound("Invalid month")
   
   redirect_month=months[month-1]
   
   return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
   try:
      text=monthlyChallenges[month]
      return HttpResponse(text)
   except:
      return HttpResponseNotFound("This month is not supported!")
