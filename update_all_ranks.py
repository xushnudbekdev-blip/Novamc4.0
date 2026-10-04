import os
import sys
import django

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "novamc.settings")
django.setup()

from shop.models import ServerMode, Category, Product

print("=== SERVERLARNI VA RANKLARNI YANGILASH BOSHLANDI ===")

# 1. SERVERLARNI SOZLASH
# Anarxiya1
anarxiya1, _ = ServerMode.objects.get_or_create(
    slug='anarxiya1',
    defaults={'name': 'Anarxiya1', 'order': 1, 'is_active': True}
)
anarxiya1.name = 'Anarxiya1'
anarxiya1.order = 1
anarxiya1.is_active = True
anarxiya1.save()

# SMP (Anarxiya2 o'rniga)
smp, _ = ServerMode.objects.get_or_create(
    slug='smp',
    defaults={'name': 'SMP', 'order': 2, 'is_active': True}
)
smp.name = 'SMP'
smp.order = 2
smp.is_active = True
smp.save()

# Eski Anarxiya2 bo'lsa nom va slug o'zgartiramiz / tozalaymiz
old_a2 = ServerMode.objects.filter(slug='anarxiya2').first()
if old_a2 and old_a2.id != smp.id:
    # re-link categories
    Category.objects.filter(server=old_a2).update(server=smp)
    old_a2.delete()

# Duels (BoxPvP o'rniga)
duels, _ = ServerMode.objects.get_or_create(
    slug='duels',
    defaults={'name': 'Duels', 'order': 3, 'is_active': True}
)
duels.name = 'Duels'
duels.order = 3
duels.is_active = True
duels.save()

old_bp = ServerMode.objects.filter(slug='boxpvp').first()
if old_bp and old_bp.id != duels.id:
    Category.objects.filter(server=old_bp).update(server=duels)
    old_bp.delete()

print("Serverlar tayyor: Anarxiya1, SMP, Duels.")


# ---------------------------------------------------------------------------
# 2. ANARXIYA 1 DONATOR RANKLAR
# ---------------------------------------------------------------------------
a1_cat, _ = Category.objects.get_or_create(
    slug='anarxiya1-donator-ranklar',
    defaults={'name': 'Donator Ranklar', 'server': anarxiya1, 'order': 1}
)
a1_cat.server = anarxiya1
a1_cat.name = 'Donator Ranklar'
a1_cat.order = 1
a1_cat.save()

# Old products in a1_cat delete
Product.objects.filter(category=a1_cat).delete()

a1_ranks = [
    {
        'name': 'RABBIT',
        'slug': 'anarxiya1-rabbit',
        'price': 29000,
        'commands': '/kit',
        'features': (
            'PLUS, PLUSPRO va maxsus RABBIT to‘plamlari\n'
            '/sethome — 999+ ta uy joylash joyi\n'
            'Moblar va o‘ldirishlardan valyuta ko‘paytirgichi: x3.0\n'
            'Privatlar soni: 999+\n'
            'Auksiondagi joy: 999\n'
            'Server to‘la bo‘lsa ham kirish imkoniyati'
        ),
    },
    {
        'name': 'TIGER',
        'slug': 'anarxiya1-tiger',
        'price': 69000,
        'commands': '/kit',
        'features': (
            'PLUS, PLUSPRO va maxsus TIGER to‘plamlari\n'
            '/sethome — 999+ ta uy joylash joyi\n'
            'Moblar va o‘ldirishlardan valyuta ko‘paytirgichi: x5.0\n'
            'Privatlar soni: 999+\n'
            'Auksiondagi joy: 999\n'
            'Server to‘la bo‘lsa ham kirish imkoniyati'
        ),
    },
    {
        'name': 'HYDRA',
        'slug': 'anarxiya1-hydra',
        'price': 119000,
        'commands': '/kit',
        'features': (
            'PLUS, PLUSPRO va maxsus HYDRA to‘plamlari\n'
            '/sethome — 999+ ta uy joylash joyi\n'
            'Moblar va o‘ldirishlardan valyuta ko‘paytirgichi: x4.0\n'
            'Privatlar soni: 999+\n'
            'Auksiondagi joy: 999\n'
            'Server to‘la bo‘lsa ham kirish imkoniyati'
        ),
    },
    {
        'name': 'D.HELPER',
        'slug': 'anarxiya1-d-helper',
        'price': 139000,
        'commands': '/kit',
        'features': (
            'PLUS, PLUSPRO va maxsus D.HELPER to‘plamlari\n'
            '/sethome — 999+ ta uy joylash joyi\n'
            'Moblar va o‘ldirishlardan valyuta ko‘paytirgichi: x5.0\n'
            'Privatlar soni: 999+\n'
            'Auksiondagi joy: 999\n'
            'Server to‘la bo‘lsa ham kirish imkoniyati'
        ),
    },
    {
        'name': 'GOD',
        'slug': 'anarxiya1-god',
        'price': 259000,
        'commands': '/kit',
        'features': (
            'PLUS, PLUSPRO va maxsus GOD to‘plamlari\n'
            '/sethome — 999+ ta uy joylash joyi\n'
            'Moblar va o‘ldirishlardan valyuta ko‘paytirgichi: x5.0\n'
            'Privatlar soni: 999+\n'
            'Auksiondagi joy: 999\n'
            'Server to‘la bo‘lsa ham kirish imkoniyati'
        ),
    },
    {
        'name': 'PEGAS',
        'slug': 'anarxiya1-pegas',
        'price': 329000,
        'commands': '/kit',
        'features': (
            'PLUS, PLUSPRO va maxsus PEGAS to‘plamlari\n'
            '/sethome — 999+ ta uy joylash joyi\n'
            'Moblar va o‘ldirishlardan valyuta ko‘paytirgichi: x5.0\n'
            'Privatlar soni: 999+\n'
            'Auksiondagi joy: 999\n'
            'Server to‘la bo‘lsa ham kirish imkoniyati'
        ),
    },
    {
        'name': 'PURPLE / CASH',
        'slug': 'anarxiya1-purple-cash',
        'price': 399000,
        'commands': '/kit',
        'features': (
            'PLUS, PLUSPRO va maxsus CASH to‘plamlari\n'
            '/sethome — 999+ ta uy joylash joyi\n'
            'Moblar va o‘ldirishlardan valyuta ko‘paytirgichi: x5.0\n'
            'Privatlar soni: 999+\n'
            'Auksiondagi joy: 999\n'
            'Server to‘la bo‘lsa ham kirish imkoniyati'
        ),
    },
]

for r in a1_ranks:
    Product.objects.create(
        name=r['name'],
        slug=r['slug'],
        category=a1_cat,
        price=r['price'],
        commands=r['commands'],
        features=r['features'],
        is_active=True
    )
    print(f"  [Anarxiya1] + {r['name']} ({r['price']:,} UZS)")


# ---------------------------------------------------------------------------
# 3. SMP DONATOR RANKLAR (PRIME)
# ---------------------------------------------------------------------------
smp_cat, _ = Category.objects.get_or_create(
    slug='smp-donator-ranklar',
    defaults={'name': 'Donator Ranklar', 'server': smp, 'order': 1}
)
smp_cat.server = smp
smp_cat.name = 'Donator Ranklar'
smp_cat.order = 1
smp_cat.save()

# Delete old categories of Anarxiya2 main ranks
Category.objects.filter(slug__in=['anarxiya2-asosiy-ranklar', 'asosiy-ranklar']).delete()
Product.objects.filter(category=smp_cat).delete()

smp_ranks = [
    {
        'name': 'PRIME',
        'slug': 'smp-prime',
        'price': 49000,
        'commands': '/kit prime',
        'features': (
            'PRIME to‘plami – /kit prime\n'
            '/sethome — 999+ ta uy joylash joyi\n'
            'Auksiondagi joy: 999\n'
            'Server to‘la bo‘lsa ham kirish imkoniyati'
        ),
    }
]

for r in smp_ranks:
    Product.objects.create(
        name=r['name'],
        slug=r['slug'],
        category=smp_cat,
        price=r['price'],
        commands=r['commands'],
        features=r['features'],
        is_active=True
    )
    print(f"  [SMP] + {r['name']} ({r['price']:,} UZS)")


# ---------------------------------------------------------------------------
# 4. DUELS DONATOR RANKLAR
# ---------------------------------------------------------------------------
duels_cat, _ = Category.objects.get_or_create(
    slug='duels-donator-ranklar',
    defaults={'name': 'Donator Ranklar', 'server': duels, 'order': 1}
)
duels_cat.server = duels
duels_cat.name = 'Donator Ranklar'
duels_cat.order = 1
duels_cat.save()

# Delete old boxpvp ranks
Category.objects.filter(slug='boxpvp-donator-ranklar').delete()
Product.objects.filter(category=duels_cat).delete()

duels_ranks = [
    {
        'name': '👑 King',
        'slug': 'duels-king',
        'price': 19000,
        'commands': '/store king',
        'features': (
            'Quick Join\'ga ruxsat\n'
            'Jamoa nomini ko‘rsatish\n'
            'Emote buyruqlariga ruxsat'
        ),
    },
    {
        'name': '🦁 Lion',
        'slug': 'duels-lion',
        'price': 35000,
        'commands': '/store lion',
        'features': (
            'Quick Join\'ga ruxsat\n'
            'Jamoa nomini ko‘rsatish\n'
            'Emote buyruqlariga ruxsat\n'
            'Discord\'da maxsus rol'
        ),
    },
    {
        'name': '🛡️ Hero',
        'slug': 'duels-hero',
        'price': 55000,
        'commands': '/store hero',
        'features': (
            'Quick Join\'ga ruxsat\n'
            'Jamoa nomini ko‘rsatish\n'
            'Emote buyruqlariga ruxsat\n'
            'Discord\'da maxsus rol\n'
            'Shaxsiy arenaga ruxsat\n'
            'Party duellarga ruxsat\n'
            'Bezakli (trim) zirhlarga ruxsat'
        ),
    },
    {
        'name': '⭐ Legend',
        'slug': 'duels-legend',
        'price': 75000,
        'commands': '/store legend',
        'features': (
            'Quick Join\'ga ruxsat\n'
            'Jamoa nomini ko‘rsatish\n'
            'Emote buyruqlariga ruxsat\n'
            'Discord\'da maxsus rol\n'
            'Shaxsiy arenaga ruxsat\n'
            'Party duellarga ruxsat\n'
            'Bezakli (trim) zirhlarga ruxsat\n'
            'Lobbida uchishga ruxsat'
        ),
    },
    {
        'name': '⚡ Master',
        'slug': 'duels-master',
        'price': 99000,
        'commands': '/store master',
        'features': (
            'Quick Join\'ga ruxsat\n'
            'Jamoa nomini ko‘rsatish\n'
            'Emote buyruqlariga ruxsat\n'
            'Discord\'da maxsus rol\n'
            'Jamoa yaratishga ruxsat\n'
            'Party duellarga ruxsat\n'
            'Bezakli (trim) zirhlarga ruxsat\n'
            'Lobbida uchishga ruxsat'
        ),
    },
]

for r in duels_ranks:
    Product.objects.create(
        name=r['name'],
        slug=r['slug'],
        category=duels_cat,
        price=r['price'],
        commands=r['commands'],
        features=r['features'],
        is_active=True
    )
    print(f"  [Duels] + {r['name']} ({r['price']:,} UZS)")


# ---------------------------------------------------------------------------
# 5. MA'MURIYAT VA BOSHOA NARSALAR KATEGORIYALARINI HAR BIR SERVER UCHUN SAQLASH
# ---------------------------------------------------------------------------
mamuriyat_products = [
    {
        'name': 'Homiy', 'price': 200000,
        'commands': '/titul\n/uc menu',
        'features': 'Homiy rangi va titul\nUnikal titul - /titul\nUnikal effektlar - /uc menu\nServer homiysi sifatida tanilish',
    },
    {
        'name': 'Admin', 'price': 150000,
        'commands': '/titul\n/uc menu',
        'features': 'Admin rangi va titul\nUnikal titul - /titul\nUnikal effektlar - /uc menu',
    },
    {
        'name': 'Moder', 'price': 100000,
        'commands': '/titul\n/uc menu',
        'features': 'Moder rangi va titul\nUnikal titul - /titul\nUnikal effektlar - /uc menu',
    },
    {
        'name': 'Helper', 'price': 50000,
        'commands': '/titul\n/uc menu',
        'features': 'Helper rangi va titul\nUnikal titul - /titul\nUnikal effektlar - /uc menu',
    },
]

boshqa_products = [
    {
        'name': 'Donate Case', 'price': 10000,
        'commands': '', 'features': 'Donate Case - maxsus sovrinlar bilan quti',
    },
    {
        'name': 'Token Case', 'price': 5000,
        'commands': '', 'features': 'Token Case - tokenlar bilan quti',
    },
    {
        'name': 'Maxsus Titul', 'price': 5000,
        'commands': '/titul', 'features': 'Maxsus unikal titul - /titul',
    },
    {
        'name': 'Narsani nusxalash', 'price': 5000,
        'commands': '', 'features': 'Qolinizdagi buyumni nusxalash xizmati',
    },
    {
        'name': '1000 Token', 'price': 1000,
        'commands': '', 'features': '1000 ta server tokeni',
    },
]

for server in [anarxiya1, smp, duels]:
    s = server.slug

    # Ma'muriyat va Maxsus
    mcat, _ = Category.objects.get_or_create(
        slug=s + '-mamuriyat-va-maxsus',
        defaults={'name': "Ma'muriyat va Maxsus", 'server': server, 'order': 2}
    )
    mcat.server = server
    mcat.name = "Ma'muriyat va Maxsus"
    mcat.order = 2
    mcat.save()

    for p in mamuriyat_products:
        p_slug = s + '-' + p['name'].lower().replace(' ', '-')
        Product.objects.update_or_create(
            slug=p_slug,
            defaults={
                'name': p['name'], 'category': mcat,
                'price': p['price'], 'commands': p['commands'],
                'features': p['features'], 'is_active': True,
            }
        )

    # Boshqa Narsalar
    bcat, _ = Category.objects.get_or_create(
        slug=s + '-boshqa-narsalar',
        defaults={'name': 'Boshqa Narsalar', 'server': server, 'order': 3}
    )
    bcat.server = server
    bcat.name = 'Boshqa Narsalar'
    bcat.order = 3
    bcat.save()

    for p in boshqa_products:
        p_slug = s + '-' + p['name'].lower().replace(' ', '-')
        Product.objects.update_or_create(
            slug=p_slug,
            defaults={
                'name': p['name'], 'category': bcat,
                'price': p['price'], 'commands': p['commands'],
                'features': p['features'], 'is_active': True,
            }
        )

print("=== MAVJUD SHABLON VA DATABASE TO'LIQ YANGILANDI! ===")
