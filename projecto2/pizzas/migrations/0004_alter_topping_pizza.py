# Generated by Django 4.1.1 on 2022-09-27 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0003_alter_topping_pizza'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topping',
            name='pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pizzas.pizza'),
        ),
    ]
