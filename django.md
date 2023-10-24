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