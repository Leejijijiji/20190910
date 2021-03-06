# Generated by Django 2.0.13 on 2019-08-28 04:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성된 시간')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정된 시간')),
                ('name', models.CharField(max_length=200, verbose_name='상품명')),
                ('description', models.TextField(verbose_name='상품설명')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='대표이미지')),
            ],
            options={
                'verbose_name': '상품',
                'verbose_name_plural': '상품',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성된 시간')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정된 시간')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Item', verbose_name='상품')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='구매자')),
            ],
            options={
                'verbose_name': '상품 좋아요',
                'verbose_name_plural': '상품 좋아요',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='like_users', through='items.Like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('user', 'item')},
        ),
    ]
