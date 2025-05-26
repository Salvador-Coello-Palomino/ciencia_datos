from django.shortcuts import render
import numpy as np
import joblib
import pandas as pd


def prediccion_view(request):
    modelo = joblib.load('modelo_ventas.pkl')
    x_pred = np.array([12, 13, 14]).reshape(-1, 1)
    predicciones = np.round(modelo.predict(x_pred))

    fechas_pred = pd.date_range(start='2025-01-01', periods=3, freq='MS')
    resultados = zip(fechas_pred.strftime('%b %Y'), predicciones)

    return render(request, 'ventas/prediccion.html', {'resultados': resultados})
