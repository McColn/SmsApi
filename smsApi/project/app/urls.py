# urls.py
from django.urls import path, include


from rest_framework import routers
from .views import SMSViewSet


router = routers.DefaultRouter()
router.register(r'sms', SMSViewSet)

urlpatterns = [
    # Your other URL patterns
    path('api/', include(router.urls)),
]

# urlpatterns = [
#     # Your other URL patterns
#     path('api/', SmsDetail.as_view(), name='api'),
# ]

