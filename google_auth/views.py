from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def api_root(request):
    return Response({
        'auth': 'api/auth/',
        'registration': 'api/auth/registration/',
        'token_obtain_pair': 'api/token/',
        'token_refresh': 'api/token/refresh/',
        'me': 'api/me/',
    })

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "id": request.user.id,
            "email": request.user.email,
            "username": request.user.username,
        })