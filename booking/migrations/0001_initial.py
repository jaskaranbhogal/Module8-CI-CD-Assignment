from django.core.validators import MinValueValidator
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Room",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("building", models.CharField(max_length=100)),
                ("capacity", models.PositiveIntegerField(validators=[MinValueValidator(1)])),
                ("is_available", models.BooleanField(default=True)),
            ],
        ),
    ]
