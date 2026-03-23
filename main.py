from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import joblib

model = joblib.load('model (3).pkl')
scaler = joblib.load('scaler (5).pkl')

avocado_app  = FastAPI()

class AvocadoSchema(BaseModel):
    firmness:int
    hue:int
    saturation:int
    brightness:int
    sound_db:int
    weight_g:int
    size_cm3:int
    color_category:int


@avocado_app.post('/predict')
async def predict_avocado(avocado:AvocadoSchema):
    avocado_dict = avocado.dict()

    color_category = avocado_dict.pop('color_category')
    color_category_1_0 = [
        1 if color_category == 'green' else 0,
        1 if color_category == 'dark green' else 0,
        1 if color_category == 'purple' else 0,
    ]
    avocado_data = (
        list(avocado_dict.values()) + color_category_1_0
    )

    scaled_data = scaler.transform([avocado_data])
    prediction = model.predict(scaled_data)[0] -1
    print(prediction)
    reverse_mapp = {0: 'hard', 1: 'pre-conditioned', 2: 'breaking', 3: 'firm-ripe', 4: 'ripe'}
    return {'Answer': reverse_mapp[int(prediction)]}

if __name__ == '__main__':
    uvicorn.run(avocado_app, host='127.0.0.1', port=8005)