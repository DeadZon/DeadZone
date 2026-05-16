@echo off
chcp 65001 >nul
setlocal

set "PATH=%~dp0bin;%PATH%"

echo ==========================================
echo    HYPERUR VBMeta Generator Tool
echo    ROM DUOC PHAT TRIEN BOI USAGI VA RIO
echo ==========================================
echo.

set "AVBTOOL=avbtool.py"
set "KEY=testkey_rsa2048.pem"
set "STOCK_VBMETA=vbmeta.img"
set "OUTPUT=vbmeta_hyperur.img"

if not exist "%AVBTOOL%" (
    echo [LOI] Khong tim thay %AVBTOOL% trong thu muc hien tai!
    pause
    exit /b 1
)

if not exist "%KEY%" (
    echo [LOI] Khong tim thay %KEY% trong thu muc hien tai!
    pause
    exit /b 1
)

if not exist "%STOCK_VBMETA%" (
    echo [LOI] Khong tim file %STOCK_VBMETA% !
    echo Vui long copy file vbmeta goc cua may vao thu muc nay va doi ten thanh %STOCK_VBMETA%.
    pause
    exit /b 1
)

if not exist "%~dp0bin\openssl.exe" (
    echo [LOI] Khong tim thay openssl.exe trong thu muc bin!
    pause
    exit /b 1
)

echo [INFO] Dang patch file vbmeta...
echo [INFO] - Ke thua cau truc tu: %STOCK_VBMETA%
echo [INFO] - Trang thai: AVB Enable, dm-verity Disabled
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
    echo [THANH CONG] Da tao xong file: %OUTPUT%
    echo [INFO] De flash vao may, hay dua may ve Fastboot va chay lenh:
    echo fastboot flash vbmeta %OUTPUT%
) else (
    echo.
    echo [LOI] Co loi xay ra trong qua trinh tao vbmeta!
    echo [FIX] Vui long kiem tra lai thu muc 'bin' da co du file openssl chua.
)

echo.
pause