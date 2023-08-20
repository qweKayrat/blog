from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.utils.safestring import mark_safe


class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Blog
        fields = '__all__'


class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    prepopulated_fields = {"slug": ("title",)}
    # автоматическое добавление slug по title на стороне admin

    list_display = ("id", "title", 'time_created', 'time_updated', 'get_html_photo', 'is_published')
    # вывод полей в admin

    list_display_links = ('id', 'title',)
    # ссылки для редактировния в admin

    search_fields = ('title', 'content')
    # поиск по полям в admin

    readonly_fields = ('time_created', 'time_updated')
    # отображение полей в admin без возможности редактирования

    list_editable = ('is_published',)
    # редактирование полей со стороны admin панели

    list_filter = ('is_published', 'time_created',)
    # фильтрация полей в admin панели

    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'time_created', 'time_updated')
    readonly_fields = ('get_html_photo', 'time_created', 'time_updated')
    save_on_top = True

    def get_html_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="70p">')

    get_html_photo.short_description = "Миниатюра"


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
