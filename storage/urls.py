from django.urls import path, include
from .views import LinkList, LinkDetail
urlpatterns = [
   path('', LinkList.as_view(), name='linkcreate'),
   path('<int:pk>/', LinkDetail.as_view(), name='linkdetail')
]