@echo off
python compile_id.py
@del *.pyc
@del ids\*.pyc
@del headers\*.pyc
pause>nul