Evacuation_plan backend
===============

evacuation_plan backend

1. Create a new virtual environment and activate it
2. From the backend folder, run pip install -r requirements.txt
3. Run python manage.py syncdb
  1. Say "no" when it asks if you want to create a super user
4. Run python manage.py migrate
5. Run python manage.py createsuperuser
