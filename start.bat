@echo off
REM Start script for Windows development

REM Get the port from environment variable or use default
set PORT=%PORT%
if "%PORT%"=="" set PORT=5000

REM Start the application
python app.py
