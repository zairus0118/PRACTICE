from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    # write_only: accepted on input, never included in a response
    password = serializers.CharField(write_only=True, validators=[validate_password])
    # temporary field: not a model field, never saved
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "confirm_password",
            "avatar",
            "level",
        ]

    def validate(self, attrs):
        # Object-level check. On PATCH the password fields are optional,
        # but if one is sent, both must be sent and must match.
        password = attrs.get("password")
        confirm_password = attrs.pop("confirm_password", None)
        if password is not None or confirm_password is not None:
            if password != confirm_password:
                raise serializers.ValidationError(
                    {"confirm_password": "Passwords do not match."}
                )
        return attrs

    def create(self, validated_data):
        # create_user hashes the password
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)  # hash the new password
            user.save()
        return user
