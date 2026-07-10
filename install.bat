@echo off
chcp 65001 >nul
title nzv tools installer

python --version >nul 2>&1
if %errorlevel% equ 0 (
    set PYTHON_CMD=python
    goto python_found
)

py --version >nul 2>&1
if %errorlevel% equ 0 (
    set PYTHON_CMD=py
    goto python_found
)

echo.
echo  ERROR: Python not found
echo.
echo  Download: https://www.python.org/downloads/
echo  Check "Add python.exe to PATH" during install
echo.
pause
exit /b 1

:python_found
echo  [+] python found (%PYTHON_CMD%)
echo.

%PYTHON_CMD% -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    %PYTHON_CMD% -m ensurepip --default-pip >nul 2>&1
    %PYTHON_CMD% -m pip --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo.
        echo  ERROR: pip not found
        echo  Run: %PYTHON_CMD% -m ensurepip --default-pip
        echo.
        pause
        exit /b 1
    )
)

echo  [*] installing dependencies...
echo.
%PYTHON_CMD% -m pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo  [!] install failed — run as admin or check connection
) else (
    echo.
    echo  [+] done! run start.bat or python main.py
)

echo.
pause
