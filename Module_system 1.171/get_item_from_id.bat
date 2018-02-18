@echo off
:start
set /P id=Item ID:
PYTHON process_get_item.py %id%
@del *.pyc
goto start