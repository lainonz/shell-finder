import requests
from multiprocessing.dummy import Pool

class Domain:
    def __init__(self, domain):
        self.domain = domain
    
    def checkShell(self):
        shellFiles = open('shell.txt', 'r')
        for path in shellFiles:
            path = path.replace('\n', '')
            r = requests.get(self.domain+path)
            if "drwxr" in r.text:
                print("[{}{}] > Found Shell!".format(self.domain, path))
                saveres = open("result/shellz.txt")
                saveres.write(self.domain+'\n')
            else:
                print("[{}{}] > Shell not Found!".format(self.domain, path))

def asuna(list):
    website = Domain(list)
    website.checkShell()

def main():
    try:
        urList = open(input("root@weblist~# "), "r").read().split("\n")
        thread = int(input("root@threads~# "))
        pool = Pool(thread)
        pool.map(asuna, urList)
        pool.close()
        pool.join
    except:
        pass

if __name__ == '__main__':
    main()
