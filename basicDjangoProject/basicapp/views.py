from django.shortcuts import render


# Create your views here.
def basicapp(requests):
    return render(requests, 'basicapp/welcome.html')

