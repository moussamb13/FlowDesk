# Create your views here.
# --------------------------------------------------------
# API Views for registration and login
# Uses DRF generic views and JWT for authentication
# --------------------------------------------------------

from rest_framework import generics
# from .serializers import RegisterSerializer
# from rest_framework_simplejwt.tokens import RefreshToken

# User registration view
class RegisterView(generics.CreateAPIView):
    """
    Handles POST requests to register new users
    """
    # serializer_class = RegisterSerializer
