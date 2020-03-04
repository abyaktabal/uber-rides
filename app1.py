import numpy as np 
from flask import Flask,request,jsonify,render_template
import pickle
import math
 
app=Flask(__name__)
model=pickle.load(open('taxi.pkl','rb'))


@app.route('/')
def home():
 	return render_template('ubar.html')
@app.route('/predict',methods=['POST'])
def predict():
	a=[int(x) for x in request.form.values()]
	b=[np.array(a)]
	prediction=model.predict(b)
	output=round(prediction[0],2)
	return render_template('ubar.html',prediction_text="Number of rides should be{}".format(math.floor(output)))


if __name__ == '__main__':
 	app.run(host='0.0.0.0',port=5000)