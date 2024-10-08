# Generated by Django 5.1.1 on 2024-09-15 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ygo_collection', '0004_remove_card_in_bulk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='attack',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='attribute',
            field=models.CharField(choices=[('dark', 'DARK'), ('divine', 'DIVINE'), ('earth', 'EARTH'), ('fire', 'FIRE'), ('light', 'LIGHT'), ('water', 'WATER'), ('wind', 'WIND')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_frame',
            field=models.CharField(choices=[('normal', 'Normal'), ('effect', 'Effect'), ('ritual', 'Ritual'), ('fusion', 'Fusion'), ('synchro', 'Synchro'), ('xyz', 'XYZ'), ('link', 'Link'), ('normal_pendulum', 'Normal Pendulum'), ('effect_pendulum', 'Effect Pendulum'), ('ritual_pendulum', 'Ritual Pendulum'), ('fusion_pendulum', 'Fusion Pendulum'), ('synchro_pendulum', 'Synchro Pendulum'), ('xyz_pendulum', 'XYZ Pendulum'), ('spell', 'Spell'), ('trap', 'Trap'), ('token', 'Token'), ('skill', 'Skill')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_property',
            field=models.CharField(choices=[('continuous', 'Continuous'), ('counter', 'Counter'), ('equip', 'Equip'), ('field', 'Field'), ('normal', 'Normal'), ('quick-play', 'Quick-Play'), ('ritual', 'Ritual')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_set',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_subtype',
            field=models.CharField(choices=[('effect', 'Effect'), ('fusion', 'Fusion'), ('link', 'Link'), ('normal', 'Normal'), ('ritual', 'Ritual'), ('synchro', 'Synchro'), ('xyz', 'Xyz')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_type',
            field=models.CharField(choices=[('monster', 'Monster'), ('other', 'Other'), ('skill', 'Skill'), ('spell', 'Spell'), ('token', 'Token'), ('trap', 'Trap')], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='defense',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='effect',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='effect_type',
            field=models.CharField(choices=[('effect', 'Effect'), ('flip', 'FLIP'), ('gemini', 'Gemini'), ('spirit', 'Spirit')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='card',
            name='is_pendulum',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='language',
            field=models.CharField(default='EN', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='level',
            field=models.IntegerField(choices=[('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10), ('11', 11), ('12', 12)], null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='monster_type',
            field=models.CharField(choices=[('aqua', 'Aqua'), ('beast', 'Beast'), ('beast-warrior', 'Beast-Warrior'), ('creator-god', 'Creator-God'), ('cyberse', 'Cyberse'), ('dinosaur', 'Dinosaur'), ('divine-beast', 'Divine-Beast'), ('dragon', 'Dragon'), ('fairy', 'Fairy'), ('fiend', 'Fiend'), ('fish', 'Fish'), ('illusion', 'Illusion'), ('insect', 'Insect'), ('machine', 'Machine'), ('plant', 'Plant'), ('psychic', 'Psychic'), ('pyro', 'Pyro'), ('reptile', 'Reptile'), ('rock', 'Rock'), ('sea-serpent', 'Sea Serpent'), ('spellcaster', 'Spellcaster'), ('thunder', 'Thunder'), ('warrior', 'Warrior'), ('winged-beast', 'Winged Beast'), ('wyrm', 'Wyrm'), ('zombie', 'Zombie')], max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='passcode',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='pendulum_effect',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='set_number',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='set_rarity',
            field=models.CharField(choices=[('collectors-rare', 'Collectors Rare'), ('common', 'Common'), ('extra-secret-rare', 'Extra Secret Rare'), ('ghost-rare', 'Ghost Rare'), ('gold-rare', 'Gold Rare'), ('gold-secret-rare', 'Gold Secret Rare'), ('holographic-rare', 'Holographic Rare'), ('mozaic-rare', 'Mozaic Rare'), ('oversized', 'Oversized'), ('parallel-rare', 'Parallel Rare'), ('platinum-rare', 'Platinum Rare'), ('platinum-secret-rare', 'Platinum Secret Rare'), ('premium-gold-rare', 'Premium Gold Rare'), ('quarter-century-secret-rare', 'Quarter Century Secret Rare'), ('rare', 'Rare'), ('secret-parallel-rare', 'Secret Parallel Rare'), ('secret-rare', 'Secret Rare'), ('shatterfoil', 'Shatterfoil'), ('special', 'Special'), ('starfoil-rare', 'Starfoil Rare'), ('starlight-rare', 'Starlight Rare'), ('super-parallel-rare', 'Super Parallel Rare'), ('super-rare', 'Super Rare'), ('token', 'Token'), ('ultimate-rare', 'Ultimate Rare'), ('ultra-parallel-rare', 'Ultra Parallel Rare'), ('ultra-rare', 'Ultra Rare'), ('unknown', 'Unknown')], max_length=255, null=True),
        ),
    ]
