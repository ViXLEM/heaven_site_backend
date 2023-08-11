from rest_framework import serializers
from .models import Table, TableData


class DataSerializer(serializers.ModelSerializer):

    def get_day(self, data_object):

        full_date = getattr(data_object, "date")
        return format(full_date, "%e").replace(" ","")

    def sum(self, data_object):
        total_sum =+ float(getattr(data_object,'data'))
        return total_sum

    day = serializers.SerializerMethodField('get_day')
    totalSum = serializers.SerializerMethodField('sum')

    def __str__(self):
        return f'day_{self.day}'

    class Meta:
        model = TableData
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):

    def sum(self, object):
        sum = 0
        for i in getattr(object, 'tabledata_set').all().values():
            if type(i['data']) == float:
                sum += i['data']
            else:
                pass
        return sum

    clientSurname = serializers.PrimaryKeyRelatedField(read_only=True, source='client.surname')
    clientName = serializers.PrimaryKeyRelatedField(read_only=True, source='client.name')
    operatorName = serializers.PrimaryKeyRelatedField(read_only=True, source='operator.username')
    tabledata_set = DataSerializer(many=True, read_only=True)
    Sum = serializers.SerializerMethodField('sum')

    class Meta:
        model = Table
        fields = '__all__'


class TableCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = '__all__'

class DataSerializer(serializers.ModelSerializer):

    def get_day(self, data_object):

        full_date = getattr(data_object, "date")
        return format(full_date, "%e").replace(" ","")

    def sum(self, data_object):
        total_sum =+ float(getattr(data_object,'data'))
        return total_sum

    day = serializers.SerializerMethodField('get_day')
    totalSum = serializers.SerializerMethodField('sum')

    def __str__(self):
        return f'day_{self.day}'

    class Meta:
        model = TableData
        fields = '__all__'


