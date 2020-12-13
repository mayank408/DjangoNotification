from django.shortcuts import render

# Create your views here.


# Basic home view
def home(request):

    my_context = {
        "grp" : request.GET.get('grp', '')
    }

    return render(request, 'django_notifications_app/home.html', my_context)


from datetime import datetime

# Django Channels
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def notification_test_page(request):

    # # Django Channels Notifications Test
    # grp = request.GET.get('grp', '')
    # print(grp , type(grp))
    # current_user = request.user
    # channel_layer = get_channel_layer()
    # data = "notification"+ "...." + str(datetime.now())
    # # Trigger message sent to group

    my_context = {
        "grp" : request.GET.get('grp', ''),
        "data" : "notification"+ "...." + str(datetime.now())
    }
    
    # async_to_sync(channel_layer.group_send)(
    #     grp,  # Channel Name, Should always be string
    #     {
    #         "type": "notify",   # Custom Function written in the consumers.py
    #         "text": data,
    #     },
    # )  


    
    return render(request, 'django_notifications_app/notifications_test_page.html', my_context)