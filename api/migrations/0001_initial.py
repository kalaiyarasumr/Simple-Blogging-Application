from datetime import datetime
from django.db import migrations, models
from django.utils import timezone

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # Add any migration dependencies here
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),  # Corrected parentheses
                ('content', models.TextField()),  # Corrected parentheses
                ('date_posted', models.DateField(default=timezone.make_aware(datetime(2022, 3, 24, 3, 35, 58)))),
                ('category', models.CharField(choices=[('Web-dev', 'Web-dev'), ('Machine Learning', 'Machine Learning')], default='Web-dev', max_length=160, null=True)),
            ],
        ),
    ]
