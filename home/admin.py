# home/admin.py
from django.contrib import admin
from .models import News
from .models import ContactMessage

admin.site.register(News)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at')

