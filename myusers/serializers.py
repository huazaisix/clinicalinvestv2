from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import MyUser
from projects.models import ClinicalProjects

import re


class MyUserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('url', 'id', 'email', 'phone')


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicalProjects
        fields = ('name', 'status', 'linkurl', 'description')


class MyUserDetailSerializer(serializers.ModelSerializer):
    # myprojects = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='cp_detail'
    # )
    myprojects = ProjectsSerializer(many=True, read_only=True)

    class Meta:
        model = MyUser
        fields = ('url', 'id', 'email', 'phone', 'user_name', 'hospital', 'address', 'myprojects')

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(help_text=u'旧密码',required=True)
    new_password = serializers.CharField(help_text=u'新密码',required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value


class CreateUserSerializer(serializers.ModelSerializer):
    """
    创建用户的序列化器
    """
    password2 = serializers.CharField(label="确认密码", write_only=True)

    class Meta:
        model = MyUser

        fields = ("id", "email", "password", "password2", "phone", "user_name")

        extra_kwargs = {
            "password": {
                "write_only": True,
                "min_length": 6,
                "max_length": 20,
                "error_messages": {
                    "min_length": "密码允许6-20个字符",
                    "max_length": "密码允许6-20个字符"
                }
            }
        }

    def validate_phone(self, value):
        """验证手机号"""
        if not re.match(r'^1[3-9]\d{9}$', value):
            raise serializers.ValidationError('手机号格式错误')
        return value

    def validate(self, data):
        """
        验证两次输入的密码
        :param data:
        :return:
        """
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("两次密码输入不一致")

        return data

    def create(self, validated_data):
        """
        创建用户
        :param validated_data:
        :return:
        """
        del validated_data["password2"]

        user = super().create(validated_data)

        user.set_password(validated_data['password'])

        user.save()

        return user


