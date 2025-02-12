# Generated by Django 5.1.2 on 2024-10-15 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_section_background_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='image',
            new_name='images',
        ),
        migrations.AddField(
            model_name='page',
            name='card_image',
            field=models.ImageField(null=True, upload_to='pages/'),
        ),
        migrations.AlterField(
            model_name='section',
            name='section',
            field=models.CharField(choices=[('projects', 'Projekte'), ('features', 'Features'), ('about', 'Über Uns'), ('contact', 'Kontakt')], max_length=10, unique=True),
        ),
    ]
