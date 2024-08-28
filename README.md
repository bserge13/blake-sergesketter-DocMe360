## Models

Set reasonable values for maximum string lengths. All fields are not null unless otherwise indicated.

### Notification

| Column | Type |

|-----------------|-------------------------|

| id | integer primary key |

| phone_number | string |

| template_id | foreign key to Template |

| personalization | nullable string |

### Template

| Column | Type |

|--------|---------------------|

| id | integer primary key |

| body | string |

## Endpoints

Please implement the following endpoints. All endpoints should return JSON and set the _Content-Type_ response header appropriately. The response body should be the affected record(s).

| Endpoint | Expected Status Code | Expected Behavior |

|-----------------------|----------------------|-----------------------------------------------------------------|

| GET /notification | 200 | Return a list of Notifications |

| GET /notification/:id | 200 | Return a given Notification. Includes "content" field (below). |

| POST /notification | 201 | Create a new Notification |

| GET /template | 200 | Return a list of Templates |

| GET /template/:id | 200 | Return a given Template |

| POST /template | 201 | Create a new Template |

| xxxx /template/:id | 200 | Update a given template. Select the HTTP method appropriately. |

### GET /notification/:id Content Field

HTTP response JSON for the endpoint `GET /notification/:id`, and only this endpoint, should include the additional string field "content" that has the value of Template.body where all instances in Template.body of the string "(personal)" are replaced by the value of Notification.personalization.

Example:

Notification "personalization" = "Bob"

Template "body" = "Hello, (peronsal). How are you today, (personal)?"

GET /notification/:id response "content" attribute = "Hello, Bob. How are you today, Bob?"

## Additional Requirements

- Include a README that describes how to run your application, any design decisions worth discussing, and any assumptions you made.

- Include a requirements.txt file

- All routes should have associated unit tests written with Pytest