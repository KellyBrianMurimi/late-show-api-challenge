# late-show-api-challenge
A Flask REST API for managing a late night TV show system with guests, episodes, and appearances.

## Features

- User authentication with JWT
- CRUD operations for guests, episodes, and appearances
- PostgreSQL database
- RESTful endpoints
- Token-based authentication for protected routes

## Requirements

- Python 3.8+
- PostgreSQL
- pipenv 

🗂 Suggested Folder Structure
.
├── server/
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── guest.py
│   │   ├── episode.py
│   │   ├── appearance.py
│   │   └── user.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── guest_controller.py
│   │   ├── episode_controller.py
│   │   ├── appearance_controller.py
│   │   └── auth_controller.py
├── migrations/
├── challenge-4-lateshow.postman_collection.json
└── README.md
 
💻 GitHub Repository Setup
✅ Create a new repo:
👉 github.comLinks to an external site. → New repo → late-show-api-challenge → No README/.gitignore


✅ Initialize + push:

git init git remote add origin https://github.com/<username>/late-show-api-challenge.git git add . git commit -m "Initial commit" git branch -M main git push -u origin main

✅ .gitignore example:


__pycache__/
*.pyc
*.db
.env
*.sqlite3
migrations/
Pipfile.lock

## Setup
✅ Install dependencies:
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary pipenv shell

✅ PostgreSQL DB setup

Create your database in Postgres:
CREATE DATABASE late_show_db;

✅ Set your DATABASE_URI in server/config.py
SQLALCHEMY_DATABASE_URI = "postgresql://<user>:<password>@localhost:5432/late_show_db"

✅ Run DB setup
export FLASK_APP=server/app.py 
flask db init 
flask db migrate -m "initial migration" 
flask db upgrade 
python server/seed.py

# Create a .env file:
bash
echo "DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/late_show_db" > .env
echo "JWT_SECRET_KEY=your-super-secret-key" >> .env
echo "FLASK_APP=server.app" >> .env
echo "FLASK_ENV=development" >> .env

Run the server:
$ export FLASK_APP=server.app
$ flask run --port 5555
## Importing the Postman Collection
Open Postman
Click "Import" in the top-left
Select your challenge-4-lateshow.postman_collection.json file
The collection should appear in your sidebar

## Testing the Authentication Flow
# Register a New User
Select the "Register" request in Postman
Set method to POST
Set URL to http://localhost:5555/register
Go to the "Body" tab, select "raw" and "JSON"
Enter test data:

json
{
    "username": "testuser",
    "password": "testpass123"
}
Click "Send"

Verify you get a 201 Created response

# Login to Get Token
Select the "Login" request
Set method to POST
Set URL to http://localhost:5555/login
Use the same credentials in the body:

json
{
    "username": "testuser",
    "password": "testpass123"
}
Click "Send"

Copy the access_token from the response (you'll need this for protected routes)

# Testing Protected Routes
Set Up Authorization
In Postman, click on your collection name
Go to the "Authorization" tab
Select "Bearer Token" as Type
Paste your copied token in the Token field

This will apply to all requests in the collection

 ## Testing Public Routes
Get All Episodes (GET /episodes)

# Select the "Get All Episodes" request

Set method to GET
Set URL to http://localhost:5555/episodes
Click "Send"

Verify 200 OK with episode list

# Get Single Episode (GET /episodes/:id)

Select the "Get Single Episode" request
Set method to GET
Set URL to http://localhost:5555/episodes/1 (use existing ID)
Click "Send"

Verify 200 OK with episode details

# Get All Guests (GET /guests)

Select the "Get All Guests" request
Set method to GET
Set URL to http://localhost:5555/guests

Click "Send"

Verify 200 OK with guest list

# Delete Episode (DELETE /episodes/:id)

Select the "Delete Episode" request
Set method to DELETE
Set URL to http://localhost:5555/episodes/1 (use an existing episode ID)

Click "Send"

Verify 200 OK response

## Test Protected Endpoints
Create Appearance (POST /appearances)
Select the "Create Appearance" request
Set method to POST
Set URL to http://localhost:5555/appearances

Add JSON body:

json
{
    "rating": 4,
    "guest_id": 1,
    "episode_id": 1
}
Click "Send"

Verify 201 Created response

## Technologies used
1.Python3.8
2.Flask
3.PostgreSQL

## License
Copyright <2025> <Kelly Brian>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

