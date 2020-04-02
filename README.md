# Description

A lightweighted online exam system, users are able to take several types of questions like single selection, multiple selections, true or false, direct input short answer or long sentences.

This project is based on Python 3.6 and Django 3.0.4

## Features

- Django settings for multiple environments (Production mode & local dev. mode)
- Customized Django user model which replaced the default user model
- Connect to remote mysql database directly
- Rich-text editor embedded in Django admin

## Prerequisites

- Create a SensitiveInfo.py under settings folder

```
BASE_SECRET_KEY = 'xxxxxxxxxxxxxxxx'
BASE_ALLOWED_HOSTS = ['*']
LOCAL_ALLOWED_HOSTS = ['xxxxxxxxxxxxxxxx']
PROD_ALLOWED_HOSTS = ['xxxxxxxxxxxxxxxx']

LOCAL_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'xxxxxxxxxxxxxxxx',
        'USER': 'xxxxxxxxxxxxxxxx',
        'PASSWORD': 'xxxxxxxxxxxxxxxx',
        'HOST': '127.0.0.1',
        'PORT': 3333
    }
}

PROD_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'xxxxxxxxxxxxxxxx',
        'USER': 'xxxxxxxxxxxxxxxx',
        'PASSWORD': 'xxxxxxxxxxxxxxxx',
        'HOST': 'localhost',
        'PORT': 3306
    }
}

# USE this to link remote server mysql port 3306 to local 3333 port
# ssh -N -L 3333:127.0.0.1:3306 username@xxx.xxx.xxx.xxx -p 22
```

- Clone code to local
- Setup .venv (optional)
- pip install packages
```
asgiref==3.2.7
Django==3.0.4
mysqlclient==1.4.6
Pillow==7.0.0
pytz==2019.3
sqlparse==0.3.1
```


![Screenshot](https://github.com/sctongye/Somsyd-ExamSys/blob/master/Screenshots/01.png?raw=true "Screenshoot")

![Screenshot](https://github.com/sctongye/Somsyd-ExamSys/blob/master/Screenshots/02.png?raw=true "Screenshoot")

![Screenshot](https://github.com/sctongye/Somsyd-ExamSys/blob/master/Screenshots/03.png?raw=true "Screenshoot")

![Screenshot](https://github.com/sctongye/Somsyd-ExamSys/blob/master/Screenshots/04.png?raw=true "Screenshoot")
