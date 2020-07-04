from django.shortcuts import get_object_or_404 , render
from django.http import HttpResponse
import csv
import xlrd
import pandas as pd
from django.template import loader
from .models import Question
from django.http import Http404

# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.order_by('pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list
#     }
#     return HttpResponse(template.render(context, request))

# Alternate code to index code above(needed to get index in an order)
def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question Does Not Exist")
#     return render(request, 'polls/detail.html', {'question':question})

# Alternate code to get details of a question(and if question doesn't exist raise 404 error)
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You are looking at the results of question %s. "
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s. " % question_id)

# def csv(request, question_id):
#     response = HttpResponse(content_type='text/csv' % question_id)
#     response['Content-Disposition'] = 'attachment; filename= "C:/Users/jayka/Videos/Resume/Tags.csv"'
#     writer = csv.writer(response)
#     return response


