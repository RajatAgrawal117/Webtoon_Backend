from django.urls import path
from . import views

urlpatterns = [
    path('webtoons/', views.get_all_webtoons, name='get_all_webtoons'),  # GET for all webtoons
    path('webtoons/<int:webtoon_id>/', views.get_webtoon_by_id, name='get_webtoon_by_id'),  # GET by ID
    path('webtoons/add/', views.add_webtoon, name='add_webtoon'),  # POST for new webtoon
    path('webtoons/delete/<int:webtoon_id>/', views.delete_webtoon, name='delete_webtoon'),  # DELETE by ID
]
