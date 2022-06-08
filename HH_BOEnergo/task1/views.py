from django.shortcuts import render
from django.http import HttpResponse
import math


# Create your views here.s
def index(request):

    a = 1
    b = 0
    c = 0

    discr = b ** 2 - 4 * a * c

    if discr > 0:
        x1 = round((-b + math.sqrt(discr)) / (2 * a), 2)
        x2 = round((-b - math.sqrt(discr)) / (2 * a), 2)
        result = 'Имеет два решения'
        # print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif discr == 0:
        x1 = round(-b / (2 * a), 2)
        x2 = '-'
        result = 'Имеет одно решения'
        # print("x = %.2f" % x)
    else:
        x1 = x2 = '-'
        result = 'Корней нет'

    return render(request, 'task1/index.html', {'x1': x1, 'x2': x2, 'number_res': '!', 'result': result})
