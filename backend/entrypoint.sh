#python manage.py makemigrations
#python manage.py migrate
#python manage.py collectmedia
python manage.py migrate
python manage.py collectstatic --no-input
python manage.py runserver 0.0.0.0:8000