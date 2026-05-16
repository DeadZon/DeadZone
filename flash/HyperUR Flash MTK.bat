@echo off
title HyperUR Flash MTK by lcnguyn06(RIO)
setlocal enabledelayedexpansion
cd /d %~dp0
set fastboot=META-INF\windows\fastboot.exe
if not exist %fastboot% echo %fastboot% not found. & pause & exit /B 1
echo =========== HYPERUR FLASHING ROM =============================
echo Mod by HyperUR Team - Website: https://www.hyperur.io.vn
echo Based on China ROM 
echo.
echo. ROM INFORMATION
for /f "usebackq tokens=1,* delims==" %%A in ("%~dp0images\HyperUR_firmware.txt") do (
    echo  %%A: %%B
)
echo.
echo ============================================================
echo.
echo Checking for connected devices...
%fastboot% devices
echo.
set expected_codename=
for /f "tokens=2 delims==" %%A in ('type images\HyperUR_firmware.txt ^| findstr /C:"Codename="') do set expected_codename=%%A
if "%expected_codename%" equ "" echo HyperUR_firmware.txt not found or Codename not set. & pause & exit /B 1
for /f "tokens=2" %%A in ('%fastboot% getvar product 2^>^&1 ^| findstr "product:"') do set device=%%A
if "%device%" equ "" echo Your device could not be detected. & pause & exit /B 1
echo Your device: %device%
if "%device%" neq "%expected_codename%" echo Compatible devices: %expected_codename% & pause & exit /B 1
set hwc=
for /f "tokens=3" %%A in ('%fastboot% oem hwid 2^>^&1 ^| findstr "HwCountry:"') do set hwc=%%A

:menu
echo.
echo ============================================================
echo  SELECT FLASH MODE
echo ============================================================
echo  [1] Update (Keep Data)    - Preserve your apps and data
echo  [2] Format (Clean Flash)  - Wipe data partition ^(first flash / downgrade^)
echo  [Q] Quit
echo ============================================================
echo.
set /p mode=Enter choice [1/2/Q]:
if /i "!mode!" equ "1" goto :update
if /i "!mode!" equ "2" goto :format
if /i "!mode!" equ "Q" exit /B 0
echo Invalid choice. Please enter 1, 2 or Q.
goto :menu

:update
set flash_mode=UPDATE
goto :flash

:format
set flash_mode=FORMAT
echo.
echo NOTE: Data partition will be ERASED.
echo       You will lose apps, settings and files on internal storage.
echo       Recommended for first time flash or ROM downgrade.
goto :flash

:flash
echo.
echo ##############################################################
echo [!flash_mode!] Please wait. The device will reboot once flashing is complete.
echo ##############################################################
echo.
%fastboot% set_active a
%fastboot% flash preloader_a images\preloader_raw.img
%fastboot% flash preloader_b images\preloader_raw.img
%fastboot% flash preloader1 images\preloader_raw.img
%fastboot% flash preloader2 images\preloader_raw.img
%fastboot% flash apusys_ab images\apusys.img
%fastboot% flash audio_dsp_ab images\audio_dsp.img
%fastboot% flash ccu_ab images\ccu.img
%fastboot% flash connsys_gnss_ab images\connsys_gnss.img
%fastboot% flash dpm_ab images\dpm.img
%fastboot% flash dtbo_ab images\dtbo.img
%fastboot% flash gpueb_ab images\gpueb.img
%fastboot% flash gz_ab images\gz.img
%fastboot% flash lk_ab images\lk.img
%fastboot% flash logo_ab images\logo.img
%fastboot% flash mcf_ota_ab images\mcf_ota.img
%fastboot% flash mcupm_ab images\mcupm.img
%fastboot% flash md1img_ab images\md1img.img
%fastboot% flash mvpu_algo_ab images\mvpu_algo.img
%fastboot% flash pi_img_ab images\pi_img.img
%fastboot% flash scp_ab images\scp.img
%fastboot% flash spmfw_ab images\spmfw.img
%fastboot% flash sspm_ab images\sspm.img
%fastboot% flash tee_ab images\tee.img
%fastboot% flash vbmeta_ab images\vbmeta.img
%fastboot% flash vbmeta_system_ab images\vbmeta_system.img
%fastboot% flash vbmeta_vendor_ab images\vbmeta_vendor.img
%fastboot% flash vcp_ab images\vcp.img
%fastboot% flash boot_ab images\boot.img
%fastboot% flash init_boot_ab images\init_boot.img
%fastboot% flash vendor_boot_ab images\vendor_boot.img
%fastboot% flash cust images\cust.img
%fastboot% flash super images\super.img
if "%flash_mode%" equ "FORMAT" %fastboot% erase metadata
if "%flash_mode%" equ "FORMAT" %fastboot% erase userdata
if "%flash_mode%" equ "FORMAT" %fastboot% erase expdb
if "%flash_mode%" equ "FORMAT" %fastboot% erase frp
%fastboot% reboot
echo.
echo. Please wait 5-10 minutes. The device will automatically restart and turn on the screen.
echo Flash completed. Press any key to exit.
pause >nul
endlocal
