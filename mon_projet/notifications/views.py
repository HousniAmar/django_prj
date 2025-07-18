from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer

# Create your views here.

def get_notifications_for_request(request):
    """Get notifications for user or session"""
    if request.user.is_authenticated:
        return Notification.objects.filter(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        return Notification.objects.filter(session_key=session_key)

@api_view(['GET'])
def get_notifications(request):
    """Get all notifications for current user/session"""
    notifications = get_notifications_for_request(request)
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_unread_notifications(request):
    """Get unread notifications count and list"""
    notifications = get_notifications_for_request(request).filter(is_read=False)
    serializer = NotificationSerializer(notifications, many=True)
    return Response({
        'count': notifications.count(),
        'notifications': serializer.data
    })

@api_view(['PUT'])
def mark_notification_read(request, notification_id):
    """Mark a specific notification as read"""
    try:
        notifications = get_notifications_for_request(request)
        notification = notifications.get(id=notification_id)
        notification.is_read = True
        notification.save()
        
        serializer = NotificationSerializer(notification)
        return Response(serializer.data)
    except Notification.DoesNotExist:
        return Response({'error': 'Notification not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def mark_all_read(request):
    """Mark all notifications as read"""
    notifications = get_notifications_for_request(request).filter(is_read=False)
    notifications.update(is_read=True)
    
    updated_notifications = get_notifications_for_request(request)
    serializer = NotificationSerializer(updated_notifications, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_notification(request):
    """Create a new notification (for testing purposes)"""
    serializer = NotificationSerializer(data=request.data)
    if serializer.is_valid():
        if request.user.is_authenticated:
            serializer.save(user=request.user)
        else:
            session_key = request.session.session_key
            if not session_key:
                request.session.create()
                session_key = request.session.session_key
            serializer.save(session_key=session_key)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_notification(request, notification_id):
    """Delete a specific notification"""
    try:
        notifications = get_notifications_for_request(request)
        notification = notifications.get(id=notification_id)
        notification.delete()
        return Response({'message': 'Notification deleted successfully'})
    except Notification.DoesNotExist:
        return Response({'error': 'Notification not found'}, status=status.HTTP_404_NOT_FOUND)
