@echo off
chcp 65001 >nul
title nzv tools

python --version >nul 2>&1
if %errorlevel% equ 0 (
    set PYTHON_CMD=python
    goto run_main
)

py --version >nul 2>&1
if %errorlevel% equ 0 (
    set PYTHON_CMD=py
    goto run_main
)

echo.
echo  ERROR: Python not found
echo.
echo  Download: https://www.python.org/downloads/
echo  Check "Add python.exe to PATH" during install
echo.
pause
exit /b

:run_main
%PYTHON_CMD% main.py
if %errorlevel% neq 0 (
    echo.
    echo  [!] crashed (code: %errorlevel%)
    echo  [!] run install.bat to fix dependencies
    echo.
    pause
)
