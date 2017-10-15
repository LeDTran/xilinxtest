from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from graph.models import Student

import plotly.plotly as py
import plotly.graph_objs as go

import json


# from rest_framework.views import APIView
# from rest_framework.response import Response

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# class Graph(TemplateView):

class Graph(TemplateView):
    template_name = 'graph.html'

    # def get_context_data(self, **kwargs):
    #     context = super(Graph, self).get_context_data(**kwargs)

    #     x = [-2,0,4,6,7]
    #     y = [q**2-q+3 for q in x]
    #     trace1 = go.Scatter(x=x, y=y, marker={'color': 'red', 'symbol': 104, 'size': "10"},
    #                         mode="lines",  name='1st Trace')

    #     data=go.Data([trace1])
    #     layout=go.Layout(title="Meine Daten", xaxis={'title':'x1'}, yaxis={'title':'x2'})
    #     figure=go.Figure(data=data,layout=layout)
    #     div = py.plot(figure, auto_open=False, output_type='div')

    #     context['graph'] = div

    #     return context

    def get(self, request):
        students = Student.objects.all()

        # test1_scores = Student.objects.all().values_list('test1')
        test1 = Student.objects.values_list('test1', flat=True).order_by('test1')
        # test1 = [2.37, 2.16, 4.82, 1.73, 1.04, 0.23, 1.32, 2.91, 0.11, 4.51, 0.51, 3.75, 1.35, 2.98, 4.50, 0.18, 4.66, 1.30, 2.06, 1.19]
        test1_scores= json.dumps(test1)

        test2_scores = Student.objects.values_list('test2', flat=True).order_by('test2')
        test3_scores = Student.objects.values_list('test3', flat=True).order_by('test3')

        getSum(test1_scores)

        return render(request, "graph.html", {'students':students, 'test1_scores':test1_scores})






# def Graph(request):
    # # template_name = 'graph.html'
    # students = Student.objects.all()

    # # test1_scores = Student.objects.all().values_list('test1')
    # test1_scores = Student.objects.values_list('test1', flat=True).order_by('test1')
    # test2_scores = Student.objects.values_list('test2', flat=True).order_by('test2')
    # test3_scores = Student.objects.values_list('test3', flat=True).order_by('test3')

    # getSum(test1_scores)

    # return render(request, "graph.html", {'students':students, 'test1_scores':test1_scores})

# _________________________
# 
#     trace0 = go.Box(
#         y=[2.37, 2.16, 4.82, 1.73, 1.04, 0.23, 1.32, 2.91, 0.11, 4.51, 0.51, 3.75, 1.35, 2.98, 4.50, 0.18, 4.66, 1.30, 2.06, 1.19],
#         name='Only Mean',
#         marker=dict(
#             color='rgb(8, 81, 156)',
#         ),
#         boxmean=True
#     )
#     trace1 = go.Box(
#         y=[2.37, 2.16, 4.82, 1.73, 1.04, 0.23, 1.32, 2.91, 0.11, 4.51, 0.51, 3.75, 1.35, 2.98, 4.50, 0.18, 4.66, 1.30, 2.06, 1.19],
#         name='Mean & SD',
#         marker=dict(
#             color='rgb(10, 140, 208)',
#         ),
#         boxmean='sd'
#     )
#     data = [trace0, trace1]
#     py.iplot(data)
#     return render(request, "graph.html", {'data':data})
# 
# ______________________________
# 
    # x = [-2,0,4,6,7]
    # y = [q**2-q+3 for q in x]
    # trace1 = go.Scatter(x=x, y=y, marker={'color': 'red', 'symbol': 104, 'size': "10"},
    #                     mode="lines",  name='1st Trace')

    # data=go.Data([trace1])
    # layout=go.Layout(title="Meine Daten", xaxis={'title':'x1'}, yaxis={'title':'x2'})
    # figure=go.Figure(data=data,layout=layout)
    # data = py.plot(figure, auto_open=False, output_type='div')
    # return render(request, "graph.html", {'data':data})



def getSum(scores):
    print(scores)
    x=0
    for i in scores:
        # x = x + i
        print(i)
    print(x)
    return 5