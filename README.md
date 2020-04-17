[![Build Status](https://travis-ci.com/hangry-ateball/hangry-ateball-be.svg?branch=master)](https://travis-ci.com/hangry-ateball/hangry-ateball-be)

# Hangry-Ateball-BE
![](https://im4.ezgif.com/tmp/ezgif-4-a30855586948.gif)</br>
You are on your lunch break.  You've already eaten Chipotle 3 times this week.  You and your group of friends decide that it's time to change it up.  Everyone is "down for anything" but nobody can make a concrete decision.  That's when you whip out your phone and open up Hangry Ateball.

This repo is for a [REST API] (https://hangry-ateball-api.herokuapp.com/) that consumes the Yelp and Google Maps API. It serves to return Restaurant information as a JSON object for our [Front End application](https://github.com/hangry-ateball/hangry-ateball-fe), where the restaurant information can be displayed to the User.

Hangry Ateball replicates the future-deciding 8 Ball by finding a nearby restaurant for you!  You can decide what kind of food (or leave it up to fate) as well as cost and if you want to walk or drive and the app will do the rest for you.  From the results screen, you can easily open maps to navigate to the restaurant or send the information to your friends via text with the click of a button.  It's munch time.  Where will you be?

### Contributors:
- Back End Team:
    - [Jonathan Patterson](https://github.com/Jonpatt92)
    - [Linda Le](https://github.com/linda-le1)
    - [Scott Regenthal](https://github.com/freeheeling)
- Front End Team:
    - [Caleb Haizlett](https://github.com/CHaiz15)
    - [Kim McCaskill](https://github.com/kimmccaskill)

## Tech Stack
- **Language:** Python 3.8.1
- **Framework:** Flask
- **Testing:** Pytest and Coverage (95.6% test coverage)
- **Deployment:** Heroku
- **APIs:** Yelp API, Google Geocoding API, and Google Places API
- **External Libraries:**
  - [Coverage](https://github.com/nedbat/coveragepy)
  - [Flask-CORS](https://github.com/corydolphin/flask-cors)
  - [Flask Swagger UI](https://github.com/swagger-api/swagger-ui)
  - [Gunicorn](https://github.com/benoitc/gunicorn)
  - [Marshmallow JSON API](https://github.com/marshmallow-code/marshmallow-jsonapi)
  - [Pytest](https://github.com/pytest-dev/pytest)
  - [Python DotEnv](https://github.com/theskumar/python-dotenv)
  - [Twilio](https://github.com/twilio/twilio-python)


### Available Endpoints (also available on [Swagger](https://hangry-ateball-api.herokuapp.com/api/docs/)):
- Endpoint `/api/v1/recommendations`
    - Returns restaurant recommendation based on user's preferences
    - Required params:
        - Note: If latitude and longitude are not available, address can be entered instead.
        -`latitude`, integer, i.e. 39.7392358
        -`longitude`, integer, i.e. -104.990251
    - Optional params:
        - `categories`, string (can be a comma delimited list), i.e. Chinese
        - `price`, maximum price point, integer between 1 and 4, i.e. 3 (will also search for restaurants with price point of 2 and 1)
        - `address`, use only if latitude and longitude not submitted, string, i.e. 1331 17th St LL100, Denver, CO or Denver, CO
    - Response Example:
        <img alt="homepage screenshot" width="90%" src="https://user-images.githubusercontent.com/54052410/79527223-43080b00-8024-11ea-8314-3a4dfa9d6625.png" />
- Endpoint `/api/v1/random`
    - Returns random restaurant recommendation
    - Required params:
        -`latitude`, integer, i.e. 39.7392358
        -`longitude`, integer, i.e. -104.990251
    - Optional params:
        - `address`, use only if latitude and longitude not submitted, string, i.e. 1331 17th St LL100, Denver, CO or Denver, CO
    - Response Example:
            <img alt="homepage screenshot" width="90%" src="https://user-images.githubusercontent.com/54052410/79527228-44d1ce80-8024-11ea-8d9e-9d745b73c2bd.png" />
- Endpoint `/api/v1/notify`
    - Sends an SMS invitation to join a friend at a specified location.
    - Required params:
        - `to`, an SMS-enabled phone number to receive a notification, integer, i.e. 3031234567
        - `from`, a Twilio SMS-enabled phone number from which to send a notification,integer
        - `body`, provide an establishment name and address to be appended to the SMS notifcation, string

### Learning Goals:
- Ultimately, demonstrate knowledge we have gained throughout Turing.
- Learn and implement a new language: Python.
- Learn and implement a new testing environment: Pytest.
- Work closely with a front-end team to create a synchronous application.
- Use an agile process to turn well defined requirements into deployed and production ready software.
- Gain experience dividing applications into components and domains of responsibilities to facilitate multi-developer teams.
- Explore and implement new concepts, patterns, or libraries that have not been explicitly taught while at Turing.
- Practice an advanced, professional git workflow.
- Gain more experience using continuous integration tools to build and automate the deployment of features in various environments.
- Build applications that execute in development, test, CI, and production environments.
- Focus on communication between front-end and back-end teams in order to complete and deploy features that have been outlined by the project spec.

#### Wins:

- Achieved MVP with extensions before deadline.
- Successful workflow and communication between FE and BE teams.
- We made an app we would actually use!
- Great testing coverage for backend.
<img alt="homepage screenshot" width="90%" src="https://user-images.githubusercontent.com/54052410/79527232-48fdec00-8024-11ea-8b53-725b88b77dc0.png" />

#### Challenges
- Learning Python and Flask.
- Using new testing framework, Pytest and other new technologies/tools like Twilio, and Swagger.
- COVID-19 impacts including remote work and affecting live restaurant data.

### Hangry Ateball Application Screenshots

#### Homepage:
<img alt="homepage screenshot" width="40%" src="https://user-images.githubusercontent.com/19761687/79509423-b6942300-7ff8-11ea-90c1-f63d1679141b.png" />

#### Form:
<img alt="homepage screenshot" width="40%" src="https://user-images.githubusercontent.com/19761687/79509429-b85de680-7ff8-11ea-896d-e0ce004570c6.png" />

#### Result:
<img alt="homepage screenshot" width="40%" src="https://user-images.githubusercontent.com/19761687/79509432-b98f1380-7ff8-11ea-8716-325d9c96ab65.png" />
