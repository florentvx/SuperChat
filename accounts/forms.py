from django.forms import ModelForm
from .models import Chat, Message

class ChatForm(ModelForm):
    def __init__(self, chatter, *args, **kwargs):
        self.NewChat = Chat()
        if chatter != None:
            self.NewChat.SetInitials(chatter)
        super(ChatForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Chat
        fields = ['Name','Description','Tags']

    def save(self, commit = True):
        self.NewChat.Name = self.cleaned_data['Name']
        self.NewChat.Description = self.cleaned_data['Description']
        if commit:
            self.NewChat.save()
            self.NewChat.Tags.set(self.cleaned_data["Tags"])
        return self.NewChat

class MessageForm(ModelForm):
    def __init__(self, chat, *args, **kwargs):
        self.NewMsg = Message()
        self.NewMsg.Chat = chat
        super(MessageForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Message
        fields=['Author','Content','Category']

    def save(self, commit = True):
        self.NewMsg.Author = self.cleaned_data['Author']
        self.NewMsg.Content = self.cleaned_data['Content']
        self.NewMsg.Category = self.cleaned_data['Category']
        if commit:
            self.NewMsg.save()
        return self.NewMsg