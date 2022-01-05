Demo Pipeline
=============
the goal of this demo is to create a data pipeline for two data file (Reservation , location)
The focus of this demo is on connectivity / scalability / performance
In this project I used these technologies:


* `celery`==`5.0.2`
* `Django`==`3.1.3`
* `git+git://github.com/thepylot/djongo.git#egg=djongo
* `mongoengine`==`0.20.0`
* `pylint-mongoengine`==`0.4.0`
* `pymongo`==`3.11.0`
* `psycopg2-binary`==`2.8.5`
* `redis`==3.5.3
* `Faker`
* `djangorestframework`
* `djangorestframework-csv`
 
Run
-----------
Run the project with docker

```bash

docker-compose run app /bin/bash -c "python manage.py createsuperuser"
docker-compose up

```
after this you will have to add user + email + password then you will have to write : 
```bash
docker-compose up
``` 

Admin page to view the data
-----------
```bash
http://localhost:8000/admin
```

After this, you can load the reservation and location data into the databases. 
 
For loading the location | reservation data
-----------
```bash
 docker-compose run app /bin/bash -c "python manage.py load_locations /datasets/assignment_locations.csv"
 docker-compose run app /bin/bash -c "python manage.py load_reservations /datasets/assignment_reservations.csv"
```

This part is where I was focusing the scalability function, because it uses celery.
Currently there is only 1node for celery so it might take longer to load. If needed we can add 10 nodes so the celery which handles the tasks will be faster.


Retrieving the data
-----------
We can now retrieve the data from two databases (postgres, mongo) in both Json and CSV format


Data URLs
-----------
```bash
http://localhost:8000/core/locations.json
http://localhost:8000/core/locations.csv

http://localhost:8000/core/locations-nonrel.json
http://localhost:8000/core/locations-nonrel.csv

http://localhost:8000/core/reservations.json
http://localhost:8000/core/reservations.csv

http://localhost:8000/core/reservations-nonrel.json
http://localhost:8000/core/reservations-nonrel.csv
``` 



Test case
-----------
you can see the test case I've created in app/core/test.py 



