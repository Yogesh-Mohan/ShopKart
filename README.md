ShopKart
A Django-based e-commerce web application with category browsing, product discovery, search, authentication, and session-based cart features.

Overview
ShopKart is a learning-friendly online shopping project built with Django.
It includes core storefront flows such as browsing collections, viewing products, searching by keyword, user registration/login, and adding products to cart.

Features
Home page with trending products and highlighted categories
Collections page for category browsing
Category-wise product listing
Product detail page
Product search by name, description, and vendor
User authentication:
Register
Login
Logout
Session-based shopping cart with AJAX add-to-cart
Tech Stack
Python 3.13
Django 5.x
SQLite (default database)
HTML, CSS, JavaScript
Pillow (used by image generation scripts)
Project Structure
online_project: Django project root
online_project/online_project: Project settings and URL configuration
online_project/shop: Main app with models, views, routes, templates
online_project/static: CSS and uploaded product/category images
test_mysql.py: Optional MySQL connectivity test script
Prerequisites
Python 3.13
Pipenv
Git
Installation
Clone the repository.

Move into the project directory.

Install dependencies with Pipenv.

pipenv install
pipenv install --dev

If Django or Pillow is missing in your environment, install them explicitly.

pipenv install django pillow mysql-connector-python

Activate shell.

pipenv shell

Move to the Django project folder.

cd online_project

Apply migrations.

python manage.py migrate

Create admin user (optional).

python manage.py createsuperuser

Run Locally
From the online_project folder:

Open in browser:

http://127.0.0.1:8000/
http://127.0.0.1:8000/admin/
Main Routes
/ : Home
/collections/ : Category list
/collections/<category-name>/ : Products in a category
/collections/<category-name>/<product-name>/ : Product details
/search/?q=<keyword> : Product search
/register/ : User registration
/login/ : User login
/logout/ : User logout
/cart/ : Cart page
/add-to-cart/ : AJAX cart endpoint
Optional Data/Image Population
From the online_project folder:

Download real sample images.

python download_real_images.py

Populate categories and products.

python populate_original_data.py

Generate placeholder category images (if needed).

python populate_category_images.py

Notes
Default database is SQLite.
Media files are served from static/uploads in this project setup.
Cart is currently session-based (not a full order management system).
Current Pipfile may not list all runtime packages required by scripts, so explicit install may be needed.
Troubleshooting
If image scripts fail:
Ensure Pillow is installed.
If migrations fail:
Check that you are inside the online_project folder.
If login/register pages do not load:
Verify migrations were applied successfully.
If MySQL is needed:
Use test_mysql.py to verify connector and DB connectivity.
Contributing
Fork the repository
Create a feature branch
Commit your changes
Push and open a Pull Request
License
This project currently has no explicit license file.
Add a LICENSE file (for example, MIT) if you plan to distribute or accept external contributions.
