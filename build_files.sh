env/scripts/activate

# Install required packages
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic 

# Apply database migrations
python manage.py migrate

# Start the Django development server or your preferred deployment method
python manage.py runserver