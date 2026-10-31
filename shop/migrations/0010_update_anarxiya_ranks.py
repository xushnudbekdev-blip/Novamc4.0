from django.db import migrations
from django.utils.text import slugify


NEW_RANKS = [
    ('Askar', 6000,
     '/kit askar\n/hat\n/top',
     'Homelar soni: 4 ta\nRegion bloklar: 4 ta\nAuksion slotlari: 8 ta\nEnderchest: 4 qator\nTeleport vaqti: 6 soniya'),
    ('Qahramon', 10500,
     '/kit qahramon\n/clear\n/feed\n/heal\n/me',
     'Homelar soni: 5 ta\nRegion bloklar: 4 ta\nAuksion slotlari: 9 ta\nEnderchest: 4 qator\nTeleport vaqti: 6 soniya'),
    ('Ritsar', 16000,
     '/kit ritsar\n/back\n/ec\n/wbench\n/itemname',
     "O'limda XP saqlanib qoladi\nRangli yozish imkoni\nHomelar soni: 6 ta\nRegion bloklar: 6 ta\nAuksion slotlari: 10 ta\nEnderchest: 4 qator\nTeleport vaqti: 5 soniya"),
    ('Alpomish', 22000,
     '/kit alpomish\n/bc\n/ext\n/msgtoggle\n/paytoggle\n/tptoggle\n/feed\n/heal',
     'Homelar soni: 8 ta\nRegion bloklar: 7 ta\nAuksion slotlari: 11 ta\nEnderchest: 5 qator\nTeleport vaqti: 4 soniya'),
    ('Titan', 29000,
     '/kit titan\n/time\n/weather\n/loom\n/carttable\n/eztooka\n/firework',
     'Homelar soni: 10 ta\nRegion bloklar: 7 ta\nAuksion slotlari: 12 ta\nEnderchest: 5 qator\nTeleport vaqti: 4 soniya'),
    ('Elita', 37000,
     '/kit elita\n/jump\n/afk\n/setwarp\n/delwarp\n/repair',
     "AFK paytida kick qilinmaydi\nHomelar soni: 12 ta\nRegion bloklar: 8 ta\nAuksion slotlari: 12 ta\nEnderchest: 5 qator\nTeleport vaqti: 3 soniya"),
    ('Afsona', 48000,
     '/kit afsona\n/smithtable\n/stonecutter\n/grindstone',
     'Homelar soni: 15 ta\nRegion bloklar: 10 ta\nAuksion slotlari: 14 ta\nEnderchest: 5 qator\nTeleport vaqti: 3 soniya'),
    ('General', 68000,
     '/kit general',
     "Teleportga cheklov yo'q\nHomelar soni: 18 ta\nRegion bloklar: 15 ta\nAuksion slotlari: 13 ta\nEnderchest: 6 qator\nTeleport vaqti: 0 soniya"),
    ('Imperator', 86000,
     '/kit imperator\n/fly',
     "Teleportga cheklov yo'q\nUchish imkoni (/fly)\nHomelar soni: 20 ta\nRegion bloklar: 15 ta\nAuksion slotlari: 16 ta\nEnderchest: 6 qator\nTeleport vaqti: 0 soniya"),
]


def update_ranks(apps, schema_editor):
    ServerMode = apps.get_model('shop', 'ServerMode')
    Category = apps.get_model('shop', 'Category')
    Product = apps.get_model('shop', 'Product')

    # Anarxiya1 serverini yaratish yoki topish
    server, _ = ServerMode.objects.get_or_create(
        slug='anarxiya1',
        defaults={'name': 'Anarxiya1', 'order': 1, 'is_active': True}
    )

    # "Donator Ranklar" kategoriyasini yaratish yoki topish
    cat, _ = Category.objects.get_or_create(
        slug='anarxiya1-donator-ranklar',
        defaults={'name': 'Donator Ranklar', 'server': server, 'order': 1}
    )
    cat.server = server
    cat.save()

    # Eski rank mahsulotlarini o'chirish (faqat shu kategoriyadan)
    Product.objects.filter(category=cat).delete()

    # Yangi ranklarni qo'shish
    for name, price, commands, features in NEW_RANKS:
        base_slug = slugify(name)
        slug = base_slug
        counter = 1
        while Product.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        Product.objects.create(
            category=cat,
            name=name,
            slug=slug,
            price=price,
            commands=commands,
            features=features,
            is_active=True,
        )


def reverse_ranks(apps, schema_editor):
    # Rollback: yangi ranklarni o'chirish
    Product = apps.get_model('shop', 'Product')
    Category = apps.get_model('shop', 'Category')
    cat = Category.objects.filter(slug='anarxiya1-donator-ranklar').first()
    if cat:
        Product.objects.filter(category=cat).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_sitesettings_telegram_bot_token'),
    ]

    operations = [
        migrations.RunPython(update_ranks, reverse_ranks),
    ]
