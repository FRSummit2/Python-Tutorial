from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .utils import Utils
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse


class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])

        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relative_link = reverse('email-verify')
        abs_url = 'http://' + current_site + relative_link + '?token=' + str(token)
        email_body = 'Hi ' + user.username + ' Use link below to verify your email \n' + abs_url
        data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Verify your email'}

        print('-----------------------------------------------------------------')
        print(RefreshToken.for_user(user))
        print('-----------------------------------------------------------------')
        print(user_data)
        print('-----------------------------------------------------------------')
        print(data)
        print('-----------------------------------------------------------------')

        Utils.send_email(data)

        test_data = {token: RefreshToken.for_user(user)}

        return Response(user_data, test_data, status=status.HTTP_201_CREATED)


class VerifyEmail(generics.GenericAPIView):
    def get(self):
        pass
