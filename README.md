# Persian Topic Analysis Web Service

## Requirements
1.create a virtual environment in your directory  
2.install all packages in requirements.txt  
- Note: you can use `pipenv` for better dependency management:
```bash
pip install -r requirements.txt
or 
pipenv install
```

## dataset
put dataset.csv into `src/utils`


## Run server
first create a superuser for accessing django-admin and then run server
```
1. python3 manage.py migrate
2. python3 manage.py createsuperuser
3. python3 manage.py runserver
```


## API Endpoints
|      Endpoint      | Method | Parameters | Info                                                          |
|--------------------|--------|------------|---------------------------------------------------------------|
| /article/predict/  | POST   | text       | predicting category of a text                                 |
| /article/          | GET    |            | getting all articles and their category available in database |
