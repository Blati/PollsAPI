from django.contrib import admin
from .models import Poll, Choice, Vote, PollMain

# Register your models here.

admin.site.register(PollMain)
admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Vote)
