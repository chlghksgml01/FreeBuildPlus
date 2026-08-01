@echo off
setlocal EnableExtensions EnableDelayedExpansion
title FreeBuild Plus - Install
set "MODDIR=%~dp0"
for %%I in ("%MODDIR%..\..\Content\Paks") do set "GAMEPAKS=%%~fI"

echo ==========================================
echo  FreeBuild Plus - Installer
echo ==========================================
echo.

if not exist "!GAMEPAKS!\WS-WindowsNoEditor.pak" (
  echo [ERROR] Soulmask Paks folder not found.
  echo.
  echo This file must stay inside:
  echo   Soulmask\WS\Mods\FreeBuildPlus
  echo.
  echo Looked in:
  echo   !GAMEPAKS!
  echo.
  pause
  exit /b 1
)

echo Installing to:
echo   !GAMEPAKS!
echo.

REM Remove legacy split overlays so only FreeBuild Plus is active
del /F /Q "!GAMEPAKS!\WS-WindowsNoEditor_2_P.pak" 2>nul
del /F /Q "!GAMEPAKS!\WS-WindowsNoEditor_2_P.sig" 2>nul

copy /Y "%MODDIR%OverlayPaks\WS-WindowsNoEditor_1_P.pak" "!GAMEPAKS!\" >nul
if errorlevel 1 (
  echo [ERROR] Could not copy the mod file.
  echo Right-click this file and choose "Run as administrator".
  echo.
  pause
  exit /b 1
)

copy /Y "%MODDIR%OverlayPaks\WS-WindowsNoEditor_1_P.sig" "!GAMEPAKS!\" >nul
if errorlevel 1 (
  echo [ERROR] Could not copy the signature file.
  echo Right-click this file and choose "Run as administrator".
  echo.
  pause
  exit /b 1
)

echo [OK] FreeBuild Plus installed.
echo.
pause
