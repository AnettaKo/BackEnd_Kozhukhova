My wardrobe
================

"My Wardrobe" is an application to record closes.

A user can work with wardrobe articles: add new one, change, delete articles.
The program use classificators and notes for quick input. The program contains
a user interface through the console. Data is stored in MongoDB database 
on https://cloud.mongodb.com. The database is accessed via API using FastAPI library.


Requirements:
--------

Python 3.11.

Install the packages specified in the file "requirements.txt".

Set up access to the MongoDB database in the [database.py](my_functions%2Fdatabase.py) module.


Usage:
-----------

1. Run "[main_backend.py](main_backend.py)" to start the API
2. Run [main_interface.py](main_interface.py) to start console interface. 

Testing:
-----------

Run [test.py](test.py) to start testing


