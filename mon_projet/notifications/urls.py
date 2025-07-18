from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('api/notifications/', views.get_notifications, name='get_notifications'),
    path('api/notifications/unread/', views.get_unread_notifications, name='get_unread_notifications'),
    path('api/notifications/<int:notification_id>/read/', views.mark_notification_read, name='mark_notification_read'),
    path('api/notifications/mark-all-read/', views.mark_all_read, name='mark_all_read'),
    path('api/notifications/create/', views.create_notification, name='create_notification'),
    path('api/notifications/<int:notification_id>/delete/', views.delete_notification, name='delete_notification'),
]