@echo off
title HyperUR Flash by lcnguyn06(RIO)
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
%fastboot% flash abl_ab images\abl.img
%fastboot% flash aop_ab images\aop.img
%fastboot% flash aop_config_ab images\aop_config.img
%fastboot% flash bluetooth_ab images\bluetooth.img
%fastboot% flash countrycode_ab images\countrycode.img
%fastboot% flash cpucp_ab images\cpucp.img
%fastboot% flash cpucp_dtb_ab images\cpucp_dtb.img
%fastboot% flash devcfg_ab images\devcfg.img
%fastboot% flash dsp_ab images\dsp.img
%fastboot% flash dtbo_ab images\dtbo.img
%fastboot% flash featenabler_ab images\featenabler.img
%fastboot% flash hyp_ab images\hyp.img
%fastboot% flash idmanager_ab images\idmanager.img
%fastboot% flash imagefv_ab images\imagefv.img
%fastboot% flash keymaster_ab images\keymaster.img
%fastboot% flash modem_ab images\modem.img
if "%hwc%" equ "CN" (
%fastboot% flash modemfirmware_ab images\modemfirmware.img
) else (
%fastboot% flash modemfirmware_ab images\modemfirmware_ww.img
)
%fastboot% flash multiimgqti_ab images\multiimgqti.img
%fastboot% flash pdp_ab images\pdp.img
%fastboot% flash pdp_cdb_ab images\pdp_cdb.img
%fastboot% flash pvmfw_ab images\pvmfw.img
%fastboot% flash qupfw_ab images\qupfw.img
%fastboot% flash shrm_ab images\shrm.img
%fastboot% flash soccp_dcd_ab images\soccp_dcd.img
%fastboot% flash soccp_debug_ab images\soccp_debug.img
%fastboot% flash spuservice_ab images\spuservice.img
%fastboot% flash tz_ab images\tz.img
%fastboot% flash uefi_ab images\uefi.img
%fastboot% flash uefisecapp_ab images\uefisecapp.img
%fastboot% flash vbmeta_ab images\vbmeta.img
%fastboot% flash vbmeta_system_ab images\vbmeta_system.img
%fastboot% flash vm-bootsys_ab images\vm-bootsys.img
%fastboot% flash xbl_ab images\xbl.img
%fastboot% flash xbl_config_ab images\xbl_config.img
%fastboot% flash xbl_ramdump_ab images\xbl_ramdump.img
%fastboot% flash boot_ab images\boot.img
%fastboot% flash init_boot_ab images\init_boot.img
%fastboot% flash vendor_boot_ab images\vendor_boot.img
%fastboot% flash recovery_ab images\recovery.img
%fastboot% flash super images\super.img
if "%flash_mode%" equ "FORMAT" %fastboot% erase metadata
if "%flash_mode%" equ "FORMAT" %fastboot% erase userdata
if "%flash_mode%" equ "FORMAT" %fastboot% erase frp
%fastboot% reboot
echo.
echo. Please wait 5-10 minutes. The device will automatically restart and turn on the screen.
echo Flash completed. Press any key to exit.
pause >nul
endlocal
