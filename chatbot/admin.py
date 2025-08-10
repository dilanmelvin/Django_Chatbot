from django.contrib import admin
from .models import ChatMessage


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'user_message_short', 'bot_response_short']
    list_filter = ['created_at']
    search_fields = ['user_message', 'bot_response']
    readonly_fields = ['created_at']
    
    def user_message_short(self, obj):
        return obj.user_message[:50] + '...' if len(obj.user_message) > 50 else obj.user_message
    user_message_short.short_description = 'User Message'
    
    def bot_response_short(self, obj):
        return obj.bot_response[:50] + '...' if len(obj.bot_response) > 50 else obj.bot_response
    bot_response_short.short_description = 'Bot Response'
