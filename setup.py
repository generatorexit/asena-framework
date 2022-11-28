#!/usr/bin/python

# quick installer for Asena
import os
import subprocess
print("[*] Installing requirements.txt")
subprocess.Popen("pip3 install -r requirements.txt", shell=True).wait()
print("[*] Installing Asena Framework to /usr/share/asena-framework")
print(os.getcwd())
subprocess.Popen("mkdir /usr/share/asena-framework/;mkdir /etc/asena-framework/;cp -rf * /usr/share/asena-framework/;cp src/core/config.baseline /etc/asena-framework/asena.config", shell=True).wait()
print("[*] Creating launcher for Asena Framework")
filewrite = open("/usr/local/bin/asena", "w")
filewrite.write("#!/bin/sh\ncd /usr/share/asena-framework\n./asena")
filewrite.close()
print("[*] Done. Chmoding +x")
subprocess.Popen("chmod +x /usr/local/bin/asena", shell=True).wait()
print("[*] Finished. Run 'asena' to start the Asena Framework.")
