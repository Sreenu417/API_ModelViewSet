# Generated by Django 4.2.2 on 2023-06-13 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product_Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pc_id", models.PositiveIntegerField()),
                ("pc_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pid", models.PositiveIntegerField()),
                ("pname", models.CharField(max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                ("date", models.DateField()),
                (
                    "pc_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.product_category",
                    ),
                ),
            ],
        ),
    ]
