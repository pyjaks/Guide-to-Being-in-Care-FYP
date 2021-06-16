Project has 3 main apps - main (with guide content templates), discussion board, and accounts (for custom user model making use of date of birth for restricting access to pages based on user's age).

### To Run

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

python manage.py sass scss/custom.scss static/main/css/custom.css
python manage.py collectstatic

python manage.py runserver
```

