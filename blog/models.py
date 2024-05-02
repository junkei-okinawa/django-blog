import json
from django.db import models

# from markdownx.models import MarkdownxField
from mdeditor.fields import MDTextField
from django.utils.safestring import mark_safe
from markdownx.utils import markdownify
from emoji import Emoji
from colorfield.fields import ColorField


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = MDTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

    def get_body_markdownx(self):
        return mark_safe(markdownify(Emoji.replace(self.body)))

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.post}'"


class BlogColor(models.Model):
    with open("static/colorfield/colorPalette.json", "r") as f:
        color_palet_json = json.load(f)
    COLOR_PALETTE = [(value, key) for key, value in color_palet_json.items()]

    theme_name = models.CharField("テーマ名", max_length=50)
    body_bg = ColorField(
        "ボディ背景", default=color_palet_json["white"], samples=COLOR_PALETTE
    )
    body_text = ColorField(
        "ボディテキスト",
        default=color_palet_json["black"],
        samples=COLOR_PALETTE,
    )
    title_bg = ColorField(
        "タイトル背景", default=color_palet_json["lightgray"], samples=COLOR_PALETTE
    )
    title_text = ColorField(
        "タイトルテキスト", default=color_palet_json["black"], samples=COLOR_PALETTE
    )
    link_text = ColorField(
        "リンクテキスト", default=color_palet_json["blue"], samples=COLOR_PALETTE
    )
    head_bg = ColorField(
        "ヘッダー背景", default=color_palet_json["lightgray"], samples=COLOR_PALETTE
    )
    head_text = ColorField(
        "ヘッダーテキスト", default=color_palet_json["black"], samples=COLOR_PALETTE
    )
    code_bg = ColorField(
        "コード背景", default=color_palet_json["black"], samples=COLOR_PALETTE
    )
    code_texxt = ColorField(
        "コードテキスト", default="lightgray", samples=COLOR_PALETTE
    )
    app = models.BooleanField(
        "公開する", default=True, help_text="適用する場合はチェック"
    )

    def __str__(self):
        return self.theme_name

    class Meta:
        verbose_name = "カラー設定"
        verbose_name_plural = "カラー設定"
