from django.db import models


class Contacts(models.Model):

    fbid = models.TextField(max_length=64)
    first_name = models.TextField()
    last_name = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Messages(models.Model):

    user = models.ForeignKey(Contacts,on_delete=models.CASCADE)
    message = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.user, self.message)

