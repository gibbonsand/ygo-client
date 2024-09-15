
from django.db import models

import ygo_collection.card_field_constants as c

class Card(models.Model):
    name = models.CharField(max_length=80)
    quantity = models.IntegerField(default=0)
    quantity_sd = models.IntegerField(default=0)
    in_decks = models.IntegerField(default=0)
    in_decks_sd = models.IntegerField(default=0)
    in_draft = models.IntegerField(default=0)
    card_code = models.CharField(max_length=10, null=True)
    card_set = models.CharField(max_length=4, null=True)
    language = models.CharField(max_length=2, default='EN', null=True)
    set_number = models.IntegerField(default=0, null=True)
    set_rarity = models.CharField(max_length=255, choices=c.CARD_RARITIES, null=True)
    card_frame = models.CharField(max_length=255, choices=c.CARD_FRAMES, null=True)
    card_type = models.CharField(max_length=7, choices=c.CARD_TYPES, null=True)
    card_subtype = models.CharField(max_length=10, choices=c.CARD_SUBTYPES, null=True)
    is_pendulum = models.BooleanField(null=True)
    card_property = models.CharField(max_length=10, choices=c.CARD_PROPERTIES, null=True)
    attribute = models.CharField(max_length=6, choices=c.CARD_ATTRIBUTES, null=True)
    monster_type = models.CharField(max_length=13, choices=c.CARD_MONSTER_TYPES, null=True)
    effect_type = models.CharField(max_length=25, choices=c.CARD_EFFECT_TYPES, null=True)  
    level = models.IntegerField(choices=c.CARD_LEVELS, null=True)
    attack = models.IntegerField(null=True)
    defense = models.IntegerField(null=True)
    passcode = models.IntegerField(null=True)
    effect = models.TextField(null=True)
    pendulum_effect = models.TextField(null=True)
    image = models.ImageField(upload_to='images/', null=True)

    @property
    def in_bulk(self):  
        return self.quantity - self.quantity_sd - self.in_decks - self.in_draft
    
    @property
    def in_bulk_sd(self):
        return self.quantity_sd - self.in_decks_sd
        
    def __str__(self):
        return self.name
