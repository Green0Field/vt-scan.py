# this py module gets the hash of a file
from hashlib import file_digest
if __name__ == "__main__":
    print("You must run this as a module")
def getfhash(f, name):
    if name: 
        print('getting the hash of ' + name)
    else:
        print('getting the hash of the requested file')
    fdigest = file_digest(f, "sha256")
    return fdigest.hexdigest()
