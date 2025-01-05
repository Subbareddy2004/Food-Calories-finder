# Foodie Calorie Finder

A web application that helps you track and find calories in your food items. This Django-based application provides an easy-to-use interface for monitoring your daily caloric intake.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Foodie-calorie-finder.git
   cd Foodie-calorie-finder
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On Unix or MacOS
   source venv/bin/activate
   ```

3. Install required dependencies:
   ```bash
   pip install django
   pip install pillow  # for image processing
   ```

4. Set up the database:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (admin) account:
   ```bash
   python manage.py createsuperuser
   ```

## Running the Application

1. Start the development server:
   ```bash
   python manage.py runserver
   ```

2. Open your web browser and navigate to:
   - Main application: http://127.0.0.1:8000/
   - Admin interface: http://127.0.0.1:8000/admin/

## Features

- Track daily caloric intake
- Search for food items and their caloric content
- User-friendly interface
- Admin panel for managing food database

## Project Structure

- `counter/`: Main application directory containing views and models
- `foodie/`: Project settings and configuration
- `static/`: Static files (CSS, JavaScript, images)
- `manage.py`: Django management script

## Contributing

Feel free to fork the repository and submit pull requests for any improvements.

## License

This project is open source and available under the MIT License.
