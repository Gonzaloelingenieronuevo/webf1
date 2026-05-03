# -*- coding: utf-8 -*-
"""
Created on Sun May  3 11:54:44 2026

@author: gonza
"""

import fastf1
import os

fastf1.Cache.enable_cache("./cache")

def get_telemetry(year, gp, driver, lap_number):
    try:
        session = fastf1.get_session(year, gp, "R")
        session.load()

        laps = session.laps.pick_drivers(driver)
        lap = laps[laps['LapNumber'] == lap_number].iloc[0]

        tel = lap.get_telemetry().add_distance()
        tel['Time'] = tel['Time'].dt.total_seconds()

        os.makedirs("outputs", exist_ok=True)
        file_path = f"outputs/{driver}_{gp}_{lap_number}.xlsx"
        tel.to_excel(file_path)

        return {
            "status": "ok",
            "file": file_path,
            "points": len(tel)
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}
    
