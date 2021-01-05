#!/bin/bash
xset s noblank
xset s off
xset -dpms

unclutter -idle 0.5 -root &

sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' /home/pi/.config/chromium/Default/Preferences
sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' /home/pi/.config/chromium/Default/Preferences

#/usr/bin/chromium-browser \
#	--noerrdialogs --disable-infobars --kiosk http://localhost/gh 


DISPLAY=:0 /usr/bin/chromium-browser http://localhost/gh \
--kiosk \
--disable-infobars \
--incognito \
--disable-session-crashed-bubble \
--disable-features=RendererCodeIntegrity \
--process-per-site \
--bwsi \
--disable-cache \
--noerrdialogs \
--no-first-run \
--fast --fast-start \
--check-for-update-interval=31536000 \
--disable-gl-error-limit \
--aggressive-cache-discard \
--simulate-critical-update \
--user-agent="Mozilla/5.0 (X11; CrOS armv7l 11895.95.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.125 Safari/537.36" \
--autoplay-policy=no-user-gesture-required 

