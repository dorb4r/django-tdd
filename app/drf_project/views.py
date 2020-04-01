"""
General views
"""

from django.http import JsonResponse


def ping(request):
    """

    :param request:
    :return:
    """
    data = {"ping": "pong!"}
    return JsonResponse(data)
