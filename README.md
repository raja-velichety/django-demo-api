Django Invoice API
This is a simple Django API for managing invoices and invoice details. It supports creating and updating invoices, along with their associated line items.

Prerequisites
Python 3.x
Django 3.x or higher
Steps to Run Locally
1. Clone the Repository
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/raja-velichety/django-demo-api.git
cd your-repo-name
2. Set Up a Virtual Environment
Create and activate a virtual environment to isolate dependencies:

bash
Copy code
# For macOS/Linux:
python3 -m venv venv
source venv/bin/activate

# For Windows:
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt

4. Set Up Database

use the default SQLite database for development purposes by leaving DATABASES as-is.

5. Run Migrations
Run database migrations to set up the schema:

bash
Copy code
python manage.py migrate
7. Create a Superuser (Optional)
If you want to use the Django admin interface, create a superuser:

bash
Copy code
python manage.py createsuperuser
8. Start the Development Server
Run the Django development server:

bash
Copy code
python manage.py runserver
Visit http://127.0.0.1:8000/ to view the API.

# API Endpoints
POST /api/invoices/ — Create a new invoice.
PUT /api/invoices/ — Update a invoice
