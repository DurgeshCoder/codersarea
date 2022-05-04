from django.contrib import admin
from .models import Topic, Technology, SubTopics

# Register your models here.


admin.site.register(Technology)


@admin.register(SubTopics)
class SubTopicAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_filter = ('technology',)


@admin.register(Topic)
class ExampleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug',)
    list_editable = ('author', 'slug',)
    search_fields = ('title', 'author',)
    list_filter = ('sub_topic',)
    list_per_page = 10

    class Media:
        js = ("tinyInject.js",)
