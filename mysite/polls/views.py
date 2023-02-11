from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse

from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    
    return render(request, 'polls/index.html', context)

    
def results(request, question_id):
    # Recupera a pergunta pelo seu id
    question = Question.objects.get(pk=question_id)

    # Recupera todas as escolhas relacionadas a essa pergunta
    choices = question.choice_set.all()
    
    context = {'question': question}
    
    return render(request, 'polls/results.html', context)


def vote (request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        print(question_id)
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        
    
    except KeyError:
        return render(request, 'polls/vote.html', {
            'question': question,
            'erro_message': "You didn't select a choice."
            
        })
        
        
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=[question.id]))
        

# Parei em 1:30