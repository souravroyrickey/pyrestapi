from django.contrib.auth import get_user_model

from .models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

class UserViewSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number']

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=40, allow_blank=True)
    email = serializers.CharField(max_length=80, allow_blank=False)
    phone_number = PhoneNumberField(allow_null=False, allow_blank=False)
    #password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'password','is_stuff']
        extra_kwargs = {'password': {'write_only': True}, }



    def validate(self, attrs):
        user_exist = User.objects.filter(username=attrs['username']).exists()
        if user_exist:
            raise serializers.ValidationError('Username already exist. Please enter different username')

        email_exist = User.objects.filter(email=attrs['email']).exists()
        if email_exist:
            raise serializers.ValidationError('Email already in use. Please use different Email Account')

        phone_exist = User.objects.filter(phone_number=attrs['phone_number']).exists()
        if phone_exist:
            raise serializers.ValidationError('Phone Number already in use. Please use different Phone Number')

        return super().validate(attrs)
