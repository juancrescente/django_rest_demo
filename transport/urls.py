from django.urls import path

from . import views

urlpatterns = [
    path('provider/', views.ProviderListCreate.as_view()),
    path('provider/<int:pk>/', views.ProviderDetail.as_view()),
    path('servicearea/', views.ServiceAreaList.as_view()),
    path('servicearea/<int:pk>/', views.ServiceAreaDetail.as_view()),
    path('query/', views.ServiceAreaQuery.as_view()),
]
