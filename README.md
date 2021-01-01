# CRUD-operations-on-a-file-based-key-value-data-store
- Here we have built a file based key value data store which supports basic CRUD operations as well as multi threading. 
- This data store is meant to be used as a local storage for one single process on one laptop. 
- The data store must be exposed as a library to clients that can instantiate a class and work with the data store. <br/><br/>

**CRUD** is an acronym that comes from the world of computer programming and refers to the four functions that are considered necessary to implement a persistent storage application: 
1. Create
2. Read
3. Update
4. Delete

## Functional requirements supported by the data store
1. It can be initialized using an optional file path. If one is not provided, it will reliably create itself in a reasonable location on the laptop.
2. A new key-value pair can be added to the data store using the Create operation. The key is always a string - capped at 32chars. The value is always a JSON object - capped at 16KB.
3. If Create is invoked for an existing key, an appropriate error must be returned.
4. A Read operation on a key can be performed by providing the key, and receiving the value in response, as a JSON object.
5. A Delete operation can be performed by providing the key.
6 Every key supports setting a Time-To-Live property when it is created. This property is optional. If provided, it will be evaluated as an integer defining the number of seconds the key must be retained in the data store. Once the Time-To-Live for a key has expired, the key will no longer be available for Read or Delete operations.
7. Appropriate error responses must always be returned to a client if it uses the data store in unexpected ways or breaches any limits.

## Non-functional requirements supported by the data store
1. The size of the file storing data must never exceed 1GB.
2. More than one client process cannot be allowed to use the same file as a data store at any given time.
3. A client process is allowed to access the data store using multiple threads, if it desires to. The data store must therefore be thread-safe.
4. The client will bear as little memory costs as possible to use this data store, while deriving maximum performance with respect to response times for accessing the data store.

## Understanding the repository
This repository consists of 4 main files:

**1. dataStore.py**
- This file is the gist of our repository.
- It contains code which imports all the required functionalities, functions to perform CRUD operations.

**2. exceptions.py**
- This file consists of some exceptions which might occur inadvertently or by the user.
- This file is imported as a custom functionality to the `dataStore.py` file.

**3. db.json**
- This is the database or data store created using the `dataStore.py` file.
- You can name it anything of your choice but I went for db.
- It will contain all the data created, updated and deleted by the user in JSON format.

**4. unit_test.ipynb**
- This iPython notebook consists of several unit tests performed on the `db.json` file.
- We have imported `dataStore.py` file as a custom functionality to perform unit tests of CRUD operations, exceptions and multi-threading properties on the database.

## Scope for improvement
While our project supports basic CRUD operations and multi threading, still there are lot of things which can be added so as to improve the usability of the data store.

These are:
1. Although while performing the Read operation, the data associated with that particular key value is displayed but if the user wants to display all the records of the database then we can have an additional function which can be used to display all the data stored in the database.

2. If the user wants to drop / delete the whole database then a function can be created to delete the entire database.

3. I have used an iPython notebook to perform unit tests because it gives us the liberty to run our code and get the output right there and if it contains some bugs, it allows us to rectify them then and there as well. But these unit tests can also be perfomed inside a terminal using command line arguments. For this the user can create an additional file which would specify the number and type of arguments to invoke the `dataStore.py` file and to perform specific operations.
