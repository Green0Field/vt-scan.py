# this py module puts all apks into apks folder
from subprocess import *
from shutil import *
from os import makedirs
if __name__ == '__main__':
    print('You must run this as a module')
def getapks(pkglist):
    makedirs("apks", exist_ok = True)
    print("coping apk files")
    for pkg in [p.strip() for p in str(pkglist).splitlines() if p.strip()]:
        path = check_output(f"/system/bin/pm path {pkg}", shell=True, text=True)
        copy(path.splitlines()[0].replace("package:", ""), f"apks/{pkg}.apk")
        print('done with ' + pkg)
