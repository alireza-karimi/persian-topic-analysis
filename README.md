# Persian Topic Analysis Web Service

## Requirements
1.create a virtual environment in your directory  
2.install all packages in requirements.txt  
```bash
pip install -r requirements.txt
```

## ORM
We have used sqlite relational database for the api. Besides, SQLAlchemy object-relational mapper (ORM) helps us work with database easily.

## Checking Database
You can use sqlitebrowser.org to see your database graphically

## API Endpoints
| Endpoint  | Method | Parameters | Info                                                          |
|-----------|--------|------------|---------------------------------------------------------------|
| /predict  | GET    | text       | predicting category of a text                                 |
| /articles | GET    |            | getting all articles and their category available in database |
