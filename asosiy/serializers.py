from .models import *
from rest_framework.serializers import ModelSerializer


class MurojaatSerializer(ModelSerializer):
    class Meta:
        model = Murojaat
        fields = '__all__'

class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class Home_pageSerializer(ModelSerializer):
    class Meta:
        model = Home_page
        fields = '__all__'

class MaqolaSerializer(ModelSerializer):
    class Meta:
        model = Maqola
        fields = '__all__'

class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class Ijtimoiy_tarmoq_urlSerializer(ModelSerializer):
    class Meta:
        model = Ijtimoiy_tarmoq_url
        fields = '__all__'

class Haqida_toliqSerializer(ModelSerializer):
    class Meta:
        model = Haqida_toliq
        fields = '__all__'

class Faoliyat_joySerializer(ModelSerializer):
    class Meta:
        model = Faoliyat_joy
        fields = '__all__'


class HamkorSerializer(ModelSerializer):
    class Meta:
        model = Hamkor
        fields = '__all__'

