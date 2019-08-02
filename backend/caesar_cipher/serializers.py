from rest_framework import serializers
from .models import Cipher


class CipherSerializer(serializers.ModelSerializer):

    content_encode = serializers.CharField(max_length=100)
    content_decode = serializers.CharField(
        max_length=100, required=False, allow_blank=True)
    shift = serializers.IntegerField()

    class Meta:
        model = Cipher
        fields = ('content_encode', 'content_decode', 'shift')
