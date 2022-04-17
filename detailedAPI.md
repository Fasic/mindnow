# Travelling Companion API
This is an api preview for the "Travelling Companion" app

## Version: v1

**Contact information:**  
wasicfilip@gmail.com  

### Security
**Basic**  

|basic|*Basic*|
|---|---|

### /accept_relationship/{id}/

#### GET
##### Description

accept_relationship, view for accepting relationship between users. Auth user must be recipient in relationship
and relationship must not be accepted.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /accept_trip/{id}/

#### GET
##### Description

accept_trip, view for accepting trip by called user. Auth user must be person in trip_request
and trip_request must not be accepted.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /accommodation/

#### GET
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [ [TripAccommodation](#tripaccommodation) ] |

#### POST
##### Description

Automatically add cost for Accommodation

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [TripAccommodation](#tripaccommodation) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [TripAccommodation](#tripaccommodation) |

### /accommodation/{id}/

#### GET
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this trip accommodation. | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [TripAccommodation](#tripaccommodation) |

#### PUT
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this trip accommodation. | Yes | integer |
| data | body |  | Yes | [TripAccommodation](#tripaccommodation) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [TripAccommodation](#tripaccommodation) |

#### PATCH
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this trip accommodation. | Yes | integer |
| data | body |  | Yes | [TripAccommodation](#tripaccommodation) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [TripAccommodation](#tripaccommodation) |

#### DELETE
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this trip accommodation. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 |  |

### /approve_trip/{id}/

#### GET
##### Description

approve_trip, view for approval of travel person by trip host. Auth user must be trip host
and trip_request must not be approved.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 |  |

### /auth/auth_token/

#### POST
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [AuthToken](#authtoken) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [AuthToken](#authtoken) |

### /auth/register/

#### POST
##### Description

Api view for registration, permission required: None.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [Register](#register) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [Register](#register) |

### /auth/users/

#### GET
##### Description

Api view for listing all users, permission required: IsAdminUser.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [ [User](#user) ] |

#### POST
##### Description

Api view for listing all users, permission required: IsAdminUser.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [User](#user) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [User](#user) |

### /cost/

#### GET
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [ [CostItem](#costitem) ] |

#### POST
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [CostItem](#costitem) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [CostItem](#costitem) |

### /cost/{id}/

#### GET
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this cost item. | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [CostItem](#costitem) |

#### PUT
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this cost item. | Yes | integer |
| data | body |  | Yes | [CostItem](#costitem) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [CostItem](#costitem) |

#### PATCH
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this cost item. | Yes | integer |
| data | body |  | Yes | [CostItem](#costitem) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [CostItem](#costitem) |

#### DELETE
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this cost item. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 |  |

### /flight/

#### GET
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [ [Flight](#flight) ] |

#### POST
##### Description

Automatically add CostItem for Flight

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [Flight](#flight) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [Flight](#flight) |

### /flight/{id}/

#### GET
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this flight. | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Flight](#flight) |

#### PUT
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this flight. | Yes | integer |
| data | body |  | Yes | [Flight](#flight) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Flight](#flight) |

#### PATCH
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this flight. | Yes | integer |
| data | body |  | Yes | [Flight](#flight) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Flight](#flight) |

#### DELETE
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this flight. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 |  |

### /location/

#### GET
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [ [Location](#location) ] |

#### POST
##### Description

Add created_by as current user.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [Location](#location) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [Location](#location) |

### /location/{id}/

#### GET
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this location. | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Location](#location) |

#### PUT
##### Description

Add created_by as current user.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this location. | Yes | integer |
| data | body |  | Yes | [Location](#location) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Location](#location) |

#### PATCH
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this location. | Yes | integer |
| data | body |  | Yes | [Location](#location) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Location](#location) |

#### DELETE
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this location. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 |  |

### /passport/

#### GET
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [ [Passport](#passport) ] |

### /passport/create/{id}/

#### POST
##### Description

Add created_by as current user.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path |  | Yes | string |
| data | body |  | Yes | [Passport](#passport) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [Passport](#passport) |

### /passport/{id}/

#### GET
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this passport. | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Passport](#passport) |

#### PUT
##### Description

Add created_by as current user.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this passport. | Yes | integer |
| data | body |  | Yes | [Passport](#passport) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Passport](#passport) |

#### PATCH
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this passport. | Yes | integer |
| data | body |  | Yes | [Passport](#passport) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Passport](#passport) |

#### DELETE
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this passport. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 |  |

### /person/

#### GET
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [ [Person](#person) ] |

#### POST
##### Description

Add created_by as current user.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [Person](#person) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [Person](#person) |

### /person/{id}/

#### GET
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this person. | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Person](#person) |

#### PUT
##### Description

Add created_by as current user.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this person. | Yes | integer |
| data | body |  | Yes | [Person](#person) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Person](#person) |

#### PATCH
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this person. | Yes | integer |
| data | body |  | Yes | [Person](#person) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Person](#person) |

#### DELETE
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this person. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 |  |

### /relationships/

#### GET
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [ [Relationships](#relationships) ] |

#### POST
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [Relationships](#relationships) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [Relationships](#relationships) |

### /relationships/{id}/

#### GET
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this user relationships. | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Relationships](#relationships) |

#### PUT
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this user relationships. | Yes | integer |
| data | body |  | Yes | [Relationships](#relationships) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Relationships](#relationships) |

#### PATCH
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this user relationships. | Yes | integer |
| data | body |  | Yes | [Relationships](#relationships) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Relationships](#relationships) |

#### DELETE
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this user relationships. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 |  |

### /trip/

#### GET
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [ [Trip](#trip) ] |

#### POST
##### Description

Add created_by as current user.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [Trip](#trip) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [Trip](#trip) |

### /trip/{id}/

#### GET
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this trip. | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Trip](#trip) |

#### PUT
##### Description

Add created_by as current user.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this trip. | Yes | integer |
| data | body |  | Yes | [Trip](#trip) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Trip](#trip) |

#### PATCH
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this trip. | Yes | integer |
| data | body |  | Yes | [Trip](#trip) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Trip](#trip) |

#### DELETE
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this trip. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 |  |

### /trip_persons/

#### GET
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [ [TripPerson](#tripperson) ] |

#### POST
##### Description

Create trip_person object, for trip and person, and update accepted/approved values
depending on the person and trip host.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [TripPerson](#tripperson) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [TripPerson](#tripperson) |

### /trip_persons/{id}/

#### GET
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this trip person. | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [TripPerson](#tripperson) |

#### PUT
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this trip person. | Yes | integer |
| data | body |  | Yes | [TripPerson](#tripperson) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [TripPerson](#tripperson) |

#### PATCH
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this trip person. | Yes | integer |
| data | body |  | Yes | [TripPerson](#tripperson) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [TripPerson](#tripperson) |

#### DELETE
##### Description

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this trip person. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 |  |

### Models

#### TripAccommodation

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer |  | No |
| from_date | date |  | Yes |
| to_date | date |  | Yes |
| trip | integer |  | Yes |
| location | integer |  | No |
| cost | integer |  | No |

#### AuthToken

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| username | string |  | Yes |
| password | string |  | Yes |
| token | string |  | No |

#### Register

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| username | string | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | Yes |
| password | string |  | Yes |
| password2 | string |  | Yes |
| email | string (email) |  | Yes |
| first_name | string |  | Yes |
| last_name | string |  | Yes |

#### User

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer |  | No |
| last_login | dateTime |  | No |
| is_superuser | boolean | Designates that this user has all permissions without explicitly assigning them. | No |
| username | string | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | Yes |
| first_name | string |  | No |
| last_name | string |  | No |
| email | string (email) |  | No |
| is_staff | boolean | Designates whether the user can log into this admin site. | No |
| is_active | boolean | Designates whether this user should be treated as active. Unselect this instead of deleting accounts. | No |
| date_joined | dateTime |  | No |
| groups | [ integer ] | The groups this user belongs to. A user will get all permissions granted to each of their groups. | No |
| user_permissions | [ integer ] | Specific permissions for this user. | No |

#### CostItem

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer |  | No |
| description | string |  | No |
| price | string (decimal) |  | Yes |
| trip | integer |  | Yes |

#### Flight

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer |  | No |
| flight_number | string |  | Yes |
| confirmation_code | string |  | Yes |
| flight_time | dateTime |  | Yes |
| checked | boolean |  | No |
| trip | integer |  | Yes |
| from_dest | integer |  | No |
| to_dest | integer |  | No |
| cost | integer |  | No |

#### Location

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer |  | No |
| name | string |  | Yes |
| created_by | integer |  | Yes |

#### Passport

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer |  | No |
| passport_number | string |  | Yes |
| date_issued | date |  | Yes |
| valid_until | date |  | Yes |
| created_by | integer |  | Yes |

#### Person

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer |  | No |
| first_name | string |  | Yes |
| last_name | string |  | Yes |
| created_by | integer |  | Yes |
| user | integer |  | No |
| passport | integer |  | No |

#### Relationships

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer |  | No |
| request_time | dateTime |  | No |
| accepted | boolean |  | No |
| user1 | integer |  | Yes |
| user2 | integer |  | Yes |

#### Trip

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer |  | No |
| description | string |  | No |
| from_date | date |  | Yes |
| to_date | date |  | Yes |
| budget | number |  | No |
| created_by | integer |  | Yes |
| trip_location | [ integer ] |  | No |

#### TripPerson

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer |  | No |
| accepted | boolean |  | No |
| approved | boolean |  | No |
| trip | integer |  | Yes |
| person | integer |  | Yes |
