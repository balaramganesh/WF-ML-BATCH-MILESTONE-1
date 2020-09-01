import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = []
    final_features.extend([int_features[2],int_features[3],int_features[6],int_features[8],int_features[9],int_features[10],
    int_features[11],int_features[12]]) #Experience

    if int_features[7] == 1 :
        final_features.extend([0,0])
    elif int_features[7] == 2 :
        final_features.extend([1,0])
    else:
        final_features.extend([0,1])
    
    if int_features[5] == 1:
        final_features.extend([0,0,0])
    elif int_features[5] == 2:
        final_features.extend([1,0,0])
    elif int_features[5] == 3:
        final_features.extend([0,1,0])
    else:
        final_features.extend([0,0,1])
    #final_features = [np.array(int_features)]
    prediction = model.predict([final_features])
    output = prediction[0]
    #output = prediction[0][0]
    #output = round(prediction[0][0], 2)
    print("output is : ",output)
    if output == 1:
        return render_template('index.html', prediction_text='The customer accepts the personal loan')
    else:
        return render_template('index.html', prediction_text='The customer does not accept the personal loan')
    
    #return render_template('index.html', prediction_text='Outcome is {}'.format(output))
    

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)