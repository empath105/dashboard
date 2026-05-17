from django.shortcuts import render
import subprocess
import os
import json
from django.http import JsonResponse
from django.http import StreamingHttpResponse
from django.conf import settings

def run_sir_model(request):
    beta = request.GET.get('beta', '0.4')
    gamma = request.GET.get('gamma', '0.1')
    di = request.GET.get('di', '0.5')
    ds = request.GET.get('ds', '2.0')
    dr = request.GET.get('dr', '2.0')
    tmax = request.GET.get('tmax', '100')
    i0 = request.GET.get('i0', '0.05')

    script_path = os.path.join(os.path.dirname(__file__), 'scripts', 'SIR.edp')
    
    def event_stream():
        process = subprocess.Popen(
            [
                'FreeFem++', script_path, '-nw', 
                '-beta', beta,
                '-gamma', gamma,
                '-DI', di,
                '-DS', ds,
                '-DR', dr,
                '-Tmax', tmax
            ],
            stdout=subprocess.PIPE,
            text=True
        )
        
        for line in process.stdout:
            yield f"data: {line}\n\n"
            
    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')