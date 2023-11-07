from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request= request , context={}, template_name='index.html')
