from tkinter import PhotoImage
import customtkinter, zipfile, os, shutil, platform
from CTkMessagebox import CTkMessagebox
from UpdaterSettings.updater_settings import *
from Theme.theme import *
from Lang.lang import *
if platform.system() == "Windows":
    import pywinstyles
else:
    print("Note: The “pywinstyles” library has not been imported. You must be using the Windows operating system to import the “pywinstyles” library. (Rest assured, it won't significantly affect the app's performance.)")

"""
This file, updater.py, is the main file of the application called Updater. It checks for updates by retrieving the necessary information from all other configuration files and helper files, and if an update is available, it allows you to download and install it.

Note: You can modify this file to suit your needs, ensuring it is compatible with the relevant configuration files and supporting files.
"""

def updater():
    download = requests.get(file_url, stream=True)
    with open(file_name, "wb") as f:
        for chunk in download.iter_content(chunk_size):
            if chunk:
                f.write(chunk)
    with zipfile.ZipFile(file_name, 'r') as zip_ext:
        zip_ext.extractall()
        update_notification = CTkMessagebox(title=f"{updater_msg_box}", message=f"{software_name} {new_ver} {updater_msg_box_details}", option_1=f"{complete_update}", option_2=f"{option_close}")
        response = update_notification.get()

        if response == complete_update:
            main_folder = os.path.dirname(os.path.abspath(__file__))
            update_folder = os.path.join(main_folder, update_folder_name)

            for item in os.listdir(update_folder):
                src = os.path.join(update_folder, item)
                dist = os.path.join(main_folder, item)

                if os.path.exists(dist):
                    if os.path.isfile(dist) or os.path.islink(dist):
                        os.remove(dist)
                    elif os.path.isdir(dist):
                        shutil.rmtree(dist)
                shutil.move(src, dist)
            os.rmdir(update_folder)

current_ver = open(current_ver_file, "r").read()

window = customtkinter.CTk()
window.title(f"{software_name} {w_title}")
window.geometry(w_default_res)
window.resizable(False, False)
window.iconphoto(False, PhotoImage(file=icon))

if new_ver > current_ver:
    label = customtkinter.CTkLabel(master=window, text=f"{new_update} {software_name} {new_update_}", font=(userFont, userTitleFontSize, userFontBold))
    label.place(x=0)
    new_ver_label = customtkinter.CTkLabel(master=window, text=f"{new_version} {new_ver}", font=(userFont, userFontSize, userFontBold))
    new_ver_label.place(x=0, y=30)
    current_ver_label = customtkinter.CTkLabel(master=window, text=f"{current_version} {current_ver}", font=(userFont, userFontSize, userFontBold))
    current_ver_label.place(x=0, y=52)
    update = customtkinter.CTkButton(master=window, text=f"{update_btn}", font=(userFont, userFontSize, userFontBold), command=updater, corner_radius=userCornerRadiusValue, fg_color=userButtonColor, hover_color=userButtonHoverColor, text_color=userButtonTextColor, border_color=userButtonBorderColor, border_width=userButtonBorderWidth)
    update.place(x=updater_btn_place_x, y=55)
else:
    window.geometry(w_res)
    if lang == "tr":
        label = customtkinter.CTkLabel(master=window, text=f"{software_name} {software_name_last_ver}", font=(userFont, userFontSize, userFontBold))
    elif lang == "en":
        label = customtkinter.CTkLabel(master=window, text=f"{software_name_last_ver} {software_name}", font=(userFont, userFontSize, userFontBold))
    label.place(x=0)
    current_ver_label = customtkinter.CTkLabel(master=window, text=f"{current_version} {current_ver}", font=(userFont, userFontSize, userFontBold))
    current_ver_label.place(x=0, y=30)

if platform.system() == "Windows":
    pywinstyles.apply_style(window, pywinstyles_theme)
customtkinter.set_appearance_mode(userTheme)

window.mainloop()