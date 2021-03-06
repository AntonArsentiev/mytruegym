# Generated by Django 3.1.1 on 2020-09-21 19:06

import django.core.validators
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=20, verbose_name='Название')),
                ('title_en', models.CharField(default='', max_length=20, verbose_name='Title')),
                ('avatar', models.ImageField(upload_to='', verbose_name='Фотография')),
                ('kcal', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000)], verbose_name='Ккал')),
                ('protein', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000)], verbose_name='Белки')),
                ('oil', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000)], verbose_name='Жиры')),
                ('carb', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000)], verbose_name='Углеводы')),
            ],
            options={
                'verbose_name': 'Калория',
                'verbose_name_plural': 'Калории',
                'ordering': ['kcal'],
            },
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddIndex(
            model_name='calorie',
            index=models.Index(fields=['title_en', 'kcal', 'protein', 'oil', 'carb'], name='calories_ca_title_e_42012e_idx'),
        ),
        migrations.AddIndex(
            model_name='calorie',
            index=models.Index(fields=['title', 'kcal', 'protein', 'oil', 'carb'], name='calories_ca_title_2bda5f_idx'),
        ),
    ]
