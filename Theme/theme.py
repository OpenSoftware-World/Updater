""" Copyright© 2025-2026 OpenSoftware-World
Updater Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
Updater All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/OpenSoftware-World/Updater
A Copy of This Software is published on GitHub To view: https://github.com/OpenSoftware-World/Updater """

"""
This file the theme.py file stores the appearance settings for the application called Updater.

The theme file specified by the user is read, and then the necessary variables are created based on that file and made available to the application.

Note: You can modify this file to suit your own design or layout needs, but you must verify that your changes are compatible with updater.py.
"""

import configparser

theme_file_config = configparser.ConfigParser()
theme_file_config.read('Theme/theme_file.ini')

name = theme_file_config['ThemeDataFile']['name']

theme_config = configparser.ConfigParser()
theme_config.read(f'Theme/{name}')

icon = theme_config['Icon']['icon']
userTheme = theme_config['ThemeSettings']['userTheme']
pywinstyles_theme = theme_config['ThemeSettings']['pywinstyles_theme']
userFont = theme_config['FontSettings']['userFont']
userFontSize = int(theme_config['FontSettings']['userFontSize'])
userTitleFontSize = int(theme_config['FontSettings']['userTitleFontSize'])
userFontBold = theme_config['FontSettings']['userFontBold']
userCornerRadiusValue = int(theme_config['CornerRadiusSettings']['userCornerRadiusValue'])

userButtonColor = theme_config['ButtonAppearanceSettings']['userButtonColor']
userButtonHoverColor = theme_config['ButtonAppearanceSettings']['userButtonHoverColor']
userButtonTextColor = theme_config['ButtonAppearanceSettings']['userButtonTextColor']
userButtonBorderColor = theme_config['ButtonAppearanceSettings']['userButtonBorderColor']
userButtonBorderWidth = theme_config['ButtonAppearanceSettings']['userButtonBorderWidth']
userWindowTitleColor = theme_config['WindowSettings']['userWindowTitleColor']
w_default_res = theme_config['WindowSettings']['w_default_res']
w_res = theme_config['WindowSettings']['w_res']
updater_btn_place_x = int(theme_config['WindowSettings']['updater_btn_place_x'])

if userFontBold == "False":
    userFontBold = "normal"
else:
    userFontBold = "bold"

if userButtonColor == "default":
    userButtonColor = None

if userButtonHoverColor == "default":
    userButtonHoverColor = None

if userButtonTextColor == "default":
    userButtonTextColor = None

if userButtonBorderColor == "default":
    userButtonBorderColor = None

if userButtonBorderWidth == "default":
    userButtonBorderWidth = None
else:
    userButtonBorderWidth = int(userButtonBorderWidth)

if userWindowTitleColor == "default":
    userWindowTitleColor = None