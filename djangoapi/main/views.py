from django.shortcuts import render
from .serializers import *
from rest_framework.generics import *
from rest_framework.views import *
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
# Create your views here.

class ResgisterView(APIView):
    def post(self, request):
        try:
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            country_code = request.POST.get('country_code')
            name = request.POST.get('name')
            image = request.FILES.get('image')
            password = request.POST.get('password')
            
            check_mobile = User.objects.filter(mobile=mobile).first()
            check_email = User.objects.filter(email=email).first()

            if check_mobile:
                return Response(
                    {"message": "mobile Already Exists", 'success': False, 'is_register': False, "mobile": mobile},
                    status=status.HTTP_400_BAD_REQUEST)
            if check_email:
                return Response(
                    {"message": "email Already Exists", 'success': False, 'is_register': False, "email": email},
                    status=status.HTTP_400_BAD_REQUEST)


            user = User(email=email, image=image, name=name,mobile=mobile, country_code=country_code)
            user.set_password(password)
            user.save()
            return Response({"message": "Your Registrations is successfully", "success": True, 'is_register': True,
                             "user": {
                                 'id': user.id,
                                 'email': user.email,
                                 'mobile': user.mobile,
                                 'country_code': user.country_code,
                                 'name': user.name,}},
                            status=status.HTTP_201_CREATED)

        except Exception as e:
            print(e)
            return Response({'success': False, 'message': 'internal server error', 'is_register': False},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class LoginView(APIView):
    def post(self, request, *args, **kwargs):

        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email, password=password)        
            if user is None:
                return Response(
                    {"message": "Email not registered", "success": False, 'is_register': False},
                    status=status.HTTP_404_NOT_FOUND)
            login(request, user)
            user = authenticate(username=email, password=password)
            return Response({"message": "Done", "success": True, 'is_register': True, "user": {
                'id': user.id,
                'email': user.email,
                'mobile': user.mobile,
                'country_code': user.country_code,
                'name': user.name,}},
                            status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'success': False, 'message': 'internal server error'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            
            


class UserUpdate(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer