# Generated by Django 2.0.13 on 2019-09-09 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-created_at'], 'verbose_name': '상품 리뷰', 'verbose_name_plural': '상품 리뷰'},
        ),
    ]