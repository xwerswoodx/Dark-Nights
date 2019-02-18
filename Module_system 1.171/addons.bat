@echo off
set id=-1
:start
python -m addons.addons %id%
set /P id=">"
if %id% == exit (
  @del addons\*.pyc
  call clear_module.bat
  exit
)
goto start