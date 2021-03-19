from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Message(models.Model):
	author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
	content = models.TextField(null=False, blank=False)
	timestamp = models.DateTimeField(auto_now_add=True)
	room = models.CharField(max_length=100)

	def __str__(self):
		return self.author.username

	def last_30_messages(chatconsumer):
		return Message.objects.filter(room=chatconsumer.room_name).order_by('-timestamp').all()[:30]