@echo off
chcp 65001 >nul
setlocal

set "PATH=%~dp0bin;%PATH%"

echo ==========================================
echo    DeadZone VBMeta Generator Tool
echo    Developer: MEZO Developer
echo ==========================================
echo.

set "AVBTOOL=avbtool.py"
set "KEY=testkey_rsa2048.pem"
set "STOCK_VBMETA=vbmeta.img"
set "OUTPUT=vbmeta_deadzone.img"

if not exist "%AVBTOOL%" (
    echo [ERROR] %AVBTOOL% not found in current directory!
    pause
    exit /b 1
)

if not exist "%KEY%" (
    echo [ERROR] %KEY% not found in current directory!
    pause
    exit /b 1
)

if not exist "%STOCK_VBMETA%" (
    echo [ERROR] %STOCK_VBMETA% not found!
    echo Copy the original vbmeta.img from your device into this directory and rename it to %STOCK_VBMETA%.
    pause
    exit /b 1
)

if not exist "%~dp0bin\openssl.exe" (
    echo [ERROR] openssl.exe not found in bin directory!
    pause
    exit /b 1
)

echo [INFO] Patching vbmeta...
echo [INFO] - Inheriting structure from: %STOCK_VBMETA%
echo [INFO] - Status: AVB Enabled, dm-verity Disabled
echo.

python "%AVBTOOL%" make_vbmeta_image ^
    --output "%OUTPUT%" ^
    --algorithm SHA256_RSA2048 ^
    --key "%KEY%" ^
    --include_descriptors_from_image "%STOCK_VBMETA%" ^
    --padding_size 4096 ^
    --set_hashtree_disabled_flag

if %errorlevel% equ 0 (
    echo.
    echo [OK] Output file created: %OUTPUT%
    echo [INFO] To flash to your device, boot into Fastboot and run:
    echo fastboot flash vbmeta %OUTPUT%
) else (
    echo.
    echo [ERROR] vbmeta generation failed!
    echo [FIX] Check that the bin\ directory contains openssl.exe.
)

echo.
pause
