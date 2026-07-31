# this py file scans the apks in the apk folder
from vt import error
from os import listdir
if __name__ == '__main__':
    print('You must run this as a module')
def scan(f, fhash, apk, client):
    try:
        print("starting scan for " + apk)
        analysis = client.scan_file(f, wait_for_completion=True)
    except error.APIError:
        print(apk + " was already scaned, retrieving results from last scan")
        try:
            analysis = client.get_object("/files/" + fhash)
        except vt.error.APIError:
            print(apk + " was unable to be scaned. Skipping.")
            success = False
        else:
            result = analysis. last_analysis_stats
            print("got results for " + apk)
            success = True
    else:
        print("successfull scan for " + apk)
        print("retrieving results")
        result = analysis.stats
        result = {
            "malicious": result.get('malicious'),
            "suspicious": result.get('suspicious')}
        success = True
    if success and result["malicious"] < 3 and result["suspicious"] < 3:
        print(apk + ' seems ok, skipping')
    elif success and result["malicious"] <= 7 and result["suspicious"] <= 9:
        print('WARNING: ' + apk + ' could contain viruses. BE CARFULL')
        # handle the virus
    elif success and result["malicious"] <= 12 and result["suspicious"] <= 14:
        print('CAUTION: ' + apk + 'SEEMS TO HAVE BEEN VERY INFECTED!')
        # handle the virus