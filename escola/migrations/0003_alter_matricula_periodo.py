# Generated by Django 5.0.3 on 2024-03-19 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matricula',
            name='periodo',
            field=models.CharField(choices=[('M', 'Matutino'), ('V', 'Vespertino'), ('N', 'Noturno')], default='M', max_length=1),
        ),
    ]
