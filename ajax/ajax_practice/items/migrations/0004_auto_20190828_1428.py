# Generated by Django 2.0.13 on 2019-08-28 05:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0003_item_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='like_users',
        ),
        migrations.AddField(
            model_name='item',
            name='liked_users',
            field=models.ManyToManyField(blank=True, related_name='liked_users', through='items.Like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='image/', verbose_name='상품이미지'),
        ),
    ]
