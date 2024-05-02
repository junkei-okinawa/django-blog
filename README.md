# Sample Django BLOG
## how to start
1. ZIP file expansion
```sh
unzip django-blog
```
2. chenge directory
```sh
cd django-blog
```
3. install pipenv (required pip)
```sh
pip install pipenv
```
4. install enviroment settings
```sh
pipenv install
```
5. activate enviroment
```sh
pipenv shell
```
6. start django app
```sh
python manage.py makemigrations
python manage.py migrate 
python manage.py runserver
# http://127.0.0.1:8000/
```

## create admin user
```sh
python manage.py createsuperuser
# Username: 
# Email address: 
# Password: 
# Password(again): 
```
[Go to admin page](http://127.0.0.1:8000/) and signIn

## ToDo:
- [ ] line hilight
- [ ] patch markdown for inner details tag
- [ ] emoji for frontend view