from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import CipherSerializer
from .models import Cipher
import enchant


def get_cipherletter(new_key, letter):
    # still need alpha to find letters
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if letter in alpha:
        return alpha[new_key]
    else:
        return letter


def encode(text, shift):

    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + shift-65) % 26 + 65)
        else:
            result += chr((ord(char) + shift-97) % 26 + 97)
    return result


def decode(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        new_key = (alpha.find(letter) - key) % len(alpha)
        result = result + get_cipherletter(new_key, letter)

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
        eng_dict = enchant.Dict("en_US")
        data = Cipher.objects.order_by('-id').first()
        if data:
            content = data.content_encode
            check = eng_dict.check(content)
            if check:
                shift = data.shift
                result = encode(content, shift)
                Cipher.save_result(result)
            else:
                content = data.content_encode
                shift = data.shift
                result = decode(shift, content)
                Cipher.save_result(result)
        serializer = CipherSerializer(
            data, context={'request': request})
        return Response(serializer.data)
