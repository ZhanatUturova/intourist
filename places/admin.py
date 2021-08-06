from django.contrib import admin
from .models import Place, Feedback

# Register your models here.
admin.site.register(Place)

class FeedbackAdmin(admin.ModelAdmin):
    # работа над списком элементов
    list_display = ['text', 'place', 'user', 'checked']
    list_editable = ['checked']

    list_filter = ['checked']       # фильтрация

    search_fields = ['text', 'place__name', 'place__location', 'place__description']        # поиск


    # работа над одним элементом
    fields = ['user', 'place', 'text']
    readonly_fields = ['place', 'text']

admin.site.register(Feedback, FeedbackAdmin)