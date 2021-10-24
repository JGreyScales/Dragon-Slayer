@echo off
cls
color 4
python -V
pip -V
echo ==================================== PYTHON VERSON ==================================
echo.
timeout 2
echo.
echo.
color 1
pip install pygame
pip install pathlib
pip install fnmatch2
color 2
echo.
echo.
@echo ======= =============== =============== =============== COMPLETED =============== =============== =============== ======
echo.
timeout 5

