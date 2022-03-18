from django.views.generic import TemplateView

from firebase_admin import auth
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import User
from .serializers import LoginSocialSerializer


class LoginView(TemplateView):
    template_name = 'users/login.html'
    
    
class GoogleLoginView(APIView):
    serializer_class = LoginSocialSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        id_token = serializer.data.get('token_id')
        decoded_token = auth.verify_id_token(id_token)
        email = decoded_token['email']
        name = decoded_token['name']
        
        usuario, created = User.objects.get_or_create(
            email=email,
            defaults={
                'full_name': name,
                'email': email,
                'is_active' : True
            }
        )
        
        if created:
            token = Token.objects.create(user = usuario)
        else:
            token = Token.objects.get(user=usuario)
            
        userGet = {
            'id': usuario.pk,
            'email': usuario.email,
            'city' : usuario.city,
            'genero' : usuario.genero,
            'full_name' : usuario.full_name,
            'date_birth' : usuario.date_birth,
        }
        
        return Response({
            'token': token.key,
            'user': userGet
        })
        
        
        