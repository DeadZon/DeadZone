@echo off
cd %~dp0
set fastboot=bin\windows\fastboot.exe
if not exist %fastboot% echo %fastboot% not found. & pause & exit /B 1
echo Waiting for device...
set device=
for /f "tokens=2" %%A in ('%fastboot% getvar product 2^>^&1 ^| findstr "\<product:"') do set device=%%A
if "%device%" equ "" echo Your device could not be detected. & pause & exit /B 1
echo Your device: %device%
if "%device%" neq "zircon" echo Compatible devices: zircon & pause & exit /B 1
set hwc=
for /f "tokens=2" %%A in ('%fastboot% getvar hwc 2^>^&1 ^| findstr "\<hwc:"') do set hwc=%%A

:: DEADZONE_BANNER_START
:: DEADZONE_BANNER_END

echo Your device will be flashed without formatting the data partition.
echo You will keep your apps, settings and files on internal storage.
echo Continue if you are upgrading from an older ROM version.
set /p choice=Do you want to continue? [y/N]
if /i "%choice%" neq "y" exit /B 0

echo ##############################################################
echo Please wait. The device will reboot once flashing is complete.
echo ##############################################################
:: DEADZONE_IMAGE_FLASH_START
%fastboot% set_active a
:: DEADZONE_IMAGE_FLASH_END
%fastboot% erase expdb
%fastboot% oem cdms
%fastboot% reboot
