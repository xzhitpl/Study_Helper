import datetime
import os
import platform

if __name__ == "__main__":
    with open("./about.py", "r", encoding="utf-8") as f:
        about = f.read()
    about_new = about.replace("X.X.X", platform.python_version())
    date = datetime.date.today()
    about_new = about_new.replace("X年X月X日", f"{date.year}年{date.month}月{date.day}日")
    with open("./about.py", "w", encoding="utf-8") as f:
        f.write(about_new)
    os.system("pyinstaller -w main.py --hidden-import "
              "\"numpy.libs\" --hidden-import \"email.mime\" --hidden-import  \"email.mime.text\" --hidden-import "
              "\"Cryptodome.Cipher.AES\" --hidden-import \"smtplib\" -i \"./icon.ico\"")
    with open("./about.py", "w", encoding="utf-8") as f:
        f.write(about)
    os.system("pyinstaller -F -w updater.py")
    input()
