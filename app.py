from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pickle
import numpy as np
import pandas as pd

model_path='model1.pkl'
with open(model_path,'rb') as file:
    model=pickle.load(file)
scaler1 = pickle.load(open('MinMaxscaler.pkl', 'rb'))
scaler2 = pickle.load(open('cholesterol.pkl', 'rb'))
scaler3 = pickle.load(open('maxHeartRate.pkl','rb'))

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/",response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", 
                                      {"request": request, "user_name": "Developer"})
@app.post('/predict')
async def predict(request:Request):
    form_data = await request.form()
    data_dict = {key: [float(val)] for key, val in form_data.items()}
    input_df = pd.DataFrame(data_dict)

    input_df = input_df.rename(columns={
        'trestbps': 'resting bp s',
        'chol': 'cholesterol',
        'MHR': 'max heart rate'
    })

    input_df['resting bp s'] = scaler1.transform(input_df[['resting bp s']])[0][0]
    input_df['cholesterol'] = scaler2.transform(input_df[['cholesterol']])[0][0]
    input_df['max heart rate'] = scaler3.transform(input_df[['max heart rate']])[0][0]
    input_df['oldpeak'] = (input_df[['oldpeak']])**(0.2)

    final_features = input_df.values
    prediction = model.predict(final_features)
    output = "Has Disease" if prediction[0]==1 else 'No Disease'
    return templates.TemplateResponse(name='index.html',
                                      context={
                                        "request": request,
                                        "prediction_text": f"Prediction: {output}"
                                    })

if __name__=="__main__":
    import uvicorn
    print("Starting FastAPI server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)