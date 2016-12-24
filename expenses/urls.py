from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.CreateExpense.as_view(), name='homepage'),
    url(r'create/', views.CreateExpense.as_view(), name='create'),
    url(r'read/', views.GetExpense.as_view(), name='read'),
    url(r'update/', views.UpdateExpense.as_view(), name='update'),
    url(r'delete/', views.DeleteExpense.as_view(), name='delete'),
]
