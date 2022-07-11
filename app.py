import pandas as pd
import streamlit as st
import xgboost as xgb
import numpy as np

model = xgb.XGBClassifier()

model.load_model("xgb_model.bin")

@st.cache()
# defining the function which will make the prediction using the data which the user inputs 
def prediction(fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE):

    parkinsons_prediction = model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])

    if (parkinsons_prediction[0] == 0):

        parkinson_diagnosis = "The person does not have Parkinson's disease"
    else:
        parkinson_diagnosis = "The person has Parkinson's disease"
    
    return parkinson_diagnosis

#title
st.title("Parkinson's Disease Prediction")

# following lines create boxes in which user can enter data required to make prediction   
col1, col2, col3, col4, col5 = st.columns(5)  
    
with col1:
    fo = st.text_input('MDVP:Fo(Hz)')
        
with col2:
    fhi = st.text_input('MDVP:Fhi(Hz)')
        
with col3:
    flo = st.text_input('MDVP:Flo(Hz)')
        
with col4:
    Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
with col5:
    Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
with col1:
    RAP = st.text_input('MDVP:RAP')
        
with col2:
    PPQ = st.text_input('MDVP:PPQ')
        
with col3:
    DDP = st.text_input('Jitter:DDP')
        
with col4:
    Shimmer = st.text_input('MDVP:Shimmer')
        
with col5:
    Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
with col1:
    APQ3 = st.text_input('Shimmer:APQ3')
        
with col2:
    APQ5 = st.text_input('Shimmer:APQ5')
        
with col3:
    APQ = st.text_input('MDVP:APQ')
        
with col4:
    DDA = st.text_input('Shimmer:DDA')
        
with col5:
    NHR = st.text_input('NHR')
        
with col1:
    HNR = st.text_input('HNR')
        
with col2:
    RPDE = st.text_input('RPDE')
        
with col3:
        DFA = st.text_input('DFA')
        
with col4:
    spread1 = st.text_input('spread1')
        
with col5:
    spread2 = st.text_input('spread2')
        
with col1:
    D2 = st.text_input('D2')
        
with col2:
    PPE = st.text_input('PPE')


# code for Prediction
parkinson_prediction = ''
    
# creating a button for Prediction    
if st.button("Parkinson's Test Result"):
    Shimmer_dB = float(Shimmer_dB)
    APQ3 = float(APQ3)
    Shimmer = float(Shimmer)
    DDP = float(DDP)
    PPQ = float(PPQ)
    fo = float(fo)
    fhi = float(fhi)
    flo = float(flo)
    Jitter_percent = float(Jitter_percent)
    Jitter_Abs = float(Jitter_Abs)
    RAP = float(RAP)
    APQ5 = float(APQ5)
    DDA = float(DDA)
    NHR = float(NHR)
    HNR = float(HNR)
    APQ = float(APQ)
    RPDE = float(RPDE)
    DFA = float(DFA)
    spread1 = float(spread1)
    spread2 = float(spread2)
    D2 = float(D2)
    PPE = float(PPE)
    
    parkinson_prediction = prediction(fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE)

    st.success('Your result is {}'.format(parkinson_prediction))
   
    