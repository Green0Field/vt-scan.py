###################
#    virustotal   #
##################
# A py program for
# termux to scan the
# phones apps with
# virustotal.
from getapks import *
from getpkgs import *
from scan import *
import conf
from fhash import *
from argparse import *
import vt
def scanapks():
    apks = listdir("apks")
    with vt.Client(conf.API_KEY) as client:
        for apk in apks:
            with open("apks/" + apk, "rb") as f:
                fhash = getfhash(f, apk)
                scan(f, fhash, apk, client)
if __name__ == '__main__':
    parser = ArgumentParser(description="scan installed apps on Android", prog="vt-scan.py")
    parser.add_argument("-s", "--scan", help="only scan apks in apks folder and exit", action="store_true")
    parser.add_argument("-a", "--apks", help="only extract apks and exit", action="store_true")
    args = parser.parse_args()
    if args.scan:
        scanapks()
    elif args.apks:
        getapks(getpkgs())
    else:
        getapks(getpkgs())
        scanapks()
    """for apk in apks:
        if apk.endswith('.apk'):
            print("starting scan for " + apk)
            with open("apks/" + apk, 'rb') as f:
                try:
                    analysis = client.scan_file(f, wait_for_completion=True)
                except vt.error.APIError:
                    print(apk + ' was already scaned, retrieving results from last scan')
                    fhash = getfhash(f, apk)
                    result = client.get_object("/files/" + fhash)
                else:
                    print('successfull scan for ' + apk)
                    print("ret")
                    fhash = getfhash(f, apk)
                    result = client.get_object("/files" + fhash)""" 
else:
    print('You must run this as a script')
