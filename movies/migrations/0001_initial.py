# Generated by Django 3.2.18 on 2023-05-18 17:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('spoiler', models.BooleanField(default=False, verbose_name='스포일러')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('report', models.BooleanField(default=False, verbose_name='신고')),
                ('like_users', models.ManyToManyField(related_name='like_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.CharField(default='', max_length=100)),
                ('title', models.CharField(max_length=20)),
                ('tags', models.CharField(default='태그', max_length=10000)),
                ('description', models.CharField(max_length=300)),
                ('platform', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('poster_path', models.CharField(default='', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('want_users', models.ManyToManyField(related_name='want_posts', to=settings.AUTH_USER_MODEL)),
                ('watching_users', models.ManyToManyField(related_name='watching_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('rating', models.PositiveBigIntegerField(default=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('tags', models.CharField(default='태그', max_length=100000)),
                ('spoiler', models.BooleanField(default=False, verbose_name='스포일러')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('report', models.BooleanField(default=False, verbose_name='신고')),
                ('like_users', models.ManyToManyField(related_name='like_reviews', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('스팸', '스팸'), ('스포일러', '스포일러'), ('해로운 허위 정보 및 폭력 미화', '해로운 허위 정보 및 폭력 미화'), ('신원 파악이 가능한 개인정보 노출', '신원 파악이 가능한 개인정보 노출'), ('기타', '기타')], max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_report', to='movies.review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('스팸', '스팸'), ('스포일러', '스포일러'), ('해로운 허위 정보 및 폭력 미화', '해로운 허위 정보 및 폭력 미화'), ('신원 파악이 가능한 개인정보 노출', '신원 파악이 가능한 개인정보 노출'), ('기타', '기타')], max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_report', to='movies.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movies.review'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
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
