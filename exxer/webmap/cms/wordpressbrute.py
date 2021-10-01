import os

class myapp:
    website = input("please add the target =>")
    print("target =>" + " " + website)
    username = input("add username =>")
    print("username =>" + " " + username)
    wordlists = input("wordlists =>")
    print("wordlists =>" + " " + wordlists)
    os.system("wpscan -u" + " " + website +  + " " + "-wordlist " + " " + wordlists + " " + "--username" +"  " + username)

if __name__ == "__main__":
    myapp()