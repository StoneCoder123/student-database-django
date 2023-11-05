# Generated by Django 4.2.7 on 2023-11-05 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Record",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("rollno", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=50)),
                ("phone", models.CharField(max_length=50)),
                ("CPI", models.DecimalField(decimal_places=2, max_digits=10)),
                ("CSE_205", models.DecimalField(decimal_places=0, max_digits=10)),
                ("ME_102", models.DecimalField(decimal_places=0, max_digits=10)),
                ("CSO_204", models.DecimalField(decimal_places=0, max_digits=10)),
                ("CSO_211", models.DecimalField(decimal_places=0, max_digits=10)),
                ("DOS", models.DecimalField(decimal_places=0, max_digits=10)),
                ("MA_202", models.DecimalField(decimal_places=0, max_digits=10)),
            ],
        ),
    ]
