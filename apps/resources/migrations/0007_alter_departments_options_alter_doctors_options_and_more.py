# Generated by Django 4.2.4 on 2023-09-04 18:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("resources", "0006_doctors_appointments"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="departments",
            options={"verbose_name_plural": "Departments"},
        ),
        migrations.AlterModelOptions(
            name="doctors",
            options={"verbose_name_plural": "Doctors"},
        ),
        migrations.AlterModelOptions(
            name="resources",
            options={"verbose_name_plural": "Resources"},
        ),
    ]