from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def test_covid(request):
    response = {}

    for key, value in request.POST.items():
        if key != 'csrfmiddlewaretoken':
            response[key] = value

    return JsonResponse({
        'message': 'Data Received',
        'data': response,
    })
