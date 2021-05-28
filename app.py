from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import Column, Integer, String, Float
import os
from flask_marshmallow import Marshmallow
from SVMModel import SVMModel
import pandas as pd

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

#configing our database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'articles.db')
app.config['JSON_AS_ASCII'] = False

#defining the database
db = SQLAlchemy(app)
#building marshmallow for seriallizing purposes
ma = Marshmallow(app)

#creating svm model object
file_address = 'dataset.csv'
data = pd.read_csv(file_address, error_bad_lines = False, sep = ";")
data.columns = ['y', 'x']
svm_predictor = SVMModel(data=data)
svm_predictor.train_model()

# flask CLI 
@app.cli.command('db_create')
def db_create():
	db.create_all()
	print('Database created!')

@app.cli.command('db_drop')
def db_drop():
	db.drop_all()
	print('Databse dropped!')

@app.cli.command('db_seed')
def db_seed():
	############### nothing for now
	print('Database seeded!')

#######

@app.route('/predict')
def predict():
	#getting url parameter "text"
	text = request.args.get('text')
	category = str(svm_predictor.predict(text))
	article = Article(article_text=text, article_category=category)
	db.session.add(article)
	db.session.commit()
	return jsonify(category=category), 201


@app.route('/articles')
def articles():
	articles_list = Article.query.all()
	result = articles_schema.dump(articles_list)
	return jsonify(result)


########## database models
class Article(db.Model):
	__tablename__ = 'articles'
	article_id = Column(Integer, primary_key=True)
	article_text = Column(String)
	article_category = Column(String)

#classes for marshmallow
class ArticleSchema(ma.Schema):
	class Meta:
		fields = ('article_id', 'article_text', 'article_category')

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)

########

if __name__ == '__main__':
	app.run(debug=True)

