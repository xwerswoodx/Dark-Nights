@echo off
:start
set /P id=Item ID:
PYTHON get_item_from_id.py %id%
@del *.pyc
goto start