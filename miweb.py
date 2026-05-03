# -*- coding: utf-8 -*-
"""
Created on Sun May  3 11:50:36 2026

@author: gonza
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastf1_service import get_telemetry
from matlab_service import run_matlab

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/telemetry")
def telemetry(year: int, gp: str, driver: str, lap: int):
    return get_telemetry(year, gp, driver, lap)

@app.get("/matlab")
def matlab():
    return run_matlab()

@app.get("/run_all")
def run_all(year: int, gp: str, driver: str, lap: int):
    py = get_telemetry(year, gp, driver, lap)
    ml = run_matlab()

    return {"python": py, "matlab": ml}

