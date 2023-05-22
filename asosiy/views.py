from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *
from rest_framework.viewsets import ModelViewSet


class MurojaatViewSet(ModelViewSet):
    queryset = Murojaat.objects.all()
    serializer_class = MurojaatSerializer
    http_method_names = ['post']

class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    http_method_names = ['get']

class Home_pageViewSet(ModelViewSet):
    queryset = Home_page.objects.all()
    serializer_class = Home_pageSerializer
    http_method_names = ['get']

class MaqolalarAPIView(APIView):
    def get(self, request):
        maqolalar = Maqola.objects.all().order_by('-sana')
        serializer = MaqolaSerializer(maqolalar, many=True)
        return Response(serializer.data)

class Bosh_menu_MaqolalariAPIView(APIView):
    def get(self, request):
        maqolalar = Maqola.objects.filter(bosh_sahifa_uchun=True).order_by('-sana')
        serializer = MaqolaSerializer(maqolalar, many=True)
        return Response(serializer.data)

class MaqolalarTopAPIView(APIView):
    def get(self, request):
        maqolalar = Maqola.objects.order_by('-korilganlik')[:4]
        serializer = MaqolaSerializer(maqolalar, many=True)
        return Response(serializer.data)

class MaqolaDetailAPIView(APIView):
    def get(self, request, pk):
        maqola = Maqola.objects.get(id=pk)
        serializer = MaqolaSerializer(maqola)
        view_sanoq = maqola.korilganlik
        view_sanoq += 1
        maqola.korilganlik = view_sanoq
        maqola.save()
        print(maqola.korilganlik)
        return Response(serializer.data)

class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all().order_by('-sana')
    serializer_class = VideoSerializer
    http_method_names = ['get']
    order_fields = ['sana', 'sarlavha', 'sarlavhaeng', 'sarlavharu']
    search_fields = ['sana', 'sarlavha', 'sarlavhaeng', 'sarlavharu', 'matn', 'matneng', 'matnru']

class Ijtimoiy_tarmoqViewSet(ModelViewSet):
    queryset = Ijtimoiy_tarmoq_url.objects.all()
    serializer_class = Ijtimoiy_tarmoq_urlSerializer
    http_method_names = ['get']

class Haqida_toliqViewSet(ModelViewSet):
    queryset = Haqida_toliq.objects.all()
    serializer_class = Haqida_toliqSerializer
    http_method_names = ['get']

class FaoliyatAPIView(APIView):
    def get(self, request):
        faoliyat = Faoliyat_joy.objects.all()
        serializer = Faoliyat_joySerializer(faoliyat)
        return Response(serializer.data)

class HamkorAPIView(APIView):
    def get(self, request):
        hamkorlar = Hamkor.objects.all()
        serializer = HamkorSerializer(hamkorlar)
        return Response(serializer.data)
