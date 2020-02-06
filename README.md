## Model Based Restful Quart and Mongo DB
<p align="center">
  <img width="280" height="140" src="https://motor.readthedocs.io/en/stable/_images/motor.png">
</p>

### Note: API Integration with React [react-api-integration](https://github.com/mrxmamun/react-api-integration.git)
#### Model based restful quart (python) and asynchronous mongo db. Integrate with any API development.  

### Create [virtual environment]('https://docs.python.org/3/library/venv.html) and install requirements 
```sh
pip install -r requirements.txt
```
### Configure Database
#### From [config.py](src/config.py) configure datbase url, name, user and password 
```json
 {
   "db": {
            "url" : "mongodb://localhost:27017/",
            "name" :"db_name",  
            "user" :"",
            "password" :""
    }
 }
``` 

## In model update collection name and desire fields name and fields type. For example see todo [model](src/models/todo.py) file
#### From [model](src/models) folder write your individual model and configure db collection name, fields name and fields type
#### Example
##### In todo [model](src/models/todo.py) update collection name, fields name and fields type
```py
collection_name = 'todos'   # collection name
fields = {   
    "title"     : "string",
    "body"      : "string",
    "created"   : "datatime"
} 
```

##### Update required fields, optional fields from todo [model](src/models/todo.py)
```py
create_required_fields = []  # example create_required_fields = ["title", "body"]
create_optional_fields = []  # example create_required_fields = ["created"]
update_required_fields = []
update_optional_fields = []
```
#### Example 
```py
create_required_fields = ["title", "body"] 
create_optional_fields = []  
update_required_fields = ["title", "body"]
update_optional_fields = []
```
#### In [Database](src/factory/database.py) insert, find , find_by_id, update and delete methods are generalize methods.  
#### Those methods are call from [model](src/models) 
- `insert` method store data to database after confirm validation from model 
- `find` method retries all data from mongo database 
- `find_by_id` method retries back a single search data
- `update` method store updated data to database with corresponding id 
- and `delete` method delete data from database with corresponding id 

### Lets run the App
```sh
python app.py 
```
