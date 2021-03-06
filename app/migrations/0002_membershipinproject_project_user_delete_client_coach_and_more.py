# Generated by Django 4.0.1 on 2022-02-07 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembershipInProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_allocated_by_member', models.IntegerField(verbose_name='Temps alloué par le membre')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50, verbose_name='Titre du projet')),
                ('project_duration', models.IntegerField(default=0, verbose_name='Durée Estimée')),
                ('time_allocated', models.IntegerField(verbose_name='Temps Alloué')),
                ('needs', models.TextField(max_length=250, verbose_name='Besoins')),
                ('description', models.TextField(max_length=250)),
                ('isValid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Prénom')),
                ('last_name', models.CharField(max_length=30, verbose_name='Nom')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.user')),
            ],
            bases=('app.user',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.user')),
            ],
            bases=('app.user',),
        ),
        migrations.AddField(
            model_name='membershipinproject',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.project'),
        ),
        migrations.AddField(
            model_name='project',
            name='creator',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='project_owner', to='app.student'),
        ),
        migrations.AddField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='Les_Membres', through='app.MembershipInProject', to='app.Student'),
        ),
        migrations.AddField(
            model_name='project',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_coach', to='app.coach'),
        ),
        migrations.AddField(
            model_name='membershipinproject',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student'),
        ),
        migrations.AlterUniqueTogether(
            name='membershipinproject',
            unique_together={('project', 'student')},
        ),
    ]
