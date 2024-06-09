import ctypes
import requests
import os
import sys
import time
import subprocess
import shutil


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()
    if sys.argv[1] == "delete":
        time.sleep(0.2)
        os.remove("./学习助手.exe")
        os.remove("./options.safe")
        os.remove("./msyh.ttc")
        os.remove("./icon.png")
        shutil.rmtree("./_internal")
        with open("./delete.cmd", "w") as f:
            f.write(f"@echo off\nping -n 2 127.0.0.1>nul\ndel \"{os.getcwd()}\\updater.exe\"\ndel %0")
        subprocess.Popen("delete.cmd", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, creationflags=0x08000000)
        sys.exit()
    elif sys.argv[1] == "update":
        ctypes.windll.user32.MessageBoxW(0, )
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                 "Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"}
        ver = sys.argv[1]
        url = f"https://github.com/xzhitpl/Study_Helper/releases/download/V{ver}/Study_Helper-{ver}-win_amd64.7z"
        response = requests.get(url, headers=headers, verify=False)
        with open("./new.7z", "wb") as f:
            f.write(response.content)
        zipper = requests.get("https://www.7-zip.org/a/7zr.exe", headers=headers)
        with open("./7zr.exe", "wb") as f:
            f.write(zipper.content)
        os.system("7zr x new.7z")
        os.remove("./new.7z")
        os.remove("./7zr.exe")
        os.remove("./学习助手.exe")
        shutil.rmtree("./_internal")
        shutil.copyfile("./学习助手/学习助手.exe", "./学习助手.exe")
        shutil.copytree("./学习助手/_internal", "./_internal")
