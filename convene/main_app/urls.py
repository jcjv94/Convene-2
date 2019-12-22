from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import render


def logout_view(request):
    logout(request)
    return render(request, 'index.html')


urlpatterns = [
    path('', views.landing, name='landing'),
    path('events/', views.events_index, name='index'),
    path('events/<str:event_category>', views.category_index, name='category_index'),
    path('events/<int:event_id>/', views.events_detail, name='events_detail'),
    path('events/<int:event_id>/add_comment', views.events_comment, name='events_comment'),
    path('events/create/', views.EventCreate.as_view(), name='events_create'),
    path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='events_update'),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='events_delete'),
    path('events/<int:event_id>/add_photo/', views.add_photo, name='add_photo'),
    path('events/<int:event_id>/upload_photo/', views.upload_photo, name='upload_photo'),
    path('events/', views.events, name='events'),
    path('user/', views.user, name='user'),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', logout_view, name='logout'),
    path('accounts/signup', views.signup, name='signup'),
]

