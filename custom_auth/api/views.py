from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def login(request):
    return Response("Hello, auth page.")

@api_view(['POST'])
def create_access_by_rt(request):
    return Response("get AT by RT")