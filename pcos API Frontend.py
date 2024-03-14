# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 13:29:39 2024

@author: User
"""

import json
import requests

url =  'http://127.0.0.1:8000/pcos_prediction'

input_data_for_model = {
    'Follicle_No_R' : 3,
    'Follicle_No_L' : 3,
    'skin_darkening' : 0,
    'hair_growth' : 0,
    'Weight_gain' : 0,
    'cycle' : 2,
    'Fast_food' : 1,
    'Pimples' : 0,
    'amh_ng_ml' : 2.07,
    'Weight_kg' : 44,
    'BMI' : 19.3,
    'Cycle_length' : 5,
    'Hair_loss' : 0,
    'age_yrs' : 28,
    'Waist_inch' : 30
    
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)