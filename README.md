# Vendor Management System
The Vendor Management System is a web application built using Django, designed to help manage vendors and purchase orders for a business. It allows users to perform CRUD operations on vendors and purchase orders, track vendor performance metrics, and view historical performance data.

## Installation

### Clone the repository:

```bash
git clone https://github.com/SHIV000000/VendorEase.git
```
### Navigate to the project directory:

```bash
cd VendorEase
```
## Create a virtual environment:


#### Windows:

```bash
py -m venv env
```

#### Unix/macOS:

```bash
python -m venv env
```

### Activate the virtual environment:

#### Windows:

```bash
 env\Scripts\activate
```

#### Unix/macOS:

```bash
source env/bin/activate
```
## Install dependencies:

```bash
pip install -r requirements.txt
```
### Run migrations:

```bash
python manage.py migrate
```

### Start the development server:

```bash
python manage.py runserver
```
### Usage
Access the application: Open your web browser and navigate to http://localhost:8000/.

### Admin panel: Access the Django admin panel by visiting http://localhost:8000/admin/. You can login using the admin credentials configured during installation.

## Features
```bash
Vendor Management:
Add, view, update, and delete vendors.
View vendor details and performance metrics.

Purchase Order Management:
Add, view, update, and delete purchase orders.
Track purchase order status and details.

Performance Metrics:
Calculate and display vendor performance metrics, including on-time delivery rate, quality rating average, average response time, and fulfillment rate.

Historical Performance:
Store and display historical performance data for vendors.
```

## Project Structure
### vendor_management/: Django project directory.
### frontend/: Contains HTML templates and incorporated Tailwind CDN CSS .
### vendors/: Django app for managing vendors and purchase orders.
### db.sqlite3: SQLite database file.
### manage.py: Django project management script.
