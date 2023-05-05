from django.contrib import admin
from .models import EmailSend
# Register your models here.


@admin.register(EmailSend)
class EmailSendAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'subject', 'message']
