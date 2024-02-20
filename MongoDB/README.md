### Traditional DB - Sql database

MySQL
PostgreSQL
Oracle Database
Microsoft SQL Server
SQLite


### Mongo DB - NoSql Database
Not-only-Sql

-  data in collections of JSON-like documents. Each document can have a different structure, and fields within documents can vary. 
- optimized for querying JSON-like documents. It supports a wide range of operations such as filtering, sorting, and aggregation.
-  MongoDB does not enforce a strict schema. You can add or remove fields to documents on the fly, without affecting other documents in the collection.

what is collections ?
- a collection is a grouping of MongoDB documents

Try basic CREAD operation for basic understanding

**Usage**

docker compose -f docker-compose.yml up

#Get inside client container and do basic operations
docker exec -it 97f2856d7ac3 bash 

- python insert.py
- python read.py
- python edit.py
- python delete.py

