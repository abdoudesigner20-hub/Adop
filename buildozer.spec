[app]

title = Currency Converter Pro
package.name = currencyconverter
package.domain = org.abdoudessigner

source.dir = .
source.include_exts = py,png,jpg,jpeg,mp3,json

version = 1.0

requirements = python3,kivy,requests,kivmob,

orientation = portrait

fullscreen = 0

android.permissions = INTERNET

android.api = 33
android.minapi = 21

android.gradle_dependencies = com.google.android.gms:play-services-ads:22.6.0

android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True

android.private_storage = True

android.logcat_filters = *:S python:D
