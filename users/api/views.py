from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def users(request):
    if request.method == 'GET':
        return Response({
            "message": "Hello, users page.",
        })
    elif request.method == 'POST':
        return Response({
            "message": "Hello, users mypage.",
        })
    else:
        return Response({
            "message": "error",
        })