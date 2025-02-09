# This fiel is created by me not by Django

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def started(request):
    return render(request,"index2.html")
def about2(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def help(request):
    return render(request,"help.html")
def back(request):
    return HttpResponse('<a href="/">back</a>')
def about(request):
    punc='.,"?!@#$%^&*_-;:`'
    data = request.GET.get('text', 'default')
    capital = request.GET.get("box", 'off')
    lowerCase = request.GET.get("box2", "off")
    length = request.GET.get("box3", "off")
    removePunc = request.GET.get("box4", "off")
    removeDS = request.GET.get("box5", "off")

    result = []  # List to hold multiple results

    # Apply transformations based on the checkboxes selected
    if capital == "on":
        result.append(f"Uppercase: {data.upper()}")
    if lowerCase == "on":
        result.append(f"Lowercase: {data.lower()}")
    if length == "on":
        result.append(f"Length: {len(data)}")
    if removePunc == "on":
        result.append(f"Without Punctuation: {''.join([char for char in data if char not in punc])}")
    if removeDS == "on":
        result.append(f"Without Extra Spaces: {' '.join(data.split())}")
    
    # Combine all results into a single response
    return render(request, 'output.html', {'result': "<br>".join(result)})