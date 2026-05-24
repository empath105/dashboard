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


def run_turing_model(request):
    a = request.GET.get('a', '0.1')
    b = request.GET.get('b', '0.9')
    Du = request.GET.get('Du', '0.001')
    Dv = request.GET.get('Dv', '0.04')
    tmax = request.GET.get('tmax', '140')

    script_path = os.path.join(os.path.dirname(__file__), 'scripts', 'Turing.edp')
    
    def event_stream():
        process = subprocess.Popen(
            [
                'FreeFem++', script_path, '-nw', 
                '-a', a,
                '-b', b,
                '-Du', Du,
                '-Dv', Dv,
                '-T', tmax
            ],
            stdout=subprocess.PIPE,
            text=True
        )
        
        for line in process.stdout:
            yield f"data: {line}\n\n"
            
    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')


def run_fkpp_model(request):
    B = request.GET.get('B', '1.0')
    q = request.GET.get('q', '0.5')
    Da = request.GET.get('Da', '1.0')
    Ds = request.GET.get('Ds', '5000.0')
    Scrit = request.GET.get('Scrit', '0.3')
    tmax = request.GET.get('tmax', '50.0')
    

    script_path = os.path.join(os.path.dirname(__file__), 'scripts', 'FKPP.edp')
    
    def event_stream():
        process = subprocess.Popen(
            [
                'FreeFem++', script_path, '-nw', 
                '-B', B,
                '-q', q,
                '-Da', Da,
                '-Ds', Ds,
                '-Scrit', Scrit,
                '-Tmax', tmax
            ],
            stdout=subprocess.PIPE,
            text=True
        )
        
        for line in process.stdout:
            yield f"data: {line}\n\n"
            
    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')