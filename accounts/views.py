import datetime
from django.shortcuts import render, redirect

# Create your views here.
from .models import *
from .forms import ChatForm, MessageForm
from.filters import ChatFilter

def home(request):
    chatters = Chatter.objects.all()
    chats = Chat.objects.all()

    total_chatters = chatters.count()
    total_chats = chats.filter(Status='Active').count()

    #chat_filter = ChatFilter(request.GET, queryset=chats)
    #chats = chat_filter.qs

    if request.method == "GET":
        name = request.GET.get('name', "")
        from_date = request.GET.get('from_date', "")
        if from_date == "":
            from_date = datetime.date(2000,1,1)
        to_date = request.GET.get('to_date', "")
        if to_date == "":
            to_date = datetime.date(3000,1,1)
        chats = Chat.objects.filter(DateCreated__gte=from_date)\
                            .filter(DateCreated__lte=to_date)\
                            .filter(Name__icontains=name)

    context = {'chatters': chatters,
               'chats': chats,
               'total_chatters': total_chatters,
               'total_chats': total_chats,
               }

    return render(request,
                  'accounts/dashboard.html',
                  context)


def chat(request, pk):
    chat_obj = Chat.objects.get(id=pk)
    messages = Message.objects.filter(Chat=chat_obj).order_by('-DateCreated')
    msgForm = MessageForm(chat_obj)
    context = {'chat': chat_obj,
               'messages': messages,
               'message_form': msgForm}
    if request.method == "POST":
        msgForm = MessageForm(chat_obj, request.POST)
        if msgForm.is_valid():
            msgForm.save()
            #print("VALID & SAVED")
            #return redirect(f'chat/{pk}')
    return render(request, 'accounts/chat.html', context)


def chatter(request, pk):
    chatter_obj = Chatter.objects.get(id=pk)
    chatter_chats = Chat.objects.filter(Host=chatter_obj)
    context = {
        'chatter': chatter_obj,
        'chats': chatter_chats,
    }
    return render(request, 'accounts/chatter.html', context)


def create_chat(request, pk):
    host = Chatter.objects.get(id=pk)
    form = ChatForm(host)
    if request.method == "POST":
        form = ChatForm(host, request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        context = {'form': form}
        return render(request, 'accounts/chat_form.html', context)


def update_chat(request, pk):
    chat_obj = Chat.objects.get(id=pk)
    if request.method == 'POST':
        form = ChatForm(None, request.POST, instance=chat_obj)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ChatForm(None, instance=chat_obj)
        context = {'form': form}
        return render(request, 'accounts/chat_form.html', context)


def delete_chat(request, pk):
    chat_obj = Chat.objects.get(id=pk)
    if request.method == 'POST':
        chat_obj.delete()
        return redirect('/')
    context = {'item': chat_obj}
    return render(request, 'accounts/delete_chat.html', context)
