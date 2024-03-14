# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class model_input(BaseModel):
    Follicle_No_R : int
    Follicle_No_L : int
    skin_darkening : int
    hair_growth : int
    Weight_gain : int
    cycle : int
    Fast_food : float
    Pimples : int
    amh_ng_ml: float
    Weight_kg: int
    BMI : float
    Cycle_length : int
    Hair_loss : int
    age_yrs : int
    Waist_inch : float
    
    
#loading the saved_model
pcos_model = pickle.load(open('pcos_model.sav', 'rb'))

@app.post('/pcos_prediction')
def pcos_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    folR = input_dictionary['Follicle_No_R']
    folL = input_dictionary['Follicle_No_L']
    skin = input_dictionary['skin_darkening']
    hairG = input_dictionary['hair_growth']
    weightG = input_dictionary['Weight_gain']
    cycleRI = input_dictionary['cycle']
    ffood = input_dictionary['Fast_food']
    pimp = input_dictionary['Pimples']
    amh = input_dictionary['amh_ng_ml']
    weight = input_dictionary['Weight_kg']
    bmi = input_dictionary['BMI']
    cycle_len = input_dictionary['Cycle_length']
    hairL = input_dictionary['Hair_loss']
    age = input_dictionary['age_yrs']
    waist = input_dictionary['Waist_inch']
    
    input_list = [folR, folL, skin, hairG, weightG, cycleRI, ffood, pimp, amh, weight, bmi, cycle_len, hairL, age, waist]
    
    prediction = pcos_model.predict([input_list])
    
    if prediction[0] == 0:
        return 'The person does not have PCOS'
    
    else:
        return 'The person has PCOS'
    
    
    
    
    



    