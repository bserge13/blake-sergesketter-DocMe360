# About the API 

## Purpose 
This API works to provide CRUD functionality between the relational tables of message TEMPLATES and personalized NOTIFICATIONS


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

NOTE: A request of GET /api/notification/{id} will return a Notification with a special field, CONTENT, that has the value of it's parent association (Template.body) and interpolating-in the place of "(personal)" it's own value (Notification.personalization) 

## Endpoints

REQ: Please implement the following endpoints. All endpoints should return JSON and set the _Content-Type_ response header appropriately. The response body should be the affected record(s).
ANSWER: It is implicitly handled by Flask_restful automatically setting the '_Content-Type_' to 'application/json' when returning via the 'marshal_with' decorator

### - Notification
| GET /notification | 200 | Return a list of Notifications |

| GET /notification/:id | 200 | Return a given Notification. Includes "content" field (below). |

| POST /notification | 201 | Create a new Notification |
### - Template
| GET /template | 200 | Return a list of Templates |

| GET /template/:id | 200 | Return a given Template |

| POST /template | 201 | Create a new Template |

| PATCH /template/:id | 200 | Update a given template. Select the HTTP method appropriately. |


HTTP response JSON for the endpoint `GET /notification/:id`, and only this endpoint, should include the additional string field "content" that has the value of Template.body where all instances in Template.body of the string "(personal)" are replaced by the value of Notification.personalization.

Example:

Notification "personalization" = "Bob"

Template "body" = "Hello, (peronsal). How are you today, (personal)?"

GET /notification/:id response "content" attribute = "Hello, Bob. How are you today, Bob?"

## Additional Requirements

- Include a README that describes how to run your application, any design decisions worth discussing, and any assumptions you made.

- Include a requirements.txt file

- All routes should have associated unit tests written with Pytest



## Requirements.txt
- requirements.txt contains all the necessary dependencies needed to be installed per this project