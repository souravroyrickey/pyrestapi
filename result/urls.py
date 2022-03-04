from django.urls import path
from . import views

urlpatterns = [
    path('', views.ResultView.as_view(), name='results'),
    path('result/<int:rollnum>/', views.ResultDetailView.as_view(), name='roll_number'),
    path('searchresult/<int:rollnum>/', views.ResultSearchView.as_view(), name='search_result'),
    path('updategrade/<int:rollnum>/', views.UpdateGradeView.as_view(), name='update_grade'),
]