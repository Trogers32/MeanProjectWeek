from django.shortcuts import render, redirect
from django.contrib import messages
import datetime
import bcrypt
from django.core.urlresolvers import reverse

def home(request):
    return render(request, "index/index.html")