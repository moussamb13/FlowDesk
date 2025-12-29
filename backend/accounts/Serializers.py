# --------------------------------------------------------
# Serializers for User registration and authentication
# DRF serializers convert model instances to JSON and
# handle validation for API endpoints
# --------------------------------------------------------

from rest_framework import serializers
# from .models import User  # Uncomment when User model is active
# from django.contrib.auth.password_validation import validate_password

# Serializer for user registration
class RegisterSerializer(serializers.ModelSerializer):
    """
    Handles creation of new users via API
    """

    # Password field with write-only access
    password = serializers.CharField(write_only=True, required=True)  # , validators=[validate_password])

    # Meta information linking serializer to User model
    class Meta:
        # model = User  # Uncomment when User model is active
        fields = ['email', 'full_name', 'password']

    # Method called on serializer.save()
    def create(self, validated_data):
        # Create user using custom manager
        # user = User.objects.create_user(
        #     email=validated_data['email'],
        #     full_name=validated_data.get('full_name', ''),
        #     password=validated_data['password']
        # )
        # return user
        pass
