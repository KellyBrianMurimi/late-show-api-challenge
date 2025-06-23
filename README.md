# late-show-api-challenge
1. Import the Postman Collection
Open Postman

Click "Import" in the top-left

Select your challenge-4-lateshow.postman_collection.json file

The collection should appear in your sidebar

2. Testing the Authentication Flow
Register a New User
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

Login to Get Token
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

3. Testing Protected Routes
Set Up Authorization
In Postman, click on your collection name

Go to the "Authorization" tab

Select "Bearer Token" as Type

Paste your copied token in the Token field

This will apply to all requests in the collection

Test Protected Endpoints
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

Delete Episode (DELETE /episodes/:id)

Select the "Delete Episode" request

Set method to DELETE

Set URL to http://localhost:5555/episodes/1 (use an existing episode ID)

Click "Send"

Verify 200 OK response

4. Testing Public Routes
Get All Episodes (GET /episodes)

Select the "Get All Episodes" request

Set method to GET

Set URL to http://localhost:5555/episodes

Click "Send"

Verify 200 OK with episode list

Get Single Episode (GET /episodes/:id)

Select the "Get Single Episode" request

Set method to GET

Set URL to http://localhost:5555/episodes/1 (use existing ID)

Click "Send"

Verify 200 OK with episode details

Get All Guests (GET /guests)

Select the "Get All Guests" request

Set method to GET

Set URL to http://localhost:5555/guests

Click "Send"

Verify 200 OK with guest list