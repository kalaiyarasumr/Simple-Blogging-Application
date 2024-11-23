Simple Blog Application
A web-based blogging application built with Django and Django REST Framework (DRF). This project allows users to create, read, update, and delete blog posts with categorized content.

Features
CRUD Operations for blog posts.
Categorization of blog posts.
Interactive API documentation using DRF.
Extensible and modular structure for future enhancements.
Technologies Used
Backend: Django, Django REST Framework
Database: SQLite (default, can be configured for PostgreSQL/MySQL)
Tools: Git, Python, Visual Studio Code
Installation Guide
Prerequisites
Python 3.9+ installed on your system
Git installed
Virtual environment (optional but recommended)
Steps
Clone the Repository

bash
Copy code
git clone https://github.com/kalaiyarasumr/Simple-Blogging-Application.git
cd Simple-Blogging-Application
Set Up Virtual Environment (Optional but Recommended)

bash
Copy code
python -m venv env
source env/bin/activate    # On Windows: env\Scripts\activate
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Run Migrations

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Run the Server

bash
Copy code
python manage.py runserver
Open your browser and navigate to http://127.0.0.1:8000/.

Usage
Creating a Blog Post
Access the /api/posts/ endpoint via POST request.
Provide JSON data with the following format:
json
Copy code
{
    "title": "Blog Title",
    "description": "Short Description",
    "content": "Detailed Content",
    "category": "Web-dev"
}
Viewing All Posts
Access the /api/posts/ endpoint via GET request.
Updating a Post
Access the /api/posts/<id>/ endpoint via PUT request with updated JSON data.
Deleting a Post
Access the /api/posts/<id>/ endpoint via DELETE request.
API Endpoints
Endpoint	Method	Description
/api/posts/	GET	List all blog posts
/api/posts/	POST	Create a new blog post
/api/posts/<id>/	GET	Retrieve a specific post
/api/posts/<id>/	PUT	Update a specific post
/api/posts/<id>/	DELETE	Delete a specific post
Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch for your feature or bugfix:
bash
Copy code
git checkout -b feature-name
Commit your changes:
bash
Copy code
git commit -m "Description of your changes"
Push to your branch:
bash
Copy code
git push origin feature-name
Create a Pull Request.
