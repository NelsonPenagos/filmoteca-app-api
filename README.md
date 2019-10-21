# filmoteca-app-api

Endpoint | HTTP Method	| Result
------------ | -------------|------------ | 
http://localhost:8000/api/v1/login/ | POST | Login user
http://localhost:8000/api/v1/logout/ | POST | Logout user
http://localhost:8000/api/v1/register/ | POST | Register user
http://localhost:8000/api/v1/movie/ | POST | Get all movies
http://localhost:8000/api/v1/movie/:id | GET | Get a single movie 
http://localhost:8000/api/v1/movie/:id | PUT | Update a single movie
http://localhost:8000/api/v1/movie/:id | DELETE | Update a single movie
http://localhost:8000/api/v1/movie/name/:name | GET | Get a single movie for name
http://localhost:8000/api/v1/movie/genre/:genre | GET | Get a single movie for genre
http://localhost:8000/api/v1/movie/director/:director/ | GET | Get a single movie for director
http://localhost:8000/api/v1/movie/recomendation | GET | Get all recomendation
