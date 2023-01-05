# tree-menu-django

This django-app allows you to add menus (one or more) to the database through the admin panel, and draw menus by name on any desired page․

## Installation

```bash
git clone git@github.com:LianaSmile/tree-menu-django.git
cd tree_menu
python3 -m venv venv
source venv/bin/activate
pip install -r requirements/requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Usage
1. Direct to: http://127.0.0.1:8000/admin.
2. Add menus and submenus. 
3. Go to tree_menu/menus/templates/menus/menu.html file
4. Change  'menu_name_example' with your menu name in this part: 

```bash
{% draw_menu 'menu_name_example' request.path %}
```



## Status
Always can be improved :)