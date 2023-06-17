# Dental Clinic Patient Record and Appointment Schedule System
How to do it
1. Set up the Django project:
  - Install Django using pip: pip install django
  - Create a new Django project: django-admin startproject myproject
  - Navigate to the project directory: cd myproject

2.Set up the MySQL database:
  - Install the MySQL client for Python: pip install mysqlclient
  - Create a new MySQL database using a MySQL client of your choice.
  - Configure the Django settings:

Once you get that started, open settings. py
![image](https://github.com/shiroochan143/DRS/assets/108950973/24e063a2-fa56-4e5b-bc27-b704d63d1da3)

And then go to "Databases"
![image](https://github.com/shiroochan143/DRS/assets/108950973/b98e57c2-9639-4595-827b-83445ab144e0)
From there copy paste the 'Engine' value and at the same time, open your mysql client then create a database name of choice, and put it there.

3. Create django app:
   - Type "python manage.py startapp myapp"
   - You should have downloaded a bunch of files like forms, models, views, etc.
   - From there it's a matter of copy pasting the codes inside this repository.

4. Configuring the app:
   - Once you copy pasted the contents of "models.py" do this following steps
   - Type "python manage.py makemigrations"
   - Type "python manage.py migrate"
   - AT THAT SPECIFIC ORDER PLEASE!!!
   - After that copy paste everything else.
  
5. Running the app:
   - Type "python manage.py runserver"
   - then view "http://localhost:8000/{whatever url we have from urls}"
   - example "http://localhost:8000/dashboard/appointment-schedule/today
