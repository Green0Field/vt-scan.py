# this py file gets a list of the pkg names of the android phone's installed apps
from subprocess import check_output
if __name__ == '__main__':
    print('You must run this as a module')
def getpkgs():
    print("getting pkg names")
    pkgs = check_output("/system/bin/pm list packages -f -3", shell=True, text=True).splitlines()
    pkgs = [l.split("=")[-1] for l in pkgs if "/system/" not in l]
    return "\n".join(a for a in pkgs if not any(k in a.lower() for k in ["camera", "samsung", "galaxy", "sec", "tmobile", "t-mobile", "google", "android"]))