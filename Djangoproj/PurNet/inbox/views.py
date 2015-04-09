from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.

def inbox(request):
    return TemplateResponse(request, 'inbox/inbox.html')

def sended(request):
    return TemplateResponse(request, 'inbox/sended.html')

def trash(request):
    return TemplateResponse(request, 'inbox/trash.html')
