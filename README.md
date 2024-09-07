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
sudo apt-get install -y gettext
django-admin makemessages -l en
python manage.py compilemessages
```

## Incase permission denied to upload images
```python
sudo chown -R your_username:your_groupname /home/bahrom04/workplace/django/ekologiya/media
sudo chmod -R 755 /home/bahrom04/workplace/django/ekologiya/media
```
## Nginx
```
sudo systemctl status nginx
```
## ufw configurations
## Clear Docker Containers in development (django & postgres) Don't run it on production server
```python
docker-compose down --volumes --remove-orphans
```
If you run this command it will also delete postgres database and their volumes. So run this when you want to test new containers. See conversation below:
https://chat.openai.com/share/f1c8d760-6062-4613-8a5b-2f88cfcfecc2

## Examples
![alt text](static/image.png)

## TailwindCss
```
python -m pip install django-tailwind
python -m pip install 'django-tailwind[reload]'
sudo npm install -g cross-env
python manage.py tailwind install
python manage.py tailwind start
```

## Ownership issues with git
```
git config --global --add safe.directory /home/web/kedi.uz
```

## Redis
```
redis-server

# mac 
brew services start redis  # start
brew services stop redis  # stop

sudo systemctl start redis
sudo systemctl enable redis

sudo systemctl status redis-server

keys '*'
get <key_name>

```
