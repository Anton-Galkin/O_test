from django.db.models import Q
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Object
from .serializers import ObjectSerializer


# Create your views here.


class ObjectAPIView(generics.ListAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer

    def get(self, request, *args, **kwargs):
        all_objects = Object.objects.all()
        sort = request.GET.get('filter')
        try:
            if sort: all_objects = sort_objects(all_objects, sort)
        except:
            return error500()

        serializer = ObjectSerializer(all_objects, many=True)
        return Response(serializer.data)


class ObjectAPIDetail(generics.RetrieveAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        print(f'pk is: {pk}')

        try:
            pk = int(pk)
        except:
            return error400()

        sort = request.GET.get('filter')
        print(sort)
        if pk == 0:
            all_objects = Object.objects.all()

            try:
                if sort: all_objects = sort_objects(all_objects, sort)
            except:
                return error500()

            serializer = ObjectSerializer(all_objects, many=True)

            return Response(serializer.data)

        try:
            one_object = Object.objects.get(pk=pk)
        except:
            # raise Http404
            return error404()

        # print(f'name object: {one_object}, {one_object.type}, {one_object.parent}')

        # if one_object.parent is not None:
        #     serializer = ObjectSerializer(one_object, )
        #     return Response(serializer.data)

        if str(one_object.type) != 'folder':
            serializer = ObjectSerializer(one_object, )
            print(f'Объект не папка, выводим объект')
            return Response(serializer.data)
        else:
            descendant_objects = Object.objects.filter(Q(parent=pk) | Q(pk=pk))
            print(f'Объект возможно имеет потомков, выводим сам объект и всех потомков (если они есть)')
            if sort:
                try:
                    descendant_objects = sort_objects(descendant_objects, sort)
                except:
                    error500()

            serializer = ObjectSerializer(descendant_objects, many=True)
            return Response(serializer.data)


def sort_objects(objects, sort):
    objects = objects.order_by(sort)
    return objects


def error404():
    content = {'error': 'Объект не найден в БД'}
    return Response(content, status=status.HTTP_404_NOT_FOUND)


def error400():
    content = {'error': 'Введен неверный запрос (id не является числом)'}
    return Response(content, status=status.HTTP_400_BAD_REQUEST)


def error500():
    content = {'error': 'Ошибка сервера'}
    return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
