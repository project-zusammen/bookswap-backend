## Running the Application

Follow these steps to get this application set up on your computer:

1. Register an OAuth 2.0 application with Google and GitHub.
2. Clone the GitHub repository, create a Python virtualenv, and install all the dependencies:

```
cd flask-oauth-example
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Copy the .env.template file to .env and fill out your OAuth client ID and secrets from Google and GitHub.

Start the application:

`flask run`

On your browser, navigate to http://localhost:5000 and try the login buttons!
