# -*- coding: utf-8 -*-
"""
Created on Sun May  3 11:54:18 2026

@author: gonza
"""

def run_matlab():
    try:
        import matlab.engine
        eng = matlab.engine.start_matlab()

        eng.CODIGO(nargout=0)  # tu script convertido a .m

        eng.quit()

        return {"status": "ok"}

    except Exception as e:
        return {"status": "error", "message": str(e)}