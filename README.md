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

Then create **volumes** as below.


```bash 
docker volume create static_volume
docker volume create media_volume
```


You need to create .env file in the project root file with default values.


```bash 
cd django-restaurant
touch .env
```

## django-restaurant/.env

```python
DJANGO_SUPERUSER_PASSWORD='Your password for superuser'

SECRET_KEY = 'Your SECRET_KEY'


POSTGRES_DB = "Your POSTGRES_DB"
POSTGRES_USER = "Your POSTGRES_USER"
POSTGRES_PASSWORD = "Your POSTGRES_PASSWORD"
POSTGRES_HOST = "postgresql"
POSTGRES_PORT = "5432"


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
also You need to create **.env** file and **data** folder in the postgresql folder


```bash 
cd postgresql
touch .env
mkdir data
```

## django-restaurant/postgresql/.env

```python
POSTGRES_USER = "Your POSTGRES_USER"
POSTGRES_PASSWORD = "Your POSTGRES_PASSWORD"
POSTGRES_DB = "Your POSTGRES_DB"
```

Now run django and postgresql with **docker-compose**.

```bash 
cd ..
docker-compose up --build
```

done. You can see shah berger restaurant web page on http://localhost



## Screenshots

![Screenshot](https://i.imgur.com/XL9Zdk8.png)
![Screenshot](https://i.imgur.com/Wcvyxic.png)
![Screenshot](https://i.imgur.com/qclsNIw.png)


## Contributing
Contributions are  **welcome**  and will be fully  **credited**. I'd be happy to accept PRs for template extending.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/sepehrhozzari/django-restaurant/blob/master/LICENSE) file for details

