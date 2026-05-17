@echo off
title DeadZone — Format Data Only
setlocal enabledelayedexpansion
cd /d "%~dp0"

:: Enable ANSI colour support (Windows 10+)
reg add HKCU\Console /v VirtualTerminalLevel /t REG_DWORD /d 1 /f >nul 2>&1
for /f %%a in ('echo prompt $E ^| cmd') do set "ESC=%%a"
set "RED=%ESC%[91m"
set "GREEN=%ESC%[92m"
set "YELLOW=%ESC%[93m"
set "CYAN=%ESC%[96m"
set "WHITE=%ESC%[97m"
set "BOLD=%ESC%[1m"
set "RESET=%ESC%[0m"

:: ============================================================
::  HEADER
:: ============================================================
echo.
echo %CYAN%%BOLD%  ============================================================%RESET%
echo %CYAN%%BOLD%   DeadZone — Format Data Only%RESET%
echo %CYAN%%BOLD%   Developer: MEZO Developer%RESET%
echo %CYAN%%BOLD%  ============================================================%RESET%
echo.
echo %YELLOW%  This script erases metadata and userdata ONLY.%RESET%
echo %YELLOW%  No ROM images will be flashed.%RESET%
echo %YELLOW%  Use this to fix "Format Data" prompts or encryption issues.%RESET%
echo.

:: ============================================================
::  ENVIRONMENT CHECK
:: ============================================================
set "fastboot=META-INF\windows\fastboot.exe"
if not exist "%fastboot%" (
    echo %RED%[DEADZONE ERROR] fastboot.exe not found at: %fastboot%%RESET%
    echo %YELLOW%[DEADZONE WARNING] Make sure the ZIP was extracted completely.%RESET%
    pause & exit /B 1
)

:: ============================================================
::  DEVICE DETECTION
:: ============================================================
echo %WHITE%Listing connected fastboot devices...%RESET%
"%fastboot%" devices
echo.

set "connected="
for /f "tokens=2" %%A in ('"%fastboot%" getvar product 2^>^&1 ^| findstr "product:"') do set "connected=%%A"
if "%connected%" equ "" (
    echo %RED%[DEADZONE ERROR] No device detected. Is fastboot mode active?%RESET%
    echo %YELLOW%[DEADZONE WARNING] Hold Power + Volume Down to enter fastboot.%RESET%
    pause & exit /B 1
)

echo %WHITE%  Connected device: %CYAN%%connected%%RESET%
echo.

:: ============================================================
::  FIRMWARE INFO (informational only)
:: ============================================================
set "fwinfo=images\DeadZone_firmware.txt"
if exist "%fwinfo%" (
    echo %WHITE%  ROM Information:%RESET%
    for /f "usebackq tokens=1,* delims==" %%A in ("%fwinfo%") do (
        echo     %CYAN%%%A%RESET%: %WHITE%%%B%RESET%
    )
    echo.
)

:: ============================================================
::  CONFIRM — DATA WILL BE ERASED
:: ============================================================
echo %RED%%BOLD%  ============================================================%RESET%
echo %RED%%BOLD%   ALL USER DATA WILL BE PERMANENTLY ERASED.%RESET%
echo %RED%%BOLD%   Apps, settings, and files on internal storage will be lost.%RESET%
echo %RED%%BOLD%  ============================================================%RESET%
echo.
echo %WHITE%Press any key to proceed with format, or close this window to cancel.%RESET%
pause >nul
echo.

:: ============================================================
::  FORMAT DATA
:: ============================================================
echo %YELLOW%[DEADZONE] Erasing metadata partition...%RESET%
"%fastboot%" erase metadata
if errorlevel 1 (
    echo %YELLOW%[DEADZONE WARNING] metadata erase returned non-zero (may not exist on this device).%RESET%
)

echo %YELLOW%[DEADZONE] Erasing userdata partition...%RESET%
"%fastboot%" erase userdata
if errorlevel 1 (
    echo %RED%[DEADZONE ERROR] Failed to erase userdata.%RESET%
    pause & exit /B 1
)

:: ============================================================
::  REBOOT
:: ============================================================
echo.
echo %GREEN%%BOLD%  ============================================================%RESET%
echo %GREEN%%BOLD%   [DEADZONE OK] Format complete. Rebooting...%RESET%
echo %GREEN%%BOLD%  ============================================================%RESET%
echo.
echo %WHITE%  The device will boot into the setup wizard.%RESET%
echo %WHITE%  Do not interrupt power during the first boot.%RESET%
echo.
"%fastboot%" reboot

echo.
echo Press any key to close this window.
pause >nul
endlocal
