# FAQ Management System with Multi-Language Support

A Django-based FAQ management system with multi-language translation support. The system allows administrators to manage FAQs in English, and users can view FAQs in their preferred language through a REST API.

## Features:
- Store FAQs in English with the ability to display in different languages (Hindi, Gujarati, etc.).
- Use of `django-ckeditor` for WYSIWYG editor to format FAQ answers.
- Integration with **Google Translate API** to translate FAQs into multiple languages.
- Use of **Redis** for caching translated FAQs to improve performance.
- Admin interface to manage FAQs, only accessible to superusers.
- REST API to manage and fetch FAQs with language support.

- ## Technologies Used
- Django
- Django REST Framework
- Google Translate (via `googletrans` library)
- Redis for caching
- django-ckeditor for the WYSIWYG editor

## Table of Contents:
1. [Installation](#installation)
2. [API Usage](#api-usage)
3. [Caching](#caching)
4. [Contribution](#contribution)
5. [License](#license)
6. [Acknowledgments](#acknowledgment)

---

## Installation

### Prerequisites
- Python 11
- Redis (for caching)

### 1. Clone the Repository

```bash
git clone https://github.com/niyatiipansuriya/faq-management-system.git
cd faq-management-system
```

### 2. Set Up Virtual Environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment:

For macOS/Linux:
``` bash
source venv/bin/activate
```

For Windows:
```bash
venv\Scripts\activate
```

### 4. Install the required dependencies:

```bash
pip install django-ckeditor
pip install googletrans==4.0.0-rc1
pip install redis
pip install django-redis

```
###5. Set up Redis:

Install Redis on your machine** (if it's not already installed).

   - **For Windows:**
     - [Download Redis for Windows](https://github.com/microsoftarchive/redis/releases) and follow the installation instructions.

   - **For macOS/Linux:**

     - **macOS (via Homebrew):**
       ```bash
       brew install redis
       ```

     - **Linux (Debian/Ubuntu):**
       ```bash
       sudo apt-get install redis-server
       ```

 - Start Redis server**:
   After Redis is installed, you can start the Redis server by running the following command in your terminal:
   ```bash
   redis-server
   ```

###6. Set up the Django project:

  -First, run makemigrations to create any required migrations for the database:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

### 7. Create a superuser for accessing the Django Admin Panel:

```bash
python manage.py createsuperuser
```

### 8. Run the development server:

```bash
python manage.py runserver
```

###9. Access the application:

Open your browser and go to http://127.0.0.1:8000/.



## API Usage

### Fetch all FAQs

*   **Endpoint**: `http://localhost:8000/api/faqs/`
*   **Description**: Returns all FAQs in English by default.

### Fetch FAQs in a specific language

*   **Endpoint**: `http://localhost:8000/api/faqs/<language_code>/`
*   **Example**: `http://localhost:8000/api/faqs/bn/` will return FAQs in Bengali.
*   **Example**: `http://localhost:8000/api/faqs/hi/` will return FAQs in Hindi.

## Admin Panel
Access the admin panel at http://127.0.0.1:8000/admin/
Admin can manage FAQs (add, update, delete).
You need to create a superuser to access the admin panel:

``` bash
python manage.py createsuperuser
```

## Caching

   -Translations are cached using Redis for performance.
   -You need to have Redis installed and running on your machine (As mentioned above).

## Contribution

   -Fork the repository.
   -Create a feature branch (git checkout -b feature-branch).
   -Commit your changes (git commit -m 'feat: Add new feature').
   -Push to the branch (git push origin feature-branch).
   -Create a pull request.

## License

   -This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

   -Django for the web framework
   -django-ckeditor for the WYSIWYG editor
   -googletrans for language translation
   -Redis for caching

