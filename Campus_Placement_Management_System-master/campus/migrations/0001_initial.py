# Generated by Django 2.2.6 on 2021-03-12 08:27

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import multiselectfield.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achieve_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('student_name', models.CharField(max_length=100)),
                ('certificate_name', models.CharField(blank=True, max_length=100)),
                ('field_type', models.CharField(max_length=100)),
                ('issuer_name', models.CharField(blank=True, max_length=100)),
                ('certificate_img', models.FileField(upload_to='achievements/')),
                ('college_name', models.CharField(default='BVM', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('index_no', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(default='BVM', max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('email_id', models.CharField(max_length=100)),
                ('helpline_no', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comapnies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('company_name', models.CharField(max_length=100)),
                ('field_name', models.CharField(max_length=100)),
                ('email_id', models.CharField(max_length=100)),
                ('coming_date', models.DateField()),
                ('job_description', models.CharField(max_length=255)),
                ('college_name', models.CharField(default='BVM', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('college_name', models.CharField(default='BVM', max_length=100)),
                ('dept_name', models.CharField(max_length=100)),
                ('dept_hod', models.CharField(max_length=100)),
                ('no_of_faculty', models.CharField(max_length=10)),
                ('est_year', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('event_name', models.CharField(max_length=200)),
                ('facultyy_name', models.CharField(max_length=200)),
                ('depart_name', models.CharField(max_length=200)),
                ('college_name', models.CharField(default='BVM', max_length=100)),
                ('event_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Exams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('subject_id', models.CharField(max_length=200)),
                ('stud_name', models.CharField(max_length=200)),
                ('exam_type', models.CharField(choices=[('Mid', 'Mid'), ('External', 'External')], max_length=10)),
                ('obtain_marks', models.CharField(max_length=10)),
                ('total_marks', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Faculties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100, null=True)),
                ('lname', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=1, null=True)),
                ('dob', models.DateField(default=datetime.datetime(2021, 3, 12, 13, 57, 38, 122819))),
                ('email', models.EmailField(max_length=254, null=True)),
                ('mobile', models.CharField(max_length=12, null=True)),
                ('dept', models.CharField(choices=[('Mechanical', 'Mechanical'), ('EC', 'EC'), ('Civil', 'Civil'), ('IT', 'IT'), ('EL', 'EL'), ('EE', 'EE'), ('Production', 'Production')], max_length=1, null=True)),
                ('id_no', models.CharField(max_length=10, null=True)),
                ('desg', models.CharField(max_length=100)),
                ('permanent_address', models.CharField(max_length=256, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('resident_address', models.CharField(max_length=100, null=True)),
                ('pincode', models.CharField(max_length=6, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('B_E_college_name', models.CharField(max_length=100, null=True)),
                ('B_E_college_result', models.FileField(null=True, upload_to='')),
                ('M_E_college_name', models.CharField(max_length=100, null=True)),
                ('M_E_college_result', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_interest', models.CharField(choices=[('wd', 'Web Development'), ('ad', 'App Development'), ('cd', 'Cloud Computing'), ('excel', 'Excel'), ('wp', 'Wordpress'), ('react', 'React'), ('dj', 'Django'), ('bc', 'Block Chain'), ('dm', 'Data Mining'), ('py', 'Python'), ('c', 'C/C++'), ('j', 'Java')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('student_id', models.CharField(max_length=100)),
                ('project_name', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('url', models.URLField(blank=True, max_length=100)),
                ('rating_star', models.CharField(max_length=3)),
                ('college_name', models.CharField(default='BVM', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_skills', models.CharField(choices=[('wd', 'Web Development'), ('ad', 'App Development'), ('cd', 'Cloud Computing'), ('excel', 'Excel'), ('wp', 'Wordpress'), ('react', 'React'), ('dj', 'Django'), ('bc', 'Block Chain'), ('dm', 'Data Mining'), ('py', 'Python'), ('c', 'C/C++'), ('j', 'Java')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100, null=True)),
                ('lname', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6, null=True)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254, null=True)),
                ('mobile', models.CharField(max_length=12, null=True)),
                ('dept', models.CharField(choices=[('Mechanical', 'Mechanical'), ('EC', 'EC'), ('Civil', 'Civil'), ('IT', 'IT'), ('EL', 'EL'), ('EE', 'EE'), ('Production', 'Production')], max_length=10, null=True)),
                ('enrollment', models.CharField(max_length=20, null=True)),
                ('id_no', models.CharField(max_length=10, null=True)),
                ('permanent_address', models.CharField(max_length=256, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('resident_address', models.CharField(max_length=100, null=True)),
                ('pincode', models.CharField(max_length=6, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('ssc', models.CharField(max_length=100, null=True)),
                ('ssc_result', models.FileField(null=True, upload_to='')),
                ('hsc', models.CharField(max_length=100, null=True)),
                ('hsc_result', models.FileField(null=True, upload_to='')),
                ('skills', multiselectfield.db.fields.MultiSelectField(choices=[('wd', 'Web Development'), ('ad', 'App Development'), ('cd', 'Cloud Computing'), ('excel', 'Excel'), ('wp', 'Wordpress'), ('react', 'React'), ('dj', 'Django'), ('bc', 'Block Chain'), ('dm', 'Data Mining'), ('py', 'Python'), ('c', 'C/C++'), ('j', 'Java')], max_length=39, null=True)),
                ('interest', multiselectfield.db.fields.MultiSelectField(choices=[('wd', 'Web Development'), ('ad', 'App Development'), ('cd', 'Cloud Computing'), ('excel', 'Excel'), ('wp', 'Wordpress'), ('react', 'React'), ('dj', 'Django'), ('bc', 'Block Chain'), ('dm', 'Data Mining'), ('py', 'Python'), ('c', 'C/C++'), ('j', 'Java')], max_length=39, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('subject_name', models.CharField(max_length=100)),
                ('semester', models.CharField(max_length=3)),
                ('teach_year', models.CharField(max_length=5)),
                ('faculty_id', models.CharField(max_length=100)),
                ('dept_id', models.CharField(max_length=100)),
                ('college_name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('semester', models.CharField(max_length=3)),
                ('year', models.CharField(max_length=5)),
                ('time', models.CharField(max_length=100)),
                ('faculty_name', models.CharField(max_length=100)),
                ('lab_lec', models.CharField(max_length=1)),
                ('subject_name', models.CharField(max_length=20)),
                ('batch_id', models.CharField(max_length=5)),
                ('college_name', models.CharField(default='BVM', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_student', models.BooleanField(default=False)),
                ('is_faculty', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('email', models.CharField(max_length=100)),
                ('is_pass_change', models.BooleanField(default=False)),
                ('slug', models.SlugField(default=uuid.uuid1, unique=True)),
                ('college_name', models.CharField(default='BVM', max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
