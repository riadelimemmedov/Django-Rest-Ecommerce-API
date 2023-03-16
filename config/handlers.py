from django.http import JsonResponse
from rest_framework import status


#!handler400
def handler400(request, *args, **argv):
    data = {"code": 400, "message": "Bad request.", "body": None}
    return JsonResponse(data=data, status=status.HTTP_400_BAD_REQUEST)


#!handler403
def handler403(request, *args, **argv):
    data = {"code": 403, "message": "Forbidden.", "body": None}
    return JsonResponse(data=data, status=status.HTTP_403_FORBIDDEN)


#!handler404
def handler404(request, *args, **argv):
    data = {"code": 404, "message": "Not found.", "body": None}
    return JsonResponse(data=data, status=status.HTTP_404_NOT_FOUND)


#!handler500
def handler500(request, *args, **argv):
    data = {"code": 500, "message": "Internal Server Error.", "body": None}
    return JsonResponse(data=data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
