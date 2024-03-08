from django.shortcuts import render
from faker import Faker

def index(req):
    fake = Faker()
    return render(req, 'index.html', {'fake': fake})