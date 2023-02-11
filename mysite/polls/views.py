from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World!")

def detail(request, question_id):
    HttpResponse("Essa é pergunta de numero " + question_id)
    
def results(request, question_id):
    response = "Esses são os resultados da pergunda de numero " + question_id
    
    return HttpResponse(response)

def vote (request, question_id):
    response = "Você votou na questão " + question_id
    
    return HttpResponse(response)

# Parei em 1:30