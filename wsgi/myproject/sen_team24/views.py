from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	name="star";
	html="<htm><body><h1>Just Checking/h1></body><html>"
	return HttpResponse(html);
