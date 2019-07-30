from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import CipherSerializer
from .models import Cipher


def encode(text, shift):

    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + shift-65) % 26 + 65)
        else:
            result += chr((ord(char) + shift-97) % 26 + 97)
    return result


class CaesarCipherView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request, format='json'):
        data = request.data
        serializer = CipherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        data = Cipher.objects.order_by('-id').first()
        content = data.content_encode
        serializer = CipherSerializer(
            data, context={'request': request})
        return Response(serializer.data)
