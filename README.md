## Ekologiya
Cmd venv activation:
```
python -m venv venv
call venv/Scripts/activate
```
Clone, create venv and run:

```python
pip install -r requirements/develop.txt
python manage.py migrate
python manage.py createsuperuser
``` 

## In Deployment or Develop don't forget that!
https://stackoverflow.com/questions/35101850/cant-find-msguniq-make-sure-you-have-gnu-gettext-tools-0-15-or-newer-installed
### For windows run this command in cmd .Othervise In Vscode will not work
```python
django-admin makemessages -l en
django-admin makemessages -l ru
django-admin makemessages -l uz
python manage.py compilemessages
```
## Examples
![alt text](static/image.png)
