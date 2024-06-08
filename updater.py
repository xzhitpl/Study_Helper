import requests
import os

if __name__ == "__main__":
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"}
    response = requests.get(
        "https://github.com/xzhiter/Mistakes_Recorder/releases/download/V3.1/Mistakes_Recorder-3.1-py312-win_amd64.7z",
        headers=headers, verify=False)
    with open("./new.7z", "wb") as f:
        f.write(response.content)
    zipper = requests.get("https://www.7-zip.org/a/7zr.exe", headers=headers)
    with open("./7zr.exe", "wb") as f:
        f.write(zipper.content)
    os.system("7zr x new.7z")
    os.remove("./new.7z")
    os.remove("./7zr.exe")
