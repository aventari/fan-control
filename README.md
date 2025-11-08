# fan-control
Go program to control fan
Create the Virtual Environment

Instead of installing flask globally, create a self-contained environment just for this project. The common name for this is venv.
Bash

python3 -m venv venv

You'll see a new folder named venv appear.

2. Activate the Environment

You must "activate" this environment in your shell session.
Bash

source venv/bin/activate

Your command prompt will change to show (venv) at the beginning, letting you know it's active.

(venv) activ@activpi5:~/fan-control $

3. Install Flask (Inside the venv)

Now you can install flask safely without using sudo. It will be installed only inside your venv folder, leaving the system Python untouched.
Bash

pip install flask

4. Run Your App

With the environment still active, run your app as before:
Bash

python app.py

How to Stop

When you are finished working on the project and want to leave the virtual environment, just type:
Bash

deactivate


---
How to Run in Production

You must use a production WSGI server. The most popular one for this is Gunicorn.

Step 1: Activate Your Environment Make sure you are in your project folder and the virtual environment is active.
Bash

source venv/bin/activate

(Your prompt should show (venv))

Step 2: Install Gunicorn Install it into your virtual environment, just like you did with Flask.
Bash

pip install gunicorn

Step 3: Run With Gunicorn Instead of python app.py, you will now run it like this:
Bash

gunicorn --bind 0.0.0.0:5000 web-app:app

    --bind 0.0.0.0:5000: Tells Gunicorn to listen on port 5000 on all network interfaces.

    app:app: This means "in the file named app.py, find the Flask variable named app."

This is more stable and secure, but it is still not enough.
