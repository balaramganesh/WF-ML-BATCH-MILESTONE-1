import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'ID':5001, 'Age':50, 'Experience':25, 'Income':80, 'ZIP Code':96651, 'Family':3, 'CCAvg':2, 'Education':2, 
                            'Mortgage':20, 'Securities Account':1, 'CD Account':1, 'Online': 1, 'CreditCard':1})

print(r.json())