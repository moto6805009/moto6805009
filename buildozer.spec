[app]

# Application name
title = RepairApp

# Package name
package.name = repairapp

# Package domain
package.domain = org.example

# Source directory
source.dir = .

# Application version
version = 1.0

# Supported orientation (portrait/landscape)
orientation = portrait

# Include these file types in the APK
source.include_exts = py,png,jpg,kv,atlas,ttf

# Application requirements
requirements = python3,kivy,cython,requests


# Architecture to build for (supports multiple)
android.archs = armeabi-v7a, arm64-v8a

# Fullscreen mode (0 = off, 1 = on)
fullscreen = 0

# Icon and splash (optional)
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/splash.png

# Permissions (add INTERNET if using API/webhook)
android.permissions = INTERNET

# Use private internal storage
android.private_storage = True

# Enable backup
android.allow_backup = True

# Copy .py files instead of compiling into libpymodules.so
android.copy_libs = 1

# Python bytecode compilation
# android.no-byte-compile-python = False

# Versioning: override versionCode if needed
# android.numeric_version = 1

# Logging level
log_level = 2


[buildozer]

# Warn if running as root
warn_on_root = 1

# Output and build directories (optional customization)
# build_dir = ./.buildozer
# bin_dir = ./bin
