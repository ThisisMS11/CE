## Rendering HTML Templates in Django
Rendering some data from a database Article table (stored in sqlite dynamically).
![](/photos/1.png)

## Environment Variables in Django

1. Do **pip install django-dotenv**
2. Whereever you want to use variables out of the env file do the following :
```
import os 
SECRET_KEY = os.environ.get("SECRET_KEY",default_value)
```
3. Inside Manage.py
```
import dotenv
dotenv.read_dotenv()
```

## Github clone Thing
```
1. Go the django project and clone it .

2. git clone https://github.com/ThisisMS11/CE.git

3. cd CE

4. Now first recreate the virtual environment with the help of the following commands :
    a. pyenv virtualenv environment_name
    b. pyenv activate environment_name

5. So I assume that you have successfully created your virtual environment and you do have a requirements.txt file in your django project.

6. pip install -r requirements.txt

7. pip list (to view the installed dependencies)
```