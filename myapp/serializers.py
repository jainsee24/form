from rest_framework import serializers
from .models import UserDetail, OtherName, ApplicationType

class ApplicationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationType
        fields = '__all__'

class OtherNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherName
        fields = '__all__'

class UserDetailSerializer(serializers.ModelSerializer):
    application_type = ApplicationTypeSerializer(required=False)
    other_names = OtherNameSerializer(many=True, required=False)

    class Meta:
        model = UserDetail
        fields = '__all__'

    def create(self, validated_data):
        application_type_data = validated_data.pop('application_type', None)
        other_names_data = validated_data.pop('other_names', [])
        user_detail = UserDetail.objects.create(**validated_data)

        if application_type_data:
            ApplicationType.objects.create(user_detail=user_detail, **application_type_data)
        
        for name_data in other_names_data:
            OtherName.objects.create(user_detail=user_detail, **name_data)

        return user_detail

    def update(self, instance, validated_data):
        application_type_data = validated_data.pop('application_type', None)
        other_names_data = validated_data.pop('other_names', [])

        # Update ApplicationType
        if application_type_data:
            ApplicationType.objects.update_or_create(user_detail=instance, defaults=application_type_data)

        # Update OtherNames
        instance.other_names.all().delete()  # Clear existing
        for name_data in other_names_data:
            OtherName.objects.create(user_detail=instance, **name_data)

        # Update UserDetail
        return super().update(instance, validated_data)
