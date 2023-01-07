# Generated by Django 3.1.1 on 2020-09-24 19:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_bid_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlistening',
            name='favoured',
            field=models.ManyToManyField(related_name='user_favoured', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Favorites',
        ),
    ]
