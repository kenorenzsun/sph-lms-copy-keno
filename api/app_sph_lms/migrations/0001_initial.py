# Generated by Django 4.1.7 on 2023-03-31 07:23

import app_sph_lms.models
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(2)])),
                ('last_name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(2)])),
                ('is_active', models.BooleanField(default=1)),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, validators=[django.core.validators.MinLengthValidator(5)])),
                ('img_path', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'User',
                'db_table': 'app_sph_lms_users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(3)])),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Category',
                'db_table': 'app_sph_lms_categories',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(3)])),
                ('email', models.EmailField(max_length=255, validators=[django.core.validators.MinLengthValidator(5)])),
                ('description', models.TextField(max_length=65000, null=True, validators=[django.core.validators.MinLengthValidator(5)])),
                ('address', models.CharField(max_length=255, null=True, validators=[django.core.validators.MinLengthValidator(5)])),
                ('city', models.CharField(max_length=255, null=True, validators=[django.core.validators.MinLengthValidator(5)])),
                ('state', models.CharField(max_length=255, null=True, validators=[django.core.validators.MinLengthValidator(5)])),
                ('postal_code', models.CharField(max_length=255, null=True, validators=[django.core.validators.MinLengthValidator(5)])),
                ('country', models.CharField(max_length=255, null=True, validators=[django.core.validators.MinLengthValidator(5)])),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Company',
                'db_table': 'app_sph_lms_companies',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, validators=[django.core.validators.MinLengthValidator(5)])),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Status',
                'db_table': 'app_sph_lms_statuses',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(3)])),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tag',
                'db_table': 'app_sph_lms_tags',
            },
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'UserRole',
                'verbose_name_plural': 'UserRole',
                'db_table': 'app_sph_lms_user_roles',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=app_sph_lms.models.generate_code, max_length=10, unique=True)),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(3)])),
                ('description', models.TextField(max_length=65000, null=True, validators=[django.core.validators.MinLengthValidator(5)])),
                ('img_path', models.CharField(max_length=255, null=True)),
                ('preview_vid_path', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sph_lms.company')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_sph_lms.status')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Course',
                'db_table': 'app_sph_lms_courses',
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=app_sph_lms.models.generate_code, max_length=10, unique=True)),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(3)])),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sph_lms.company')),
            ],
            options={
                'verbose_name': 'Class',
                'verbose_name_plural': 'Class',
                'db_table': 'app_sph_lms_classes',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sph_lms.userrole'),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_sph_lms.status'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('class_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_sph_lms.class')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sph_lms.company')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_sph_lms.status')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Trainer',
                'verbose_name_plural': 'Trainer',
                'db_table': 'app_sph_lms_trainers',
                'unique_together': {('class_id', 'trainer')},
            },
        ),
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('class_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_sph_lms.class')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sph_lms.company')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_sph_lms.status')),
                ('trainee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Trainee',
                'verbose_name_plural': 'Trainee',
                'db_table': 'app_sph_lms_trainees',
                'unique_together': {('class_id', 'trainee')},
            },
        ),
        migrations.CreateModel(
            name='CourseTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sph_lms.course')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sph_lms.tag')),
            ],
            options={
                'verbose_name': 'CourseTag',
                'verbose_name_plural': 'CourseTag',
                'db_table': 'app_sph_lms_course_tags',
                'unique_together': {('course', 'tag')},
            },
        ),
        migrations.CreateModel(
            name='CourseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sph_lms.category')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sph_lms.course')),
            ],
            options={
                'verbose_name': 'CourseCategory',
                'verbose_name_plural': 'CourseCategory',
                'db_table': 'app_sph_lms_course_categories',
                'unique_together': {('course', 'category')},
            },
        ),
    ]
