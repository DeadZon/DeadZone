#!/bin/sh
cd "$(dirname "$0")"
fastboot=bin/linux/fastboot
if [ ! -f $fastboot ]; then echo "$fastboot not found."; exit 1; fi
if [ ! -x $fastboot ] && ! chmod +x $fastboot; then echo "$fastboot cannot be executed."; exit 1; fi
echo "Waiting for device..."
device=$($fastboot getvar product 2>&1 | grep "\bproduct:" | awk "{print \$2}")
if [ -z "$device" ]; then echo "Your device could not be detected."; exit 1; fi
echo "Your device: $device"
if [ "$device" != "zircon" ]; then echo "Compatible devices: zircon"; exit 1; fi
hwc=$($fastboot getvar hwc 2>&1 | grep "\bhwc:" | awk "{print \$2}")

# DEADZONE_BANNER_START
# DEADZONE_BANNER_END

echo "Your device will be flashed and the data partition will be formatted."
echo "You will lose your apps, settings and files on internal storage."
echo "Continue if you are flashing for the first time or downgrading."
printf "Do you want to continue? [y/N] "
read -r choice
if [ "$choice" != "y" ] && [ "$choice" != "Y" ]; then exit 0; fi

echo "##############################################################"
echo "Please wait. The device will reboot once flashing is complete."
echo "##############################################################"
# DEADZONE_IMAGE_FLASH_START
$fastboot set_active a
# DEADZONE_IMAGE_FLASH_END
$fastboot erase metadata
$fastboot erase userdata
$fastboot erase expdb
$fastboot oem cdms
$fastboot reboot
