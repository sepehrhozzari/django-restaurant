# Shah Berger Restaurant
<p align="center">
  <img src="https://i.imgur.com/LNbDJT4.png">
</p>
<p align="center">
  <img src="https://i.imgur.com/xIcTiQK.png">
</p>
Shah Berger is a perfect restaurant application written by Python3 & Django4.0.

## Installation

First **clone** this project.

```bash 
git clone https://github.com/sepehrhozzari/django-restaurant.git
```

Then create **virtualenv** as below.

```bash 
cd django-restaurant
virtualenv .venv
source .venv/bin/activate
```

install **requirements**.

```bash 
pip install -r requirements.txt
```


You need to create .env file in the project root file.

## .env

```python
SECRET_KEY = 'Your SECRET_KEY'

DB_NAME = 'Your DB_NAME'
DB_USER = 'Your DB_USER'
DB_PASSWORD = 'Your DB_PASSWORD'
DB_HOST = 'Your DB_HOST'

EMAIL_HOST = 'Your EMAIL_HOST'
EMAIL_PORT = 'Your EMAIL_PORT'
EMAIL_HOST_USER = 'Your EMAIL_HOST_USER'
EMAIL_HOST_PASSWORD = 'Your EMAIL_HOST_PASSWORD'

SOCIAL_AUTH_GITHUB_KEY = 'Your SOCIAL_AUTH_GITHUB_KEY'
SOCIAL_AUTH_GITHUB_SECRET = 'Your SOCIAL_AUTH_GITHUB_SECRET'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'Your SOCIAL_AUTH_GOOGLE_OAUTH2_KEY'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'Your SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET'

SOCIAL_AUTH_FACEBOOK_KEY = 'Your SOCIAL_AUTH_FACEBOOK_KEY'
SOCIAL_AUTH_FACEBOOK_SECRET = 'Your SOCIAL_AUTH_FACEBOOK_SECRET'

```

finally migrate and runserver.

```bash 
python3 manage.py migrate
python3 manage.py runserver
```

## Screenshots

![Screenshot](https://i.imgur.com/XL9Zdk8.png)
![Screenshot](https://i.imgur.com/Wcvyxic.png)
![Screenshot](https://i.imgur.com/qclsNIw.png)


## Contributing
Contributions are  **welcome**  and will be fully  **credited**. I'd be happy to accept PRs for template extending.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/sepehrhozzari/django-restaurant/blob/master/LICENSE) file for details

