from django.shortcuts import render
import pickle
import pandas as pd
import os
from django.conf import settings

# Load Models with Absolute Path
model = pickle.load(open(os.path.join(settings.BASE_DIR, 'models', 'model_gbc.pkl'), 'rb'))
scaler = pickle.load(open(os.path.join(settings.BASE_DIR, 'models', 'scaler.pkl'), 'rb'))
encoder = pickle.load(open(os.path.join(settings.BASE_DIR, 'models', 'encoder.pkl'), 'rb'))

def predict_crop(N, P, K, temperature, humidity, ph, rainfall):
    input_df = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]],
                            columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])
    scaled_input = scaler.transform(input_df)
    encoded_result = model.predict(scaled_input)
    result = encoder.inverse_transform(encoded_result)
    return result[0]

def home(request):
    return render(request, 'predictor/form.html')

def result(request):
    if request.method == 'POST':
        N = float(request.POST['N'])
        P = float(request.POST['P'])
        K = float(request.POST['K'])
        temperature = float(request.POST['temperature'])
        humidity = float(request.POST['humidity'])
        ph = float(request.POST['ph'])
        rainfall = float(request.POST['rainfall'])

        crop = predict_crop(N, P, K, temperature, humidity, ph, rainfall)
        return render(request, 'predictor/result.html', {'crop': crop})
    return render(request, 'predictor/form.html')

# Create your views here.
