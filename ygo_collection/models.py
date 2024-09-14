
from django.db import models

import ygo_collection.card_field_constants as c

class Card(models.Model):
    name = models.CharField(max_length=80)
    quantity = models.IntegerField(default=0)
    quantity_sd = models.IntegerField(default=0)
    in_decks = models.IntegerField(default=0)
    in_decks_sd = models.IntegerField(default=0)
    in_bulk = models.IntegerField(default=0)
    card_code = models.CharField(max_length=10)
    set = models.CharField(max_length=4)
    language = models.CharField(max_length=2, default='EN')
    set_number = models.IntegerField(default=0)
    card_type = models.CharField(max_length=7, choices=c.CARD_TYPES)
    card_subtype = models.CharField(max_length=10, choices=c.CARD_SUBTYPES, default="None")
    is_pendulum = models.BooleanField(default=False)
    property = models.CharField(max_length=10, choices=c.CARD_PROPERTIES)
    attribute = models.CharField(max_length=6, choices=c.CARD_ATTRIBUTES, default="None")
    types = models.CharField(max_length=255)
    effect_type = models.CharField(max_length=25, choices=c.CARD_EFFECT_TYPES, default="None")  
    level = models.IntegerField(choices=c.CARD_LEVELS, default=0)
    attack = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    passcode = models.IntegerField(default=0)
    effect = models.TextField()
    pendulum_effect = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
