from django.contrib import admin
from django.db import models
from blog.models import Category, Comment, Post, BlogColor
from markdownx.admin import MarkdownxModelAdmin
from mdeditor.widgets import MDEditorWidget


class CategoryAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {"widget": MDEditorWidget}}


class CommentAdmin(admin.ModelAdmin):
    pass


class BlogColorAdmin(admin.ModelAdmin):
    list_display = ["theme_name", "app"]

    # アクションバーの設定
    actions = ["make_app", "no_app"]

    # 公開用のカスタムメソッド
    def make_app(self, request, queryset):
        queryset.update(app=True)

    make_app.short_description = "公開する"

    # 非公開用のカスタムメソッド
    def no_app(self, request, queryset):
        queryset.update(app=False)

    no_app.short_description = "公開しない"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(BlogColor, BlogColorAdmin)
