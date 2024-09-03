# About the API 

## Purpose 
This API works to provide CRUD functionality between the relational tables of message TEMPLATES and personalized NOTIFICATIONS


## Getting Started
This project leverages the ease and simplicity of Flask as its framework, and the dynamic ability of Python as it's programming language
(NOTE: this is not a deployed project which means it will only be accessible via a localhost server)

First you will want to insure you have Python installed locally on your personal machine. If you need any guidance you can click [here](https://www.python.org/downloads/) for support

Next, upon opening the project we'll want to install the necessary dependencies in the requirements.txt file by running the command pip install -r requirements.txt

Once requirements are installed, to test the endpoints you can use the VS Code extension, Thunder Client, to see and test the functionality of the endpoints

### Running the Test Suite

To run the test suite, execute the following command:

`python create_db.py` 
`python -m pytest tests`

All tests should be passing (9/9)

### Running the Server

To run the server, execute the following command:

`python api.py`


## Models
- Template 
- Notification
* Unless indicated, all fields are NOT nullable

### Template
A Template will have fields for ID and Body

- id: integer, primary key 
- body: string 

### Notification
A Notification will have fields for ID, Phone number, Personalization, and Template ID 

- id: integer, primary key

- phone_number: string

- template_id: integer, foreign key to Template 

- personalization: string, nullable

NOTE: A request of GET /api/notification/{id} will return a Notification with a special field, CONTENT, which is the value of it's associated Template (Template.body) interpolated the place of "(personal)" from it's own value (Notification.personalization) 

EXAMPLE: 
- Notification "personalization" = "Blake"
- Template "body" = "Good morning, (personal). Ready for your appointment today, (personal)?"
- GET /notification/:id response "content" attribute = "Good morning, Blake. Ready for your appointment today, Blake?"


## Database
This API leverages a SQLite relational database, and a couple different libraries (see Requirements), to utilize the ease of built-in querying methods of an ORM (Object-Relational Mapper) to lean into object-oriented programming   


## Endpoints

### - Notification
GET /notification 
Status Code: 200 
Returns a list of Notifications 

GET /notification/:id 
Status Code: 200 
Returns a given Notification, and includes the "content" field (see Notification Model)

POST /notification 
Status Code: 201 
Creates a new Notification 

DELETE /notification/:id
Status Code: 200
Deletes a given Notification

### - Template
GET /template
Status Code: 200 
Returns a list of Templates

GET /template/:id
Status Code: 200 
Returns a given Template

POST /template 
Status Code: 201 
Creates a new Template |

PATCH /template/:id 
Status Code: 200 
Updates a given Template

DELETE /template/:id
Status Code: 200
Deletes a given Template


## NOTE: 
At this time app.run() in 'api.py' sets debug equal to FALSE for a production-ready environment. While there is a security risk to setting debug=True, here are a couple benefits to setting True for Development:

- Error display, detailed error-message outputs
- Automatic code reloading, no need for restarting server 
