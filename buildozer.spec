[app]

# اسم التطبيق الذي سيظهر على الهاتف
title = Currency Converter Pro

# اسم الحزمة (يجب أن يكون فريداً وبدون مسافات)
package.name = currency_pro_app

# النطاق (يمكنك تركه كما هو أو تغييره)
package.domain = org.abdoudesigner

# الامتدادات التي يجب تضمينها (أضفنا mp3 و json و png لأن كودك يستخدمها)
source.include_exts = py, png, jpg, kv, atlas, json, mp3

# المتطلبات البرمجية (Requirements) - حيوية جداً لكودك
# لاحظ إضافة openssl لدعم روابط https في مكتبة requests
requirements = python3, kivy==2.2.1, kivymd, requests, pillow, certifi, openssl, kivmob

# الصلاحيات التي يحتاجها تطبيقك
# يحتاج إنترنت لجلب العملات وعرض الإعلانات
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (int) Target Android API (يفضل 33 حالياً لمتجر جوجل)
android.api = 33

# (int) Minimum API
android.minapi = 21

# (str) Android NDK version (متوافق مع Buildozer Action)
android.ndk = 25b

# المعماريات المدعومة (لضمان عمله على أغلب الهواتف)
android.archs = arm64-v8a, armeabi-v7a

# قبول التراخيص تلقائياً (مهم لـ GitHub Actions)
android.accept_sdk_license = True

# إضافة مكتبات Gradle الخاصة بالإعلانات (مهم لـ KivMob)
android.gradle_dependencies = 'com.google.android.gms:play-services-ads:22.0.0'

[buildozer]
log_level = 2
