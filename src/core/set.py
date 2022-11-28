#!/usr/bin/env python3
# coding=utf-8

import shutil
import os
import re
import sys

from src.core.asenacore import *
from src.core import text

me = mod_name()

# define path and set it to the Asena root dir
definepath = os.getcwd()
sys.path.append(definepath)

# grab the operating system
operating_system = check_os()

define_version = get_version()


def all_cat():

    # banner and main menu texts
    show_banner(define_version)
    # user input: show main menu
    debug_msg(me, "printing 'text.main'", 5)
    show_main_menu = create_menu(text.main_text, text.main)

    while 1:

        def information_gathering():
            try:
                # b/c below
                # main_menu_choice = (input(asenaprompt("2", "")))
                print(asenaprompt('2',''),end='')
                main_menu_choice = input_str()

                if main_menu_choice == 'back':
                    # https://stackoverflow.com/questions/66665217/how-to-import-a-python-script-without-a-py-extension
                    # https://stackoverflow.com/questions/2601047/import-a-python-module-without-the-py-extension
                    # https://gist.github.com/mportesdev/afb2ec26021ccabee0f67d6f7d18be3f

                    from importlib.util import spec_from_loader, module_from_spec
                    from importlib.machinery import SourceFileLoader

                    spec = spec_from_loader("asena", SourceFileLoader("asena",definepath+"/asena"))
                    test = module_from_spec(spec)
                    spec.loader.exec_module(test)

                # quit out
                if main_menu_choice == 'exit' or main_menu_choice == "quit":
                    exit_asena()

                # clear menu
                if main_menu_choice == 'clear':
                    clear()

                if main_menu_choice == 'banner':
                    show_graphic()

                if main_menu_choice == '1':  # 'Spearphishing Attack Vectors
                    while 1:
                    # user input: show spearphish menu
                        debug_msg(me, "printing 'text.spearphish_menu'", 5)
                        show_spearphish_menu = create_menu(
                            text.spearphish_text, text.spearphish_menu)
                        spearphish_menu_choice = input(asenaprompt(["1"], ""))

                        if spearphish_menu_choice == 'exit':
                            exit_asena()

                        if spearphish_menu_choice == 'help':
                            print(text.spearphish_text)

                        # Spearphish menu choice 1: Perform a Mass Email Attack
                        if spearphish_menu_choice == '1':
                            sys.path.append(definepath + "/src/core/msf_attacks/")
                            debug_msg(
                                me, "importing 'src.core.msf_attacks.create_payload'", 1)
                            # try:
                            #     module_reload(create_payload)
                            # except:

                        # Spearphish menu choice 2: Create a FileFormat Payload
                        if spearphish_menu_choice == '2':
                            sys.path.append(definepath + "/src/core/msf_attacks/")
                            debug_msg(
                                me, "importing 'src.core.msf_attacks.create_payload'", 1)
                            try:
                                # reload(create_payload)
                                pass
                            except:
                                # import create_payload
                                pass
                        # Spearphish menu choice 3: Create a Social-Engineering
                        # Template
                        if spearphish_menu_choice == '3':
                            debug_msg(
                                me, "calling function 'custom_template' from 'src.core.setcore'", 3)
                            # custom_template()
                        # Spearphish menu choice 99
                        if spearphish_menu_choice == '99':
                            break

                # Main Menu choice 10: Third Party Modules
                if main_menu_choice == '2':
                    sys.path.append(definepath + "/src/core")
                    debug_msg(me, "importing 'src.core.module_handler'", 1)

                # Define Auto-Infection USB/CD Method here
                if main_menu_choice == '3':
                        # Main Menu choice 3: Infectious Media Generator
                    debug_msg(me, "printing 'text.infectious_menu'", 5)
                    show_infectious_menu = create_menu(
                        text.infectious_text, text.infectious_menu)
                    infectious_menu_choice = input(asenaprompt(["3"], ""))

                    if infectious_menu_choice == 'exit':
                        exit_asena()

                    if infectious_menu_choice == "99":
                        menu_back()

                    if infectious_menu_choice == "":
                        infectious_menu_choice = "1"

                    # if fileformat
                    if infectious_menu_choice == "1":
                        ipaddr = input(
                            asenaprompt(["3"], "IP address for the reverse connection (payload)"))
                        # update_options("IPADDR=" + ipaddr)

                    filewrite1 = open(userconfigpath + "payloadgen", "w")
                    filewrite1.write("payloadgen=solo")
                    filewrite1.close()

                    # if choice is file-format
                    if infectious_menu_choice == "1":
                        filewrite = open(userconfigpath + "fileformat.file", "w")
                        filewrite.write("fileformat=on")
                        filewrite.close()
                        sys.path.append(definepath + "/src/core/msf_attacks/")
                        debug_msg(
                            me, "importing 'src.core.msf_attacks.create_payload'", 1)
                        # try:
                        #     module_reload(create_payload)
                        # except:
                        #     import create_payload

                    # if choice is standard payload
                    if infectious_menu_choice == "2":
                        # trigger set options for infectious media
                        update_options("INFECTION_MEDIA=ON")
                        # try:
                        #     # import src.core.payloadgen.solo
                        # except:
                        #     module_reload(src.core.payloadgen.solo)

                    # if we aren't exiting, then launch autorun
                    if infectious_menu_choice != "99":
                        # try:
                        #     import src.autorun.autolaunch
                        # except:
                        #     module_reload(src.autorun.autolaunch)
                        pass

                # Main Menu choice 4: Create a Payload and Listener
                if main_menu_choice == '4':
                    update_options("PAYLOADGEN=SOLO")

                # Main Menu choice 5: Mass Mailer Attack
                if main_menu_choice == '5':
                    debug_msg(me, "importing 'src.phishing.smtp.client.smtp_web'", 1)

                # Main Menu choice 6: Teensy USB HID Attack Vector
                if main_menu_choice == '6':

                    #
                    # USER INPUT: SHOW TEENSY MENU             #
                    #
                    debug_msg(me, "printing 'text.teensy_menu'", 5)
                    show_teensy_menu = create_menu(text.teensy_text, text.teensy_menu)
                    teensy_menu_choice = input(asenaprompt(["6"], ""))

                    if teensy_menu_choice == 'exit':
                        exit_asena()

                    # if not return to main menu
                    yes_or_no = ''

                    if teensy_menu_choice != "99":
                        # set our teensy info file in program junk
                        filewrite = open(userconfigpath + "teensy", "w")
                        filewrite.write(teensy_menu_choice + "\n")
                        if teensy_menu_choice != "3" and teensy_menu_choice != "7" and teensy_menu_choice != "8" and teensy_menu_choice != "9" and teensy_menu_choice != "10" and teensy_menu_choice != "11" and teensy_menu_choice != "12" and teensy_menu_choice != "13" and teensy_menu_choice != "14":
                            yes_or_no = yesno_prompt(
                                "0", "Do you want to create a payload and listener [yes|no]: ")
                            if yes_or_no == "YES":
                                filewrite.write("payload")
                                filewrite.close()
                                # load a payload
                                sys.path.append(definepath + "/src/core/payloadgen")
                                debug_msg(
                                    me, "importing 'src.core.payloadgen.create_payloads'", 1)
                                # try:
                                #     module_reload(create_payloads)
                                # except:
                                #     import create_payloads
                        if yes_or_no == "NO":
                            filewrite.close()
                        # need these default files for web server load
                        filewrite = open(userconfigpath + "site.template", "w")
                        filewrite.write("TEMPLATE=CUSTOM")
                        filewrite.close()
                        filewrite = open(userconfigpath + "attack_vector", "w")
                        filewrite.write("hid")
                        filewrite.close()
                        # if we are doing binary2teensy
                        if teensy_menu_choice != "7" and teensy_menu_choice != "8" and teensy_menu_choice != "9" and teensy_menu_choice != "10" and teensy_menu_choice != "11" and teensy_menu_choice != "12" and teensy_menu_choice != "14":
                            sys.path.append(definepath + "/src/teensy")
                            debug_msg(me, "importing 'src.teensy.teensy'", 1)
                            # try:
                            #     module_reload(teensy)
                            # except:
                            #     import teensy
                        if teensy_menu_choice == "7":
                            debug_msg(me, "importing 'src.teensy.binary2teensy'", 1)
                            # import src.teensy.binary2teensy
                        # if we are doing sd2teensy attack
                        if teensy_menu_choice == "8":
                            debug_msg(me, "importing 'src.teensy.sd2teensy'", 1)
                            # import src.teensy.sd2teensy

                        # if we are doing the sd2teensy osx attack
                        if teensy_menu_choice == "9":
                            print_status(
                                "Generating the SD2Teensy OSX ino file for you...")
                            if not os.path.isdir(userconfigpath + "reports/osx_sd2teensy"):
                                os.makedirs(userconfigpath + "reports/osx_sd2teensy")
                            shutil.copyfile("src/teensy/osx_sd2teensy.ino",
                                            "%s/reports/osx_sd2teensy/osx_sd2teensy.ino" % (userconfigpath))
                            print_status(
                                "File has been exported to ~/.set/reports/osx_sd2teensy/osx_sd2teensy.ino")
                            return_continue()

                        # if we are doing the X10 Arduino Sniffer
                        if teensy_menu_choice == "10":
                            print_status(
                                "Generating the Arduino sniffer and libraries ino..")
                            if not os.path.isdir(userconfigpath + "reports/arduino_sniffer"):
                                os.makedirs(userconfigpath + "reports/arduino_sniffer")
                            shutil.copyfile("src/teensy/x10/x10_sniffer.ino",
                                            userconfigpath + "reports/arduino_sniffer/x10_sniffer.ino")
                            shutil.copyfile("src/teensy/x10/libraries.zip",
                                            userconfigpath + "reports/arduino_sniffer/libraries.zip")
                            print_status(
                                "Arduino sniffer files and libraries exported to ~/.set/reports/arduino_sniffer")
                            return_continue()

                        # if we are doing the X10 Jammer
                        if teensy_menu_choice == "11":
                            print_status(
                                "Generating the Arduino jammer ino and libraries...")
                            if not os.path.isdir(userconfigpath + "reports/arduino_jammer"):
                                os.makedirs(userconfigpath + "reports/arduino_jammer")
                            shutil.copyfile("src/teensy/x10/x10_blackout.ino",
                                            userconfigpath + "reports/arduino_jammer/x10_blackout.ino")
                            shutil.copyfile("src/teensy/x10/libraries.zip",
                                            userconfigpath + "reports/arduino_jammer/libraries.zip")
                            print_status(
                                "Arduino jammer files and libraries exported to ~/.set/reports/arduino_jammer")
                            return_continue()

                        # powershell shellcode injection
                        if teensy_menu_choice == "12":
                            print_status(
                                "Generating the Powershell - Shellcode injection ino..")
                            debug_msg(
                                me, "importing 'src.teensy.powershell_shellcode'", 1)
                            # import src.teensy.powershell_shellcode

                # HID Msbuild compile to memory Shellcode Attack
                        if teensy_menu_choice == "14":
                            print_status(
                                "HID Msbuild compile to memory Shellcode Attack selected")
                            debug_msg(
                                me, "importing '-----file-----'", 1)
                            # import src.teensy.ino_gen

                    if teensy_menu_choice == "99":
                        teensy_menu_choice = None

                # Main Menu choice 7: Wireless Attack Point Attack Vector
                if main_menu_choice == '7':

                    if operating_system == "windows":
                        print_warning(
                            "Sorry. The wireless attack vector is not yet supported in Windows.")
                        return_continue()

                    if operating_system != "windows":
                        # set path to nothing
                        airbase_path = ""
                        dnsspoof_path = ""
                        # need to pull the SET config file
                        fileopen = open("/etc/setoolkit/set.config", "r")
                        for line in fileopen:
                            line = line.rstrip()
                            match = re.search("AIRBASE_NG_PATH=", line)
                            if match:
                                airbase_path = line.replace("AIRBASE_NG_PATH=", "")

                            match1 = re.search("DNSSPOOF_PATH=", line)
                            if match1:
                                dnsspoof_path = line.replace("DNSSPOOF_PATH=", "")

                        if not os.path.isfile(airbase_path):
                            if not os.path.isfile("/usr/local/sbin/airbase-ng"):
                                print_warning(
                                    "Warning airbase-ng was not detected on your system. Using one in SET.")
                                print_warning(
                                    "If you experience issues, you should install airbase-ng on your system.")
                                print_warning(
                                    "You can configure it through the set_config and point to airbase-ng.")
                                airbase_path = ("src/wireless/airbase-ng")
                            if os.path.isfile("/usr/local/sbin/airbase-ng"):
                                airbase_path = "/usr/local/sbin/airbase-ng"

                        if not os.path.isfile(dnsspoof_path):
                            if os.path.isfile("/usr/local/sbin/dnsspoof"):
                                dnsspoof_path = "/usr/local/sbin/dnsspoof"
                            if os.path.isfile("/usr/sbin/dnsspoof"):
                                dnsspoof_path = "/usr/sbin/dnsspoof"

                        # if we can find airbase-ng
                        if os.path.isfile(airbase_path):
                            if os.path.isfile(dnsspoof_path):
                                # start the menu here
                                while 1:

                                        #
                                        # USER INPUT: SHOW WIRELESS MENU           #
                                        #
                                    debug_msg(
                                        me, "printing 'text.wireless_attack_menu'", 5)
                                    show_wireless_menu = create_menu(
                                        text.wireless_attack_text, text.wireless_attack_menu)
                                    wireless_menu_choice = input(
                                        asenaprompt(["8"], ""))
                                    # if we want to start access point
                                    if wireless_menu_choice == "1":
                                        sys.path.append(definepath + "/src/wireless/")
                                        debug_msg(
                                            me, "importing 'src.wireless.wifiattack'", 1)
                                        # try:
                                        #     module_reload(wifiattack)
                                        # except:
                                        #     # import wifiattack
                                        #     pass

                                    # if we want to stop the wifi attack
                                    if wireless_menu_choice == "2":
                                        sys.path.append(definepath + "/src/wireless/")
                                        debug_msg(
                                            me, "importing 'src.wireless.stop_wifiattack'", 1)
                                        # try:
                                        #     module_reload(stop_wifiattack)
                                        # except:
                                        #     import stop_wifiattack

                                    # if we want to return to the main menu
                                    if wireless_menu_choice == "99":
                                        print (" [*] Returning to the main menu ...")
                                        break

                        if not os.path.isfile(dnsspoof_path):
                            if not os.path.isfile("/usr/local/sbin/dnsspoof"):
                                print_error(
                                    "ERROR:DNS Spoof was not detected. Check the set_config file.")
                                return_continue()

                # Main Menu choice 8: QRCode Generator
                if main_menu_choice == '8':
                        try:
                            from PIL import Image, ImageDraw
                            # from src.qrcode.qrgenerator import *
                            print("""
            The QRCode Attack Vector will create a QRCode for you with whatever URL you want.

            When you have the QRCode Generated, select an additional attack vector within SET and
            deploy the QRCode to your victim. For example, generate a QRCode of the SET Java Applet
            and send the QRCode via a mailer.
            """)
                            url = input(
                                "Enter the URL you want the QRCode to go to (99 to exit): ")
                            if url != "99":
                                # if the reports directory does not exist then create it
                                if not os.path.isdir("%s/reports" % (userconfigpath)):
                                    os.makedirs("%s/reports" % (userconfigpath))
                                # gen_qrcode(url)
                                return_continue()

                        except ImportError:
                            print_error(
                                "This module requires PIL (Or Pillow) and qrcode to work properly.")
                            print_error(
                                "Just do pip install Pillow; pip install qrcode")
                            print_error(
                                "Else refer to here for installation: http://pillow.readthedocs.io/en/3.3.x/installation.html")
                            return_continue()

                # Main Menu choice 9: Third Party Modules
                if main_menu_choice == '9':
                        sys.path.append(definepath + "/src/core")
                        debug_msg(me, "importing 'src.core.module_handler'", 1)

                # Main Menu choice 10: Third Party Modules
                if main_menu_choice == '10':
                    sys.path.append(definepath + "/src/core")
                    debug_msg(me, "importing 'src.core.module_handler'", 1)

            except KeyboardInterrupt:
                sys.stdout.write(f'\r{asenaprompt("2", "")}Interrupt: use the "exit" command to quit \n')
                information_gathering()


        information_gathering()


all_cat()