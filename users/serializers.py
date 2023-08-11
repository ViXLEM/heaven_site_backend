from rest_framework import serializers
from users.models import Client, User


class ClientSerializer(serializers.ModelSerializer):
    def get_full_name(self, object):
        name = getattr(object, 'name')
        surname = getattr(object, 'surname')
        return f'{name} {surname}'

    def get_id(self, object):
        id = getattr(object, 'pk')
        return int(id)

    full_name = serializers.SerializerMethodField('get_full_name')
    id = serializers.SerializerMethodField('get_id')

    class Meta:
        model = Client
        fields = '__all__'



class PermissionSerializer(serializers.ModelSerializer):

    user_permissions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("id", "first_name", 'user_permissions')

    def get_user_permissions(self, obj):
        return list(obj._user_get_permissions("all"))


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'



class ClientListSerializer(serializers.ModelSerializer):

    def get_full_name(self, object):
        name = getattr(object, 'name')
        surname = getattr(object, 'surname')
        return f'{name} {surname}'

    def get_id(self, object):
        id = getattr(object, 'pk')
        return int(id)

    full_name = serializers.SerializerMethodField('get_full_name')
    id = serializers.SerializerMethodField('get_id')


    class Meta:
        model = Client
        fields = ['full_name', 'id', 'photo']



class OperatorToClient(serializers.Serializer):

    operator = serializers.SerializerMethodField('getOperatorList')

    def getOperatorList(self, data_object):
        pk = getattr(data_object,'pk')
        name = getattr(data_object, 'name')
        surname = getattr(data_object, 'surname')
        return {'id': pk, 'fullName': f'{name} {surname}'}