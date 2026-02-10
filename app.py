from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pickle
import numpy as np

model_path='model.pkl'
with open(model_path,'rb') as file:
    model=pickle.load(file)

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
    int_features = [int(x) for x in form_data.values()]
    final_features = [np.array(int_features)]
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