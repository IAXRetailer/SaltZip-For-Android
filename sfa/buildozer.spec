[app]

title = SaltZip
package.name = saltzip
package.domain = com.h2sxxa.saltzip

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

version = 0.1
requirements = python3,kivy,pyDes,rarfile
icon.filename=icon.png

orientation = portrait
fullscreen = 0
android.arch = armeabi-v7a

android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

[buildozer]
log_level = 2