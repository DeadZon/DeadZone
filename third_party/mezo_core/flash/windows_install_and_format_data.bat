@echo off
title DeadZone Fastboot Installer
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
echo %CYAN%%BOLD%   DeadZone ROM Installer — Clean Flash (Format Data)%RESET%
echo %CYAN%%BOLD%   Developer: MEZO Developer%RESET%
echo %CYAN%%BOLD%  ============================================================%RESET%
echo.
echo %YELLOW%  WARNING: This script will ERASE all user data on the device.%RESET%
echo %YELLOW%  Recommended for: first flash, ROM downgrade, or fixing boot loops.%RESET%
echo.

:: ============================================================
::  ENVIRONMENT CHECKS
:: ============================================================
set "fastboot=META-INF\windows\fastboot.exe"
if not exist "%fastboot%" (
    echo %RED%[DEADZONE ERROR] fastboot.exe not found at: %fastboot%%RESET%
    echo %YELLOW%[DEADZONE WARNING] Make sure the ZIP was extracted completely.%RESET%
    goto :fail
)

if not exist "images" (
    echo %RED%[DEADZONE ERROR] images\ folder not found. Extract the full ZIP first.%RESET%
    goto :fail
)

set "fwinfo=images\DeadZone_firmware.txt"
if not exist "%fwinfo%" (
    echo %RED%[DEADZONE ERROR] images\DeadZone_firmware.txt not found.%RESET%
    goto :fail
)

:: ============================================================
::  ROM INFORMATION
:: ============================================================
echo %WHITE%  ROM Information:%RESET%
for /f "usebackq tokens=1,* delims==" %%A in ("%fwinfo%") do (
    echo     %CYAN%%%A%RESET%: %WHITE%%%B%RESET%
)
echo.

:: ============================================================
::  REQUIRED IMAGE CHECK
:: ============================================================
set "missing=0"
for %%I in (super.img boot.img init_boot.img vendor_boot.img vbmeta.img) do (
    if not exist "images\%%I" (
        echo %RED%[DEADZONE ERROR] Required image missing: images\%%I%RESET%
        set "missing=1"
    )
)
if "!missing!" equ "1" (
    echo %RED%[DEADZONE ERROR] Required images are missing. Aborting.%RESET%
    goto :fail
)
echo %GREEN%[DEADZONE OK] All required images present.%RESET%
echo.

:: ============================================================
::  DEVICE DETECTION
:: ============================================================
echo %WHITE%Listing connected fastboot devices...%RESET%
"%fastboot%" devices
echo.

set "expected="
for /f "tokens=2 delims==" %%A in ('type "%fwinfo%" ^| findstr /C:"Codename="') do set "expected=%%A"
if "%expected%" equ "" (
    echo %RED%[DEADZONE ERROR] Codename missing in DeadZone_firmware.txt.%RESET%
    goto :fail
)

set "connected="
for /f "tokens=2" %%A in ('"%fastboot%" getvar product 2^>^&1 ^| findstr "product:"') do set "connected=%%A"
if "%connected%" equ "" (
    echo %RED%[DEADZONE ERROR] No device detected. Is fastboot mode active?%RESET%
    echo %YELLOW%[DEADZONE WARNING] Hold Power + Volume Down to enter fastboot.%RESET%
    goto :fail
)

echo %WHITE%  Connected device  : %CYAN%%connected%%RESET%
echo %WHITE%  Expected codename : %CYAN%%expected%%RESET%
echo.

if /i "%connected%" neq "%expected%" (
    echo %RED%[DEADZONE ERROR] Device mismatch — flash aborted for safety.%RESET%
    echo %RED%  Connected: %connected%    Expected: %expected%%RESET%
    echo %YELLOW%[DEADZONE WARNING] Flashing to a wrong device can cause permanent damage.%RESET%
    goto :fail
)
echo %GREEN%[DEADZONE OK] Device codename verified.%RESET%
echo.

:: ============================================================
::  FINAL CONFIRMATION — DATA WILL BE ERASED
:: ============================================================
echo %RED%%BOLD%  ============================================================%RESET%
echo %RED%%BOLD%   ALL USER DATA WILL BE PERMANENTLY ERASED.%RESET%
echo %RED%%BOLD%   Make sure you have backed up your important files.%RESET%
echo %RED%%BOLD%  ============================================================%RESET%
echo.
echo %WHITE%Press any key to proceed, or close this window to cancel.%RESET%
pause >nul
echo.

:: ============================================================
::  FLASH — Set active slot
:: ============================================================
echo %WHITE%Setting active slot to A...%RESET%
"%fastboot%" set_active a
if errorlevel 1 goto :fail

:: ============================================================
::  FLASH — Core partition images (required)
:: ============================================================
echo.
echo %WHITE%Flashing core boot images...%RESET%
"%fastboot%" flash boot_ab "images\boot.img"
if errorlevel 1 goto :fail

"%fastboot%" flash init_boot_ab "images\init_boot.img"
if errorlevel 1 goto :fail

"%fastboot%" flash vendor_boot_ab "images\vendor_boot.img"
if errorlevel 1 goto :fail

:: ============================================================
::  FLASH — Vbmeta
:: ============================================================
echo.
echo %WHITE%Flashing vbmeta...%RESET%
"%fastboot%" flash vbmeta_ab "images\vbmeta.img"
if errorlevel 1 goto :fail

if exist "images\vbmeta_system.img" (
    "%fastboot%" flash vbmeta_system_ab "images\vbmeta_system.img"
    if errorlevel 1 goto :fail
) else (
    echo %YELLOW%[SKIP] vbmeta_system.img not present%RESET%
)

if exist "images\vbmeta_vendor.img" (
    "%fastboot%" flash vbmeta_vendor_ab "images\vbmeta_vendor.img"
    if errorlevel 1 goto :fail
) else (
    echo %YELLOW%[SKIP] vbmeta_vendor.img not present%RESET%
)

:: ============================================================
::  FLASH — Optional boot-related
:: ============================================================
if exist "images\dtbo.img" (
    echo %WHITE%Flashing dtbo...%RESET%
    "%fastboot%" flash dtbo_ab "images\dtbo.img"
    if errorlevel 1 goto :fail
) else (
    echo %YELLOW%[SKIP] dtbo.img%RESET%
)

if exist "images\recovery.img" (
    echo %WHITE%Flashing recovery...%RESET%
    "%fastboot%" flash recovery_ab "images\recovery.img"
    if errorlevel 1 goto :fail
) else (
    echo %YELLOW%[SKIP] recovery.img%RESET%
)

:: ============================================================
::  FLASH — Snapdragon firmware (all optional)
:: ============================================================
echo.
echo %WHITE%Flashing Snapdragon firmware (optional)...%RESET%
for %%I in (abl aop aop_config bluetooth cpucp cpucp_dtb devcfg dsp featenabler hyp idmanager imagefv keymaster modem modemfirmware modemfirmware_ww multiimgqti pdp pdp_cdb pvmfw qupfw shrm soccp_dcd soccp_debug spuservice tz uefi uefisecapp vm-bootsys xbl xbl_config xbl_ramdisk xbl_ramdump) do (
    if exist "images\%%I.img" (
        echo %WHITE%  Flashing %%I...%RESET%
        "%fastboot%" flash %%I_ab "images\%%I.img"
        if errorlevel 1 goto :fail
    ) else (
        echo %YELLOW%[SKIP] %%I.img%RESET%
    )
)

if exist "images\countrycode.img" (
    "%fastboot%" flash countrycode "images\countrycode.img"
    if errorlevel 1 goto :fail
) else (
    echo %YELLOW%[SKIP] countrycode.img%RESET%
)

:: ============================================================
::  FLASH — MTK firmware (all optional, NO preloader)
:: ============================================================
echo.
echo %WHITE%Flashing MTK firmware (optional)...%RESET%
for %%I in (apusys audio_dsp ccu connsys_gnss dpm gpueb gz lk logo mcf_ota mcupm md1img mvpu_algo pi_img scp spmfw sspm tee vcp) do (
    if exist "images\%%I.img" (
        echo %WHITE%  Flashing %%I...%RESET%
        "%fastboot%" flash %%I_ab "images\%%I.img"
        if errorlevel 1 goto :fail
    ) else (
        echo %YELLOW%[SKIP] %%I.img%RESET%
    )
)

if exist "images\cust.img" (
    "%fastboot%" flash cust "images\cust.img"
    if errorlevel 1 goto :fail
) else (
    echo %YELLOW%[SKIP] cust.img%RESET%
)

:: MTK preloader — NEVER flash by default
set "FLASH_PRELOADER=0"
if exist "images\preloader_raw.img" (
    echo.
    echo %YELLOW%[DEADZONE WARNING] preloader_raw.img is present but will NOT be flashed.%RESET%
    echo %YELLOW%  Set FLASH_PRELOADER=1 at the top of this script only if you know what you are doing.%RESET%
)
if "%FLASH_PRELOADER%" equ "1" (
    if exist "images\preloader_raw.img" (
        echo %YELLOW%[DEADZONE WARNING] Flashing preloader — advanced mode enabled by user.%RESET%
        "%fastboot%" flash preloader_a "images\preloader_raw.img"
        if errorlevel 1 goto :fail
        "%fastboot%" flash preloader_b "images\preloader_raw.img"
        if errorlevel 1 goto :fail
        "%fastboot%" flash preloader1 "images\preloader_raw.img"
        if errorlevel 1 goto :fail
        "%fastboot%" flash preloader2 "images\preloader_raw.img"
        if errorlevel 1 goto :fail
    )
)

:: ============================================================
::  FLASH — Super image
:: ============================================================
echo.
echo %WHITE%Flashing super.img (this may take several minutes)...%RESET%
"%fastboot%" flash super "images\super.img"
if errorlevel 1 goto :fail

:: ============================================================
::  FORMAT DATA — Erase metadata and userdata
:: ============================================================
echo.
echo %YELLOW%[DEADZONE] Erasing metadata partition...%RESET%
"%fastboot%" erase metadata

echo %YELLOW%[DEADZONE] Erasing userdata partition...%RESET%
"%fastboot%" erase userdata
if errorlevel 1 goto :fail

:: ============================================================
::  REBOOT
:: ============================================================
echo.
echo %GREEN%%BOLD%  ============================================================%RESET%
echo %GREEN%%BOLD%   [DEADZONE OK] Clean flash complete.%RESET%
echo %GREEN%%BOLD%   Rebooting device...%RESET%
echo %GREEN%%BOLD%  ============================================================%RESET%
echo.
echo %WHITE%  Please wait 5-10 minutes for the first boot to complete.%RESET%
echo %WHITE%  The device may reboot multiple times — this is normal.%RESET%
echo %WHITE%  Do not interrupt power or USB during the first boot.%RESET%
echo.
"%fastboot%" reboot

echo.
echo Press any key to close this window.
pause >nul
endlocal
exit /B 0

:: ============================================================
::  FAIL
:: ============================================================
:fail
echo.
echo %RED%%BOLD%  ============================================================%RESET%
echo %RED%%BOLD%   [DEADZONE ERROR] Flash failed.%RESET%
echo %RED%%BOLD%   Do NOT reboot until you understand what failed.%RESET%
echo %RED%%BOLD%   Check the output above for the failing command.%RESET%
echo %RED%%BOLD%  ============================================================%RESET%
echo.
pause
endlocal
exit /B 1
