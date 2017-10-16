from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from django.db.models import Avg

from graph.models import Student

import csv
import statistics

import plotly.plotly as py
import plotly.graph_objs as go

import simplejson as json

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class Graph(TemplateView):
    template_name = 'graph.html'

    def get(self, request):
        students = Student.objects.all()

        test1 = Student.objects.values_list('test1', flat=True).order_by('test1')[::1]     
        test1_scores= json.dumps(test1)

        test2 = Student.objects.values_list('test2', flat=True).order_by('test2')[::1] 
        test2_scores= json.dumps(test2)

        test3 = Student.objects.values_list('test3', flat=True).order_by('test3')[::1] 
        test3_scores= json.dumps(test3)

        final = Student.objects.values_list('final', flat=True).order_by('final')[::1] 
        final_scores= json.dumps(final)

        print(statistics.mean(test1))


        return render(request, "graph.html", {'students':students, 'test1':test1_scores, 
            'test2':test2_scores, 'test3':test3_scores, 'final':final_scores})

        # Manual specifiction of boxplot points
        # [min, q1, q1, median, q3, q3, max]

def ExportGraphCSV(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['Student', 'Test 1', 'Test 2', 'Test 3', 'Final'])

    students = Student.objects.all().values_list('name', 'test1', 'test2', 'test3', 'final')
    for student in students:
        writer.writerow(student)


    test1 = Student.objects.values_list('test1', flat=True).order_by('test1')[::1]     
    test2 = Student.objects.values_list('test2', flat=True).order_by('test2')[::1] 
    test3 = Student.objects.values_list('test3', flat=True).order_by('test3')[::1] 
    final = Student.objects.values_list('final', flat=True).order_by('final')[::1] 
 
    t1_avg = statistics.mean(test1)
    t2_avg = statistics.mean(test2)
    t3_avg = statistics.mean(test3)
    final_avg = statistics.mean(final)

    t1_sd = statistics.stdev(test1)
    t2_sd = statistics.stdev(test2)
    t3_sd = statistics.stdev(test3)
    final_sd = statistics.stdev(final)

    # t1_avg = students.aggregate(avg=Avg('test1'))['avg']

    writer.writerow([])
    writer.writerow(['', 'Test 1', 'Test 2', 'Test 3', 'Final'])
    writer.writerow(['Mean', t1_avg, t2_avg, t3_avg, final_avg])
    writer.writerow(['StDev', t1_sd, t2_sd, t3_sd, final_sd])

    return response

