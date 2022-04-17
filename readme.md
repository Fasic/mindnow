# MindNow Travelling Companion APP

Project name: mindnow

- For running application using docker, run: `docker-compose up` from root directory.
- Everything is initially set up, if desire is an empty DB run: `python manage.py flush`

Initial DB setting has two users: 
- `Username: Admin, password: admin12345` superuser for admin portal.
- `Username: User, password: user12345` normal user with some initiall data.


### Modules

| Module | Description                                      | url|
|--------|--------------------------------------------------|----|
| mind_auth  | module for authentication, no models, only views | url: 'http://<BASE_URL>/auth/...'| 
| rest_api  | module for API part of app, no models            | url: 'http://<BASE_URL>/api/...'| 
| travelling_companion  | main module, with models and WEB part of app     | url: 'http://<BASE_URL>/...'| 

### Implemented Features

- Registration and Login
- Trips, *Add, Edit, Delete*
- Location (City), *Add, Edit, Delete*
- Person (NonUser, can't login to APP), *Add, Edit, Delete*
- Adding persons to trip, with the possibility of **approval** and **acceptance**
- Adding Cost to trip, *Add, Edit, Delete*
- Adding Flights to trip, *Add, Edit, Delete*
- Adding Accommodations to trip, *Add, Edit, Delete*
- All permissions **DONE**
- Some of validations **DONE**

### Todo *features*:

- Making "UserRelationships" model work, for filtering users-persons you can add to Trip.
- More validations
- City (location) get data from public API
- Model/table for Trip locations, with date from-to, precise plan of trip, may use geo map.
- Accommodations (Booking) and Flights to work with external API to get data about reservations

## APP End points

    APP defines endpoints user can visit/call:
        admin/ - urls for admin portal
        api/ - API urls, for rest_api module
        auth/ - AUTH urls, for registration and login, mind_auth module
        default path '' - WEB urls for django template based WEB part of app, Home page (overview of trips)
    
        SWAGGER URL-s:
            /swagger/ - UI based documentation of API end points
            /swagger.json - file with json format of API end points
            /swagger.yaml - file with yaml format of API end points

- [Detailed description of API Endpoints](detailedAPI.md)

- [Or visit (swagger documentation)](http://127.0.0.1/swagger)

Short list API Endpoints:

- Unprotectad URL-s
    - api/auth/auth_token/ - login
    - api/auth/register/ - register
- Protectad URL-s
    - api/auth/users/ - get all users
    - api/trip/
    - api/trip/<int:pk>/
    - api/location/
    - api/location/<int:pk>/
    - api/person/
    - api/person/<int:pk>/
    - api/passport/
    - api/passport/<int:pk>/
    - api/passport/create/<int:id>/
    - api/trip_persons/
    - api/trip_persons/<int:pk>/
    - api/relationships/
    - api/relationships/<int:pk>/
    - api/flight/
    - api/flight/<int:pk>/
    - api/accommodation/
    - api/accommodation/<int:pk>/
    - api/cost/
    - api/cost/<int:pk>/
    - api/accept_relationship/<int:pk>/
    - api/accept_trip/<int:pk>/
    - api/ approve_trip/<int:pk>/

