from django.db import models

# Create your models here.


class Chatter(models.Model):
    Name = models.CharField(max_length=200, null=True)
    Email = models.CharField(max_length=200, null=True)
    DateCreated = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Chat(models.Model):

    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )

    Host = models.ForeignKey(Chatter, null=True, on_delete=models.SET_NULL)
    Name = models.CharField(max_length=200, null=True)
    Description = models.CharField(max_length=200, null=True)
    DateCreated = models.DateTimeField(auto_now_add=True, null=True, max_length=10)
    Donations = models.FloatField(null=True)
    Status = models.CharField(max_length=200, null=True, choices=STATUS)
    Tags = models.ManyToManyField(Tag)

    def SetInitials(self, chatter):
        self.Host = chatter
        self.Donations = 0
        self.Status = 'Active'

    def __str__(self):
        return self.Name


class Message(models.Model):

    CATEGORY = (
        ('Common', 'Common'),
        ('Bronze', 'Bronze'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold')
    )

    Chat = models.ForeignKey(Chat, null=True, on_delete=models.SET_NULL)
    Author = models.ForeignKey(Chatter, null=True, on_delete=models.SET_NULL)
    Content = models.CharField(max_length=200, null=True)
    DateCreated = models.DateTimeField(auto_now_add=True, null=True)
    Category = models.CharField(max_length=200, null=True, choices=CATEGORY)

    @property
    def PrintMessage(self):
        date = self.DateCreated.time().strftime("%H:%M:%S")
        return "[{}] - {} : {}".format(date, self.Author, self.Content)

    def __str__(self):
        content = str(self.Content)
        if len(content) > 10:
            content = self.Content[:10] + "..."
        return "{} ({}) ".format(content, str(self.Author))
