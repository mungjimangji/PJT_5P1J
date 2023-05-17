# Generated by Django 3.2.18 on 2023-05-17 00:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='report',
            field=models.BooleanField(default=False, verbose_name='신고'),
        ),
        migrations.AddField(
            model_name='commentreport',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='report',
            field=models.BooleanField(default=False, verbose_name='신고'),
        ),
        migrations.AddField(
            model_name='reviewreport',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='AdminMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300)),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentreports', to='movies.comment')),
                ('review', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewreports', to='movies.review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]