from datetime import date, datetime

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Table, TableData, Project
from .serializer import TableSerializer, TableCreationSerializer, DataSerializer


# Create your views here.
class TableView(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

    def list(self, request):

        queryset = Table.objects.prefetch_related('tabledata_set').all()
        # Этот кверисет нужно будет фильтровать по Проэкту - вместо .all() .filter(project_name)
        serializer_class = TableSerializer

        user_group = request.user.groups.all()

        def get_total_sum():
            sum = 0
            for i in Table.objects.prefetch_related('tabledata_set').values('tabledata').all():
                if type(i['tabledata']) == int:
                    sum += i['tabledata']
                else:
                    pass
            return sum

        if request.user.is_staff:
            month = request.query_params['month']
            table_list = Table.objects.prefetch_related('tabledata_set').filter(create_date=f'2023-{month}-01')

            data = serializer_class(table_list, many=True).data
            get_total_sum()
            return Response(data)

        if user_group.filter(name='Operator'):
            month = request.query_params['month']
            table_list = Table.objects.prefetch_related('tabledata_set').filter(operator=int(request.user.pk),
                                                                                date=f'2023-{month}-01')

            data = serializer_class(table_list, many=True).data
            return Response(data)

    def create(self, request, *args, **kwargs):

        serializer_class = TableCreationSerializer

        full_date = date(month=int(request.data['month']), day=1, year=2023)
        client = int(request.data['client'])
        operator = int(request.data['operator'])
        if request.data['tableType']:
            table_type = request.data['tableType']
        else:
            table_type = None
        try:
            account_id = request.data['account_id']
        except KeyError:
            account_id = None
        project = self.get_project_name('OnlyFans')

        data = {'create_date': full_date, 'client': client, 'operator': operator, 'table_type': table_type,
                'account_id': account_id, 'project': project}

        new_table = serializer_class(data=data)
        if new_table.is_valid():
            new_table.save()
            return Response(new_table.data)
        else:
            return new_table.errors

    def get_project_name(self, name):
        return Project.objects.get(site_name=name).pk


class TableDataSet(viewsets.ModelViewSet):
    queryset = TableData.objects.all()
    serializer_class = DataSerializer

    def create(self, request, *args, **kwargs):
        data = request.data['data']
        if ',' in data:
            data = round(float(data.replace(",", ".")), 2)
        full_date = date(month=int(1), day=int(request.data['date']), year=2023)

        try:
            is_day_off = request.data['is_day_off']
        except KeyError:
            is_day_off = False
        table = int(request.data['tableId'])

        table_data = {"data": data, "table": table, "date": full_date, 'is_day_off': is_day_off}

        serializer = DataSerializer(data=table_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(f"{serializer.errors}")

    def partial_update(self, request, pk=None, *args, **kwargs):

        def get_object(pk):
            return TableData.objects.get(pk=pk)

        td_object = get_object(pk=pk)

        data = request.data['data']
        if ',' in data:
            data = float(data.replace(",", "."))

        try:
            is_day_off = request.data['is_day_off']
        except KeyError:
            is_day_off = False

        serializer = DataSerializer(td_object, data={'data': data, 'date': td_object.date,
                                                     'table': int(td_object.table.pk),
                                                     'is_day_off': is_day_off})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'status': 'done'})
        else:
            return Response(serializer.errors)
