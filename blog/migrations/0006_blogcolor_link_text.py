# Generated by Django 5.0.4 on 2024-04-27 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_blogcolor_body_color_remove_blogcolor_footer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcolor',
            name='link_text',
            field=models.CharField(default='blue', max_length=50, verbose_name='リンクテキスト'),
        ),
    ]