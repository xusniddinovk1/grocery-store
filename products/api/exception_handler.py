from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None:
        return Response(
            {"detail": "Server ichki xatolik (500)."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    if response.status_code == 404:
        response.data = {"detail": "Sahifa yoki resurs topilmadi (404)."}

    return response
