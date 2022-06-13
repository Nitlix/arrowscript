from posixpath import expanduser
import requests
import os


print("Installing the newest Arrowscript Version...")

print("Creating folder...")
try:
    os.mkdir(f"{os.path.expanduser('~/Desktop')}/Arrowscript/")
    os.mkdir(f"{os.path.expanduser('~/Desktop')}/Arrowscript/temp")
except Exception:
    pass
dir = f"{os.path.expanduser('~/Desktop')}/Ammoscript/"
print("Downloading...")
url = 'https://raw.githubusercontent.com/Nitlix/arrowscript/main/builder.py'
try:
    r = requests.get(url, allow_redirects=True)
except Exception:
    print("No interenet access. Please try later.")
    input()
else:

    print("Extracting and Installing...")
    open(f"{dir}ArrowScript.py", 'wb').write(r.content)







    print("Installation completed, press anything to continue.")
    input()

