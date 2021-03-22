from django.contrib import admin
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = '__all__'


# class PostAdmin(admin.ModelAdmin):
#     form = ArticleAdminForm


class AboutUsAdminForm(forms.ModelForm):
    about_us_content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = AboutUs
        fields = '__all__'


class PostAdminSecond(admin.ModelAdmin):
    form = AboutUsAdminForm


# admin.site.register(Article, PostAdmin)
admin.site.register(AboutUs, PostAdminSecond)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(SubCategory)
admin.site.register(Video)


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('subscriber_name', 'subscriber_email')


class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 5


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'short_desc', 'category', 'ratings', 'publication')
    form = ArticleAdminForm
    readonly_fields = ('publication',)
    inlines = [GalleryInline]
