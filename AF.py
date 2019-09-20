import requests,time,sys,os,argparse
from colorama import init
init()
from colorama import Fore



parser = argparse.ArgumentParser(description='Simple Admin Finder v0.00...00 ,\n File list.txt should be the same path.')
parser.add_argument('-u','--url',required='True', help='Target URL for example : AF.py -u  www.example.com' )
args = parser.parse_args()
url = args.url

start_time = time.time()
found = []
def scanner(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            print (Fore.GREEN+'[+] Found ->  '+url)
            global found
            found.append(url)
        else:
            print (Fore.RED+'[-] Not found ->  '+url)

    except:
        print(Fore.RED+'[-] Not response from the server %s ->'%url)
def banner():
    print('\033[91m' + """
    ╔════════════════════════════════════════════╗
    ║                                            ║
    ║                                            ║
    ║        Admin Finder v0.00......000         ║
    ║                                            ║
    ║                                            ║
    ║ Developed By Mavali.a.net@gmail.com        ║
    ╚════════════════════════════════════════════╝
    """ + '\033[0m')

     
  
def main(url):
                    banner()
                    url = url.replace('http://','')
                    url = url.replace('https://','')
                    if (not url.endswith('/')):
                        url +='/'
                    if not os.path.exists('list.txt'):
                        print ('List file is not exist')
                    with open('list.txt','r') as f:
                        for line in f.read().splitlines():
                            line2 = line.strip()
                            if line2 == '':
                                continue
                            line2 = line2.replace('//','/')
                            Pefect_URL =('http://'+url+line2)
                            scanner(Pefect_URL)
                        Total_time = time.time() - float(start_time)
                        Total_time = int(Total_time) // 60  
                        print(Fore.WHITE+'\nFinished in '+ str(Total_time)+ ' min.\n')
                        total_found = len(found)
                        print ('Total found %i pages.' %total_found)
                        for item in found:
                            print(Fore.GREEN +' %s'%item)

main(url)
    

