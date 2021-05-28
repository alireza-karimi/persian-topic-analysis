from SVMModel import SVMModel
import time
import pandas as pd

file_address = 'khabarfarsi_clf_dataset.csv'
data = pd.read_csv(file_address, error_bad_lines = False, sep = ";")
data.columns = ['y', 'x']
model = SVMModel(data)
print(model.model_acuraccy())

start = time.time()
for i in range(0, 500):
	model.predict(data.x[i])
print((time.time() - start) / 500)
##Result = 0.019


start = time.time()
for i in range(0, 500):
	model.normalize_and_predict(data.x[i])
print((time.time() - start) / 500)
##Result = 0.024

corrects = 0
for i in range(0, 500):
	prediction = model.predict(data.x[i])
	if(prediction == data.y[i]):
		corrects = corrects + 1
print(corrects * 100 / 500)
##Result = 99

corrects = 0
for i in range(0, 500):
	prediction = model.normalize_and_predict(data.x[i])
	if(prediction == data.y[i]):
		corrects = corrects + 1
print(corrects * 100 / 500)
##Result = 99
