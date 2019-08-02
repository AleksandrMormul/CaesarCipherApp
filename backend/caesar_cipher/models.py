from django.db import models


class Cipher(models.Model):
    shift = models.IntegerField()
    content_encode = models.CharField(max_length=100)
    content_decode = models.CharField(max_length=100, null=True)

    def __str__(self):
        "String representation of the Cipher object."
        return f'Content {self.pk}'

    @classmethod
    def save_result(cls, text):
        cipher = cls.objects.order_by('-id').first()
        cipher.content_decode = text
        cipher.save()
