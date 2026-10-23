# Pokédex API (Django + DRF + SimpleJWT)

```bash
python -m venv venv
venv\Scripts\activate            # Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations users pokemons
python manage.py migrate
python manage.py runserver
```

Run `makemigrations users pokemons` **before** the first `migrate`
(users must be migrated first because it is the custom user model).

Quick Postman flow:
1. POST /api/users/ (username, password, confirm_password, level)
2. POST /api/token/ (username, password) -> copy `access`
3. Send header `Authorization: Bearer <access>` to /api/pokemons/
   (use form-data when uploading images)
