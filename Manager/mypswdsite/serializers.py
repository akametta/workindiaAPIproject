from rest_framework import serializers
from .models import Passwords

class PasswordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Passwords
        fields = ('id','website','password','username')