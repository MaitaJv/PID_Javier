#!/bin/sh -e

# Me ubico en la ruta donde se ubica enl proceso python 
cd /home/user/Documentos/Facultad/PID/VisualSat

source venv/bin/activate

uvicorn main:app --host 0.0.0.0 --port 8000  --ssl-keyfile=localhost-key.pem  --ssl-certfile=localhost.pem
