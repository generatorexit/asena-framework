#!/usr/bin/env python

# centralized core modules for Asena
import os
import sys
import re
import time
import datetime
import random
import shutil
import subprocess
import string
import inspect
from urllib.request import urlopen
import multiprocessing
from functools import *

from src.core import dictionaries


# class for colors
class bcolors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERL = '\033[4m'
    ENDC = '\033[0m'
    backBlack = '\033[40m'
    backRed = '\033[41m'
    backGreen = '\033[42m'
    backYellow = '\033[43m'
    backBlue = '\033[44m'
    backMagenta = '\033[45m'
    backCyan = '\033[46m'
    backWhite = '\033[47m'

# an understandable class
class create_menu:

    def __init__(self, text, menu):
        self.text = text
        self.menu = menu
        print(text)
        for i, option in enumerate(menu):

            menunum = i + 1
            # Check to see if this line has the 'return to main menu' code
            match = re.search("0D", option)
            # If it's not the return to menu line:
            if not match:
                if menunum < 10:
                    print(f"{menunum} -> {option}")
                else:
                    print(f"{menunum} > {option}")
            else:
                print('\n99 -> Return to Main Menu\n')
        return

# check operating system
def check_os():
    if os.name == "nt":
        operating_system = "windows"
    if os.name == "posix":
        operating_system = "posix"
    return operating_system

# get version for asena
def get_version():
    define_version = open("src/core/asena.version", "r").read().rstrip()
    # define_version = '1.0.0'
    return define_version

# update the Asena Framework
def update_asena():
    backbox = check_backbox()
    kali = check_kali()

    # if backbox == "BackBox": :(
    if backbox == "BackBox(sad)":
        print_status("You are running BackBox Linux which already implements Asena updates.")
        print_status("No need for further operations, just update your system.")
        time.sleep(2)

    # elif kali == "Kali": :(
    elif kali == "Kali(sad)":
        print_status("You are running Kali Linux which maintains Asena updates.")
        time.sleep(2)

    # if we aren't running Kali or BackBox :(
    else:
        # print_info("Kali or BackBox Linux not detected, manually updating..")
        print_info("Updating the Asena Framework, be patient...")
        print_info("Performing cleanup first...")
        subprocess.Popen("git clean -fd", shell=True).wait()
        print_info("Updating... This could take a little bit...")
        subprocess.Popen("git pull", shell=True).wait()
        print_status("The updating has finished, returning to main menu..")
        time.sleep(2)

# this is small area to generate the date and time
def date_time():
    now = str(datetime.datetime.today())
    return now

# this is small area to generate the time
def now():
    # seconds removed
    # clock = str(datetime.datetime.now().strftime("%H:%M:%S"))
    clock = str(datetime.datetime.now().strftime("%H:%M"))
    prnt = "[" + clock +"] "
    return prnt

# the main ~./asena path for Asena
def setdir():
    if check_os() == "posix":
        return os.path.join(os.path.expanduser('~'), '.asena' + '/')
    if check_os() == "windows":
        return "src/program_junk/"

# set the main directory for Asena
userconfigpath = setdir()

# get the main Asena path
def definepath():
    if check_os() == "posix":
        if os.path.isfile("asena"):
            return os.getcwd()
        else:
            return "/usr/share/asena-framework/"

    else:
        return os.getcwd()

# this will be the home for the asena menus
def asenaprompt(category, text):
    # if no special prompt and no text, return plain prompt
    if category == '0' and text == "":
        return bcolors.DARKCYAN + now() + bcolors.UNDERL + "asena" + bcolors.ENDC + " > "
    # if the loop is here, either category or text was positive
    # if it's the category that is blank... return prompt with only the text
    if category == '0':
        return bcolors.DARKCYAN + now() + bcolors.UNDERL + "asena" + bcolors.ENDC + " > " + text + ":"
    # category is NOT blank
    else:
        # initialize the base 'asena' prompt
        prompt = bcolors.DARKCYAN + now() + bcolors.UNDERL + "asena" + bcolors.ENDC
        # if there is a category but no text
        if text == "":
            for level in category:
                level = dictionaries.category(level)
                prompt += ":" + bcolors.UNDERL + \
                    bcolors.DARKCYAN + level + bcolors.ENDC
            promptstring = str(prompt)
            promptstring += " > "
            return promptstring
        # if there is both a category AND text
        else:
            # iterate through the list received
            for level in category:
                level = dictionaries.category(level)
                prompt += ":" + bcolors.UNDERL + \
                    bcolors.DARKCYAN + level + bcolors.ENDC
            promptstring = str(prompt)
            promptstring = promptstring + " > " + text + ":"
            return promptstring

def yesno_prompt(category, text):
    valid_response = False
    while not valid_response:
        response = input(asenaprompt(category, text))
        response = str.lower(response)
        if response == "no" or response == "n":
            response = "NO"
            valid_response = True
        elif response == "yes" or response == "y":
            response = "YES"
            valid_response = True
        else:
            print_warning("valid responses are 'n|y|N|Y|no|yes|No|Yes|NO|YES'")
    return response

def return_continue():
    print(("Press" + bcolors.RED + " {return} " + bcolors.ENDC + "to continue"))
    pause = input()

# runtime messages
def print_status(message):
    print(bcolors.GREEN + bcolors.BOLD + "[*] " + bcolors.ENDC + str(message))

def print_info(message):
    print(bcolors.BLUE + bcolors.BOLD + "[-] " + bcolors.ENDC + str(message))

def print_info_spaces(message):
    print(bcolors.BLUE + bcolors.BOLD + "  [-] " + bcolors.ENDC + str(message))

def print_warning(message):
    print(bcolors.YELLOW + bcolors.BOLD + "[!] " + bcolors.ENDC + str(message))

def print_error(message):
    print(bcolors.RED + bcolors.BOLD + "[!] " + bcolors.ENDC + bcolors.RED + str(message) + bcolors.ENDC)

# runtime inputs
def input_str():
    try:
        x = str(input())
        return x.lower().strip()
    except Exception as error:
        print("[!] Something went wrong. Printing the error: " + str(error))

def input_int():
    try:
        x = int(input())
        return str(x).lower().strip()
    except ValueError:
        print("[!] Value Error: Input must be an integer.")
    except Exception as error:
        print("[!] Something went wrong. Printing the error: " + str(error))

# DEBUGGING #######################
# ALWAYS ASENA TO ZERO BEFORE COMMIT!
DEBUG_LEVEL = 0
#  0 = Debugging OFF
#  1 = debug imports only
#  2 = debug imports with pause for <ENTER>
#  3 = imports, info messages
#  4 = imports, info messages with pause for <ENTER>
#  5 = imports, info messages, menus
#  6 = imports, info messages, menus with pause for <ENTER>

debugFrameString = '-' * 72

def debug_msg(currentModule, message, msgType):
    if DEBUG_LEVEL == 0:
        pass  # stop evaluation efficiently
    else:
        if msgType <= DEBUG_LEVEL:
            # a bit more streamlined
            print(bcolors.RED + "\nDEBUG_MSG: from module '" +
                  currentModule + "': " + message + bcolors.ENDC)

            if DEBUG_LEVEL == 2 or DEBUG_LEVEL == 4 or DEBUG_LEVEL == 6:
                input("waiting for <ENTER>\n")

# pull the help menu here
def help_menu():
    fileopen = open("README.md", "r").readlines()
    for line in fileopen:
        line = line.rstrip()
        print(line)
    fileopen = open("readme/CREDITS", "r").readlines()
    print("\n")
    for line in fileopen:
        line = line.rstrip()
        print(line)
    return_continue()

def mod_name():
    frame_records = inspect.stack()[1]
    calling_module = inspect.getmodulename(frame_records[1])
    return calling_module

# expand the filesystem windows directory
def windows_root():
    return os.environ['WINDIR']

# core log file routine for Asena
def log(error):
    try:
        # open log file only if directory is present (may be out of directory
        # for some reason)
        if not os.path.isfile("%s/src/logs/asena_logfile.log" % (definepath())):
            filewrite = open("%s/src/logs/asena_logfile.log" %
                             (definepath()), "w")
            filewrite.write("")
            filewrite.close()
        if os.path.isfile("%s/src/logs/asena_logfile.log" % (definepath())):
            error = str(error)
            # open file for writing
            filewrite = open("%s/src/logs/asena_logfile.log" %
                             (definepath()), "a")
            # write error message out
            filewrite.write("ERROR: " + date_time() + ": " + error + "\n")
            # close the file
            filewrite.close()
    except IOError as err:
        pass

# generate a random string
def generate_random_string(low, high):
    length = random.randint(low, high)
    letters = string.ascii_letters # + string.digits
    return ''.join([random.choice(letters) for _ in range(length)])

# upx encoding and modify binary
def upx(path_to_file):
    # open the asena_config
    fileopen = open("/etc/asena/asena.config", "r")
    for line in fileopen:
        line = line.rstrip()
        match = re.search("UPX_PATH=", line)
        if match:
            upx_path = line.replace("UPX_PATH=", "")

    # if it isn't there then bomb out
    if not os.path.isfile(upx_path):
        print_warning(
            "UPX was not detected. Try configuring the asena_config again.")

    # if we detect it
    if os.path.isfile(upx_path):
        print_info(
            "Packing the executable and obfuscating PE file randomly, one moment.")
        # packing executable
        subprocess.Popen(
            "%s -9 -q -o %s/temp.binary %s" % (upx_path, userconfigpath, path_to_file),
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
        # move it over the old file
        subprocess.Popen("mv %s/temp.binary %s" % (userconfigpath, path_to_file),
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()

        # random string
        random_string = generate_random_string(3, 3).upper()

        # 4 upx replace - we replace 4 upx open the file
        fileopen = open(path_to_file, "rb")
        filewrite = open(userconfigpath + "temp.binary", "wb")

        # read the file open for data
        data = fileopen.read()
        # replace UPX stub makes better evasion for A/V
        filewrite.write(data.replace("UPX", random_string, 4))
        filewrite.close()
        # copy the file over
        subprocess.Popen("mv %s/temp.binary %s" % (userconfigpath, path_to_file),
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
    time.sleep(3)

def show_banner():
    if check_os() == "posix":
        os.system("clear")
    if check_os() == "windows":
        os.system("cls")
    show_graphic()

    # here we check if there is a new version of asena - if there is, then
    # display a banner
    vc = get_version()

    # pull version
    try:
        version = ''
        def pull_version():
            if not os.path.isfile(userconfigpath + "version.lock"):
                try:
                    url = ('https://raw.githubusercontent.com/generatorexit/asena-framework/master/src/core/asena.version')
                    version = urlopen(url).read().rstrip().decode('utf-8')
                    filewrite = open(userconfigpath + 'version.lock', 'w')
                    filewrite.write(version)
                    filewrite.close()

                except KeyboardInterrupt:
                    version = "Keyboard Interrupt"

            else:
                version = open(userconfigpath + "version.lock", "r").read()

            if vc != version:
                if version != '':
                    print("\n"
                    "Your version   : " + vc + "\n"
                    "Current version: " + version + "\n"
                    "There is a new version of Asena Framework available.\n")

        # why urllib and sockets cant control DNS resolvers is beyond me - so
        # we use this as a hack job to add a delay and kill if updates are
        # taking too long
        p = multiprocessing.Process(target=pull_version)
        p.start()

        # Wait for 5 seconds or until process finishes
        p.join(8)

        # If thread is still active
        if p.is_alive():
            print(
                bcolors.RED + " Unable to check for new version of Asena (is your network up?)\n" + bcolors.ENDC)
            # terminate the process
            p.terminate()
            p.join()

    except Exception as err:
        print(err)

def show_graphic():
    banner = random.randrange(1, 9)

    if banner == 1:
        print(bcolors.YELLOW + f"""
   ________________________________________________
  |:                                         ``::%H|
  |%:.        {bcolors.CYAN}The Asena Framework{bcolors.ENDC} v{get_version()}{bcolors.YELLOW}        `:%|
  |H%::.._________________________________________:|""" + bcolors.ENDC)

    if banner == 2:
        print(fr"""
         {bcolors.YELLOW}_{bcolors.ENDC}               A  a u
        {bcolors.YELLOW}(_){bcolors.ENDC}       {bcolors.CYAN}__/7{bcolors.ENDC} A        U 
\               {bcolors.CYAN}c' ^C{bcolors.ENDC}             U                     WWWWWWW
 >   {bcolors.CYAN},---.--.__.{{,/'{bcolors.ENDC}               UUU         WWWWWW
 _  {bcolors.CYAN}'^^' )_,_  . `/{bcolors.ENDC}      .--.           UUUUUW
' \     {bcolors.CYAN}< \  `--)/|{bcolors.ENDC}   `---._ \ ^.
 .--._          {bcolors.CYAN}/ `{bcolors.ENDC}         `--..-._           _________..---------
'   / `--._              /\_.    `---._____.--'             v{get_version()}""" + bcolors.ENDC)

    if banner == 3:
        print(bcolors.GREEN + fr"""
         _..:::.._
       .:::::{bcolors.CYAN}/|{bcolors.GREEN}::::.
      ::::::{bcolors.CYAN}/ V|{bcolors.GREEN}:::::
     ::::::{bcolors.CYAN}/'  |{bcolors.GREEN}::::::
     ::::{bcolors.CYAN}<_,   ({bcolors.GREEN}::::::
      :::::{bcolors.CYAN}|    \{bcolors.GREEN}::::
       '::{bcolors.CYAN}/      \{bcolors.GREEN}:'{bcolors.ENDC}   v{get_version()}""" + bcolors.ENDC)

    if banner == 4:
        print(bcolors.CYAN + rf"""
         _     ___
        #_~`--'__ `===-,
        `.`.     `#.,//
        ,_\_\     ## #\
        `__.__    `####\
             ~~\ ,###'~
                \##'   v{get_version()}""" + bcolors.ENDC)

    if banner == 5:
        print(bcolors.ENDC + rf"""
               .-'''''-.
             .'         `.
            :             :
           :               :
           :      {bcolors.CYAN}_/|{bcolors.ENDC}      :
            :   {bcolors.CYAN}=/_/{bcolors.ENDC}      :
             `.{bcolors.CYAN}_/ |{bcolors.ENDC}     .'
          {bcolors.CYAN}(   /  ,|{bcolors.ENDC}...-'
           {bcolors.CYAN}\_/^\/||{bcolors.YELLOW}__
        _/~  `""~`"` \_
     __/  -'/  `-._ `\_\__   {bcolors.ENDC}v{get_version()}{bcolors.YELLOW}
   /     /-'`  `\   \  \-.\ """ + bcolors.ENDC)

    if banner == 6:
        print(bcolors.CYAN + rf"""
                     .
                    / V\
                  / `  /
                 <<   |
                 /    |
               /      |
             /        |
           /    \  \ /
          (      ) | |  
  ________|   _/_  | |
<__________\______)\__)   {bcolors.ENDC}v{get_version()}""" + bcolors.ENDC)

    if banner == 7:
        print(bcolors.CYAN + rf"""
         /\
     _  / |
    (  /  |  .    .  .-.  . ,';. .-.
     `/.__|_.'  .';.;.-'  ;;  ;;;   :
 .:' /    |   .' .' `:::'';  ;; `:::'-'
(__.'     `-''           ;    `.   {bcolors.ENDC}v{get_version()}""" + bcolors.ENDC)

    if banner == 8:
        print(bcolors.backBlack + rf'''
 ____________________________________________________
|[] {bcolors.CYAN}The Asena Framework{bcolors.ENDC}{bcolors.backBlack} v{get_version()}                 [-]|X|
|"""""""""""""""""""""""""""""""""""""""""""""""""|"|
|{bcolors.CYAN}asena{bcolors.ENDC}{bcolors.backBlack} > use mksec                                | |
|{bcolors.CYAN}asena{bcolors.ENDC}{bcolors.backBlack}:(mksec) > help                             | |
|                                                 | |
|                                                 |_|
|_________________________________________________|/|''' + bcolors.ENDC)

# identify if set interactive shells are disabled
def set_check():
    fileopen = open("/etc/asena/asena.config", "r")
    for line in fileopen:
        match = re.search("SET_INTERACTIVE_SHELL=OFF", line)
        # if we turned it off then we return a true else return false
        if match:
            return True
        match1 = re.search("SET_INTERACTIVE_SHELL=ON", line)
        # return false otherwise
        if match1:
            return False

# if the user specifies 99
def menu_back():
    print_info("Returning to the previous menu...")

#clear menu
def clear():
    if check_os == "posix":
        os.system("clear")
    else:
        os.system("clear")

# routine for checking length of a payload: variable equals max choice
def check_length(choice, max):
    # start initital loop
    counter = 0
    while 1:
        if counter == 1:
            choice = input(bcolors.YELLOW + bcolors.BOLD +
                               "[!] " + bcolors.ENDC + "Invalid choice try again: ")
        # try block in case its not a integer
        try:
            # check to see if its an integer
            choice = int(choice)
            # okay its an integer lets do the compare
            if choice > max:
                # trigger an exception as not an int
                choice = "blah"
                choice = int(choice)
            # if everythings good return the right choice
            return choice
        # oops, not a integer
        except Exception:
            counter = 1

# kill certain processes
def kill_proc(port, flag):
    proc = subprocess.Popen("netstat -antp | grep '%s'" %
                            (port), shell=True, stdout=subprocess.PIPE)
    stdout_value = proc.communicate()[0]
    a = re.search("\d+/%s" % (flag), stdout_value)
    if a:
        b = a.group()
        b = b.replace("/%s" % (flag), "")
        subprocess.Popen("kill -9 %s" % (b), stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, shell=True).wait()

# check the config file and return value
def check_config(param):
    fileopen = open("/etc/asena/asena.config", "r")
    for line in fileopen:
        line = line.rstrip()
        # print line
        # if the line starts with the param we want then we are set, otherwise
        # if it starts with a # then ignore
        if line.startswith(param) != "#":
            if line.startswith(param):
                line = line.rstrip()
                # remove any quotes or single quotes
                line = line.replace('"', "")
                line = line.replace("'", "")
                line = line.split("=", 1)
                return line[1]

# copy an entire folder function
def copyfolder(sourcePath, destPath):
    for root, dirs, files in os.walk(sourcePath):

        # figure out where we're going
        dest = destPath + root.replace(sourcePath, '')

        # if we're in a directory that doesn't exist in the destination folder
        # then create a new folder
        if not os.path.isdir(dest):
            os.mkdir(dest)

        # loop through all files in the directory
        for f in files:

            # compute current (old) & new file locations
            oldLoc = root + '/' + f
            newLoc = dest + '/' + f

            if not os.path.isfile(newLoc):
                try:
                    shutil.copy2(oldLoc, newLoc)
                except IOError:
                    pass

# this routine will be used to check config options within the asena.options
def check_options(option):
        # open the directory
    trigger = 0
    if os.path.isfile(userconfigpath + "set.options"):
        fileopen = open(userconfigpath + "set.options", "r").readlines()
        for line in fileopen:
            match = re.search(option, line)
            if match:
                line = line.rstrip()
                line = line.replace('"', "")
                line = line.split("=")
                return line[1]
                trigger = 1

    if trigger == 0:
        return trigger

# future home to update one localized set configuration file
def update_options(option):
        # if the file isn't there write a blank file
    if not os.path.isfile(userconfigpath + "asena.options"):
        filewrite = open(userconfigpath + "asena.options", "w")
        filewrite.write("")
        filewrite.close()

    # remove old options
    fileopen = open(userconfigpath + "asena.options", "r")
    old_options = ""
    for line in fileopen:
        match = re.search(option, line)
        if match:
            line = ""
        old_options = old_options + line
    # append to file
    filewrite = open(userconfigpath + "asena.options", "w")
    filewrite.write(old_options + "\n" + option + "\n")
    filewrite.close()

# check to see if we are running backbox linux
def check_backbox():
    if os.path.isfile("/etc/issue"):
        backbox = open("/etc/issue", "r")
        backboxdata = backbox.read()
        if "BackBox" in backboxdata:
            return "BackBox"
        # if we aren't running backbox
        else:
            return "Non-BackBox"
    else:
        print("[!] Not running a Debian variant...")
        return "Non-BackBox"

# check to see if we are running kali linux
def check_kali():
    if os.path.isfile("/etc/apt/sources.list"):
        kali = open("/etc/apt/sources.list", "r")
        kalidata = kali.read()
        if "kali" in kalidata:
            return "Kali"
        # if we aren't running kali
        else:
            return "Non-Kali"
    else:
        print("[!] Not running a Debian variant..")
        return "Non-Kali"

# exit routine
def exit_asena():
    sys.exit()

