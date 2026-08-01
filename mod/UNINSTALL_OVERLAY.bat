@echo off
setlocal EnableExtensions EnableDelayedExpansion
title FreeBuild Unlimited - Uninstall
set "MODDIR=%~dp0"
for %%I in ("%MODDIR%..\..\Content\Paks") do set "GAMEPAKS=%%~fI"

echo ============================================
echo  FreeBuild Unlimited - Uninstaller
echo ============================================
echo.

del /F /Q "!GAMEPAKS!\WS-WindowsNoEditor_1_P.pak" 2>nul
del /F /Q "!GAMEPAKS!\WS-WindowsNoEditor_1_P.sig" 2>nul
del /F /Q "!GAMEPAKS!\WS-WindowsNoEditor_2_P.pak" 2>nul
del /F /Q "!GAMEPAKS!\WS-WindowsNoEditor_2_P.sig" 2>nul

echo [OK] Overlay files removed from:
echo   !GAMEPAKS!
echo.
echo Base WS-WindowsNoEditor.pak was not touched.
echo.
pause
