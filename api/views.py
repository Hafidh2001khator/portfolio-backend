from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def profile(request):
    return Response({"name": "Hafidh Hamad Khator"})

@api_view(['GET'])
def skills(request):
    return Response({"skills": ["HTML","CSS","JS","Python"]})

@api_view(['GET'])
def projects(request):
    return Response({"projects": []})

@api_view(['POST'])
def contact(request):
    return Response({"status": "ok"})