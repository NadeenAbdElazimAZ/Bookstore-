# Generated by Django 5.0.3 on 2024-03-16 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_alter_book_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(null=True, upload_to='booksimg/images/'),
        ),
    ]
