from filmoteca_api.serializers.user_serializer import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def user_list(request):
    """create user"""
    serializer = UserSerializer(data=request.data)    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def logout(request):
    request.user.auth_token.delete()
    return Response(status = status.HTTP_200_OK)
