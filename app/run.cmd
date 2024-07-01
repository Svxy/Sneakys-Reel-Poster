@echo off

setlocal

set "PROJECT_PATH=%~dp0"
set "DAY_COUNT_PATH=%PROJECT_PATH:~0,-1%\day_count.txt"

docker run -d --name reel-poster -v "%DAY_COUNT_PATH%:/app/day_count.txt" -e USERNAME=IG_USERNAME -e PASSWORD=IG_PASSWORD reel-poster

pause