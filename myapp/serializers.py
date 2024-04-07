from rest_framework import serializers
from .models import UserDetail, OtherName

class OtherNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherName
        fields = ['family_name', 'given_name', 'middle_name']

class UserDetailSerializer(serializers.ModelSerializer):
    other_names = OtherNameSerializer(many=True, required=False)

    class Meta:
        model = UserDetail
        fields = '__all__'

    def create(self, validated_data):
        other_names_data = validated_data.pop('other_names', None)
        user_detail = UserDetail.objects.create(**validated_data)
        if other_names_data:
            for name_data in other_names_data:
                OtherName.objects.create(user_detail=user_detail, **name_data)
        return user_detail

    def update(self, instance, validated_data):
        other_names_data = validated_data.pop('other_names', None)
        if other_names_data:
            instance.other_names.all().delete()  # Clear existing and replace with new
            for name_data in other_names_data:
                OtherName.objects.create(user_detail=instance, **name_data)
        return super().update(instance, validated_data)
