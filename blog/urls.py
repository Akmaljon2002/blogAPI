from django.contrib import admin
from django.urls import path, include
from asosiy.views import *
from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version='v1',
      description="Shaxsiy blog uchun API",
      license=openapi.License(name="Akmaljon"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


router = DefaultRouter()
router.register('murojaat', MurojaatViewSet),
router.register('menu', MenuViewSet),
router.register('home', Home_pageViewSet),
router.register('video', VideoViewSet),
router.register('ijtimoiy-tarmoq', Ijtimoiy_tarmoqViewSet),
router.register('haqida', Haqida_toliqViewSet),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('maqolalar/', MaqolalarAPIView.as_view()),
    path('maqolalar-top/', MaqolalarTopAPIView.as_view()),
    path('maqolalar-bosh-menu/', Bosh_menu_MaqolalariAPIView.as_view()),
    path('faoliyatlar/', FaoliyatAPIView.as_view()),
    path('hamkorlar/', HamkorAPIView.as_view()),
    path('maqola/<int:pk>/', MaqolaDetailAPIView.as_view()),
    path('', include(router.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
