from django.shortcuts import get_object_or_404 , render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
import csv
import xlrd
import pandas as pd
from django.template import loader
from .models import Choice, Question
from django.views import generic
from django.http import Http404


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'




# OLD CODE(Hard Coded)

# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.order_by('pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list
#     }
#     return HttpResponse(template.render(context, request))

# Alternate code to index code above(needed to get index in an order)
# def index(request):
#     latest_question_list = Question.objects.order_by('pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question Does Not Exist")
#     return render(request, 'polls/detail.html', {'question':question})

# Alternate code to get details of a question(and if question doesn't exist raise 404 error)
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# def csv(request, question_id):
#     response = HttpResponse(content_type='text/csv' % question_id)
#     response['Content-Disposition'] = 'attachment; filename= "C:/Users/jayka/Videos/Resume/Tags.csv"'
#     writer = csv.writer(response)
#     return response


