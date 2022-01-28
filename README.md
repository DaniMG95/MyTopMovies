# Take Home Project

You are the developer in charge of creating a web application to admin a Movie database 
for a video streaming service. You'll need to implement the API that performs CRUD operations on the 
contents and a simple frontend to manage the movies in the platform.

This API will provide endpoints for adding new movies in the platform, querying
existing ones, adding new actors, querying them, and additional endpoints showing movies
that some actors have made together, and common actors that appear in the requested movies.

The API is developed with FastApi ant Frontend use React.

## Install and launch the server

### API

For the database we have used a mysql docker which stored the data in volume and create database, passing the commands launched for its creation.

```
docker volume create db
docker run --name db_project -v db:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=test -p 3302:3306 -d mysql
docker exec -it db_project bash
mysql --host=localhost --user=root --password=test
create database test;
```

If you have the docker created and you want to launch it you must put the following

```
docker start db_project
```


You must also create an .env file with the environment variables with the database server configuration as shown in the .env.example.
Here is an example of the .env
```
DATABASE=test
USER=root
PASSWORD=test
HOST=localhost
PORT=3302
```


To launch the application it is necessary to have python3 installed and launch the following steps.

```
cd backend
pip install -r requirements
uvicorn server:app
```

You can view the API documentation at the following [http://localhost:8000/docs](http://localhost:8000/docs). 

### FRONTEND

To launch the application it is necessary to have node installed and launch the following steps.

```
cd frontend
npm install
npm start
```


## API endpoints

### add new movies
```
POST /movies
{
    "title": string,
    "category": string,
    "cast": Array<string>
}

return
422 if the body is malformed
400 if movie's title already exists
400 if at least one of the actors in the cast is not registered
200 if correct

if the request is successful it should store the movie
```
### query all movies
```
GET /movies

return 
200
Array<{
    "title": string,
    "category": string,
    "cast": Array<string>
}> (list of movie titles)
```
### add new actor
```
POST /actors
{
    "name": string,
    "age": number,
    "gender": "male" | "female"
}

return
422 is the body is malformed
400 if the actor's name already exists
400 if the actor's gender is not "male" or "female"
200

if the request is succesful it should store the actor
```
### query all actors
```
GET /actors

return
200
Array<{
    "name": string,
    "age": number,
    "gender": "male" | "female"
} > (list of actors)
```
### get movies in which all the requested actors appear
```
GET /performances?actors=string,string,...

return
400 if at least one of the actors does not exist
400 if the 'actors' query parameter is not sent
200
Array<{
    "title": string,
    "category": string,
    "cast": Array<string>
}> (list of movies where all the actors in the query appear)
```
### get actors that appear in all the requested movies
```
GET /common_actors?movies=string,string,...

return
400 if at least one movie does not exist
400 if 'movies' query parameter does not exist
200
Array<{
    "name": string,
    "age": number,
    "gender": "male" | "female"
}> (list of actors that appear in all requested movies)
```

