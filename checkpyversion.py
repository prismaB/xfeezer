class check:
    def checknetwork():
        import requests
        r = requests.get('https://github.com')
        if r.status_code == 404 or r.status_code == 200:
            print("network connection found lets start checkpyversion")
        else:
            print("network connection not found")
            import sys
            sys.exit()
    checknetwork()
    def checkpyversion():
        import sys
        import os
        if sys.version_info < (3,9):
            sys.stdout.write("xfeezer requires the python 3.9")
            sys.exit(1)
        os.system("python3 checkfiles.py")
    checkpyversion()
if __name__ == '__main__':
    pass