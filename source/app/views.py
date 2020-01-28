from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# Create your views here.

#------------- Index ---------------------------------------
def indexPrincipal(request):
  all_questions = Question.objects.all()
  #return HttpResponse("Questões = %s." % all_questions)
  context = {'all_questions':all_questions}
  return render(request, 'app/indexPrincipal.html',context)

#------------- APP Votando ---------------------------------------

class IndexView(generic.ListView):
  template_name = 'app/index.html'
  context_object_name = 'latest_question_list'

  def get_queryset(self):
      """Return the last five published questions."""
      return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'app/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'app/results.html'


def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
      selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
      # Redisplay the question voting form.
      return render(request, 'app/detail.html', {
          'question': question,
          'error_message': "You didn't select a choice.",
      })
  else:
      selected_choice.votes += 1
      selected_choice.save()
      # Always return an HttpResponseRedirect after successfully dealing
      # with POST data. This prevents data from being posted twice if a
      # user hits the Back button.
      return HttpResponseRedirect(reverse('app:results', args=(question.id,)))