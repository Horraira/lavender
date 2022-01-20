from mobile.models import Mobile
from .serializers import mobileSerializers

from rest_framework.views import APIView

from rest_framework import generics, mixins

from rest_framework.response import Response
# Create your views here.


class mobileLCApiView(generics.ListCreateAPIView):
    queryset = Mobile.objects.all()
    serializer_class = mobileSerializers


class mobileRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mobile.objects.all()
    serializer_class = mobileSerializers

# using mixins with generic class


class mobileCreateListView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Mobile.objects.all()
    serializer_class = mobileSerializers

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class mobileDUDApiView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    queryset = Mobile.objects.all()
    serializer_class = mobileSerializers

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# APIView is general api view every other class is inherited from it
class mobileApiView(APIView):
    def get(self, request, format=None):
        mobile_list = Mobile.objects.all()
        mobile_serializer = mobileSerializers(mobile_list, many=True)
        return Response(mobile_serializer.data)


class mobileListApiView(generics.ListAPIView):
    queryset = Mobile.objects.all()
    serializer_class = mobileSerializers


class mobileCreateApiView(generics.CreateAPIView):
    queryset = Mobile.objects.all()
    serializer_class = mobileSerializers


class mobileDetailApiView(generics.RetrieveAPIView):
    queryset = Mobile.objects.all()
    serializer_class = mobileSerializers


class mobileUpdate(generics.UpdateAPIView):
    queryset = Mobile.objects.all()
    serializer_class = mobileSerializers


class mobileDelete(generics.DestroyAPIView):
    queryset = Mobile.objects.all()
    serializer_class = mobileSerializers