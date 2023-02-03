import json

from django.shortcuts import render
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    print(request.GET)
    print(request.POST)
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    data['headers'] = dict(request.headers)
    print(data['headers'])
    data['content_type'] = request.content_type
    return JsonResponse({"message": "Django API Response"})
