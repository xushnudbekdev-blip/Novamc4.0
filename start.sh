#!/bin/bash
# Apply database migrations
python manage.py migrate

# Create or update superuser
python create_superuser.py

# Collect static files
python manage.py collectstatic --noinput

# Barcha server, kategoriya va mahsulotlarni bazaga avtomatik qo'shish/yangilash
python seed_all.py

# Start the Telegram bot in the background
python bot.py &

# Start the Django web app
gunicorn novamc.wsgi:application --bind 0.0.0.0:$PORT
