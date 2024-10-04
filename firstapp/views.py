from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(response):
    return HttpResponse("<h1><b> This is the home page</b></h1><br><h2><center>Web Application Development using Django framework<center></h2>")

def about(response):
    return HttpResponse("<h1><b>This is the about page</b></h1><br><br><h2>&nbsp&nbsp&nbsp&nbsp&nbspI am Hemadharshini R, Student in the Department of Information Technology at Kamaraj College of Engineering and Technology.</h2><br><br><h2>&nbsp&nbsp&nbsp&nbsp&nbspI am passionate about coding. My areas of interest are Machine Learning, Deep learning, IoT, Web Development and Networks</h2>")
