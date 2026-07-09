""" Copyright© 2025-2026 OpenSoftware-World
Updater Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
Updater All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/OpenSoftware-World/Updater
A Copy of This Software is published on GitHub To view: https://github.com/OpenSoftware-World/Updater """

"""
This file the lang.py file enables the language system of the application called Updater to function.

When the user changes the lang variable in the Lang/lang.ini file, the software reads that file that is, the .ini file specified by the user and then creates all the variables based on that file.

Warning: Unless you want to make a very specific change, it is recommended that you do not modify this file.
"""

import configparser

lang_config = configparser.ConfigParser()
lang_config.read('Lang/lang.ini')

lang = lang_config['AppLang']['lang']

langconfig = configparser.ConfigParser()
langconfig.read(f'Lang/{lang}.ini')

software_name = langconfig['LangContent']['software_name']
w_title = langconfig['LangContent']['w_title']
new_update = langconfig['LangContent']['new_update']
new_update_ = langconfig['LangContent']['new_update_']
new_version = langconfig['LangContent']['new_version']
current_version = langconfig['LangContent']['current_version']
update_btn = langconfig['LangContent']['update_btn']
software_name_last_ver = langconfig['LangContent']['software_name_last_ver']
updater_msg_box = langconfig['LangContent']['updater_msg_box']
updater_msg_box_details = langconfig['LangContent']['updater_msg_box_details']
complete_update = langconfig['LangContent']['complete_update']
option_close = langconfig['LangContent']['option_close']