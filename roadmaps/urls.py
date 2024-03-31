from django.urls import path

from . import views

urlpatterns = [
    path('', views.create_skill),
    path('search', views.search_skill),
    path('topic', views.get_topic_text),
    path('skill/<skill_id>', views.detail_view),
]
