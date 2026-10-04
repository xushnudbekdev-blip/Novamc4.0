"""
Railway deploy vaqtida superuser avtomatik yaratadi.
DJANGO_SUPERUSER_PASSWORD, DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL
environment o'zgaruvchilaridan foydalanadi. Agar topilmasa — standart qiymatlar.
"""
import os
import sys
import django

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "novamc.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "Novajon")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "951734009")
email    = os.environ.get("DJANGO_SUPERUSER_EMAIL",    "ferdavsergashev6@gmail.com")

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, password=password, email=email)
    print(f"[+] Superuser yaratildi: {username}")
else:
    # Parolni va huquqlarni har safar yangilaymiz (env o'zgaruvchisi orqali boshqarish uchun)
    user = User.objects.get(username=username)
    user.set_password(password)
    user.is_staff = True
    user.is_superuser = True
    user.is_active = True
    user.save()
    print(f"[~] Superuser mavjud, paroli va huquqlari yangilandi: {username}")
