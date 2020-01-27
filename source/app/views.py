from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question 
from django.template import loader

# Create your views here.

#------------- Index ---------------------------------------
def indexPrincipal(request):
  all_questions = Question.objects.all()
  #return HttpResponse("Questões = %s." % all_questions)
  context = {'all_questions':all_questions}
  return render(request, 'app/indexPrincipal.html',context)

#------------- APP Votando ---------------------------------------
def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  template = loader.get_template('app/index.html')
  context = { 'latest_question_list': latest_question_list, }
  return render(request, 'app/index.html',context)

def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'app/detail.html', {'question':question})

def results(request, question_id):
  response = ("You're looking at the results of question %s")
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question  %s." % question_id)