from django.shortcuts import render

from .apps import AnalyserappConfig
from django.http import JsonResponse
from rest_framework.views import APIView

class call_model(APIView):
        def get(self,request):
                if request.method == 'GET':
                        text = request.GET.get('text')

                        vector = AnalyserappConfig.vectorizer.transform([text])
                        prediction = AnalyserappConfig.model.predict(vector)[0]
                        response = {'text_sentiment': prediction}

                        return JsonResponse(response)
