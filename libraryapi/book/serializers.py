
from rest_framework import serializers
from book.models import Books
from django.contrib.auth.models import User

class bookserializer(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields=['id','title','author','price']


class userserializer(serializers.ModelSerializer):

    password=serializers.CharField(write_only=True)
    def create(self,validated_data):
        u=User.objects.create(username=validated_data['username'])
        u.set_password(validated_data['password'])
        u.save()
        return u
    class Meta:
        model=User
        fields=['id','username','password']
