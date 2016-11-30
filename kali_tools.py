# Kali Linux tools
import os,sys,datetime,pwd
source_list="""
deb http://http.kali.org/kali kali main non-free contrib
deb http://security.kali.org/kali-security kali/updates main contrib non-free
deb-src http://http.kali.org/kali kali main non-free contrib
deb-src http://security.kali.org/kali-security kali/updates main contrib non-free"""
def program_download(program_name):# proqram yuklemek ucun <<HAZIR DEYIL>>
	pass
#----------------------------------------------------
def add_source_list(source_list):# source-list dosyaya elave etmek <<HAZIR DEYIL>>
	dosyakali=open("/etc/apt/sources.list","a")
	dosyakali.write(source_list)
#----------------------------------------------------
def updatekali():
	print("\x1b[0;30;36m")
	os.system("apt-get update")
	print("\x1b[0m")
#--------------------------------------------------------

def dosya_oxumaqkali():
	dosya=open("/etc/apt/sources.list","r")
	dosya=dosya.read()
	reqem=dosya.find(source_list)
	if reqem==-1:
		dosya=open("/etc/apt/sources.list","a")
		dosya.write(source_list)
		print("\n>>> Ekleme basarili bir sekilde tamamlandi\n")
	else:
		print("\n>>> Tebrikler  Kali source dosyalari kaynakda mevcut\n>>> Bir sonraki isleme gecin\n")
#------------------------------------------------------------
def islemkali():
	mevcut=1
	mevcut2=1
	os.system("clear")
	a=1
	print(robort)
	gorsellik=""
	while True:
		giriwkali=input("""{}
\x1b[0;30;33m1) Add Kali Linux source.list
2) Update 
3) Kali Linux Tools
4) Help
\x1b[0;30;31m99) EXIT\x1b[0m \x1b[0;30;33m
:""".format(gorsellik))
		giriwkali=giriwkali.strip()
		if not giriwkali:
			print("\n>>> Bir islem secin\n")
		elif giriwkali=="1":
			mevcut=2
			dosya_oxumaqkali()
		elif giriwkali=="2":
			if mevcut==2:
				mevcut2=2
				updatekali()
			else:
				print("\n>>> Ilk once 1-ci islemi yapmaniz tavsiye edilir ==> \"1) Add Kali Linux source.list\"\n")
		elif giriwkali=="4":
			helpkali()
		elif giriwkali=="99":
			print("\n>>> Tessekkur edirik\n")
			exit()
		elif giriwkali=="3":
			if mevcut==1:
				print("\n>>> Ilk once 1-ci islemi yapmaniz tavsiye edilir ==> \"1) Add Kali Linux source.list\"\n")
			elif mevcut==2 and mevcut2==1:
				print("\n>>> Guncelleme yapilmadi ==>\"2) Update\"\n")
			elif mevcut==2 and mevcut2==2:
				butun()
				gorsellik="==========================================="
		else:
			print("\n>>> Listeye uyqun islem secin\n")
#-----------------------------------------------------
def helpkali():
	helpkali="""
=============================================
   Proqram Kali araclarini kurmak icindir
Kullanilmasi cok kolaydir hangi islemi
istiyorsaniz karwisindaki rakami secerek
"ENTER" tusuna basmaniz yeterlidir 
----------------------------------------
Ekrandaki listede mevcut olmayan herhangi
bir islemi secmeniz durumunda hata verecekdr

\x1b[0;30;31mUYARI:\x1b[0m \x1b[0;30;33mIslem secerken rakamlarin karwisinda
hicbir sembol,harif kullanmayin aksi halde hata
verecekdir

BASARILAR!!!!
==============================================
"""
	print(helpkali)
#-------------------------------------------------------------------------

def emeliyyat(arac):
	print(arac)
	arac2=arac
	arac=arac.split()
	while True:
		aracgiriw=input(">>> :")
		aracgiriw=aracgiriw.strip()
		uzunluq=len(arac)-2
		uzunluq=uzunluq/2
		uzunluq=int(uzunluq)
		try:
			uzunluq=len(arac)-2
			uzunluq=uzunluq/2
			uzunluq=int(uzunluq)
			if aracgiriw=="99":
				break
			elif not aracgiriw:
				print("\n\n>>> Bir islem secin\n")
			elif int(aracgiriw)>uzunluq or int(aracgiriw)<=0:
				print("\n>>> Listeye uyqun islem secin\n")
			else:
				aracgiriw=aracgiriw+")"
				aracgiriw=aracgiriw.strip()
				aracgiriw=arac.index(aracgiriw)+1
				aracgiriw=arac[aracgiriw]
				aracgiriw=aracgiriw.strip()
				aracgiriw=aracgiriw.lower()
				print(aracgiriw)
				os.system("apt-get install {}".format(aracgiriw))			
		except (TypeError,ValueError):
			print("\n>>> Listeye uyqun islem secin\n")
#-------------------------------------------------------

def information_gathering():
	os.system("clear")
	arac1="""\x1b[0;30;35m==================Information Gathering==================\x1b[0m\n
\x1b[0;30;36m
1) acccheck                      31) iSMTP                     
2) ace-voip                      32) lbd                     
3) Amap                          33) Maltego Teeth                   
4) Automater                     34) masscan                     
5) bing-ip2hosts                 35) Metagoofil                     
6) braa                          36) Miranda                     
7) CaseFile                      37) Nmap                     
8) CDPSnarf                      38) ntop                     
9) cisco-torch                   39) p0f                     
10) Cookie-Cadger                40) Parsero                     
11) copy-router-config           41) Recon-ng                     
12) DMitry                       42) SET                     
13) dnmap                        43) smtp-user-enum                     
14) dnsenum                      44) snmp-check                     
15) dnsmap                       45) sslcaudit                     
16) DNSRecon                     46) SSLsplit                     
17) dnstracer                    47) sslstrip                     
18) dnswalk                      48) SSLyze                     
19) DotDotPwn                    49) THC-IPV6                     
20) enum4linux                   50) theHarvester                     
21) enumIAX                      51) TLSSLed                     
22) Fierce                       52) twofi                     
23) Firewalk                     53) URLCrazy                     
24) fragroute                    54) Wireshark                     
25) fragrouter                   55) WOL-E                     
26) Ghost Phisher                56) Xplico                     
27) GoLismero                    57) snmp
28) goofile                                           
29) hping3                                            
30) InTrace\x1b[0m

\x1b[0;30;31m99) EXIT\x1b[0m
"""
	emeliyyat(arac1)
#---------------------------------------------------------------
def vulnerablitiy_analysis():
	os.system("clear")
	arac2="""\x1b[0;30;35m==================Vurnerablitiy Analysis==================\x1b[0m\n
\x1b[0;30;36m
1) BBQSQL                        18) ohrwurm                     
2) BED                           19) openvas-administrator                     
3) cisco-auditing-tool           20) openvas-cli                     
4) cisco-global-exploiter        21) openvas-manager                     
5) cisco-ocs                     22) openvas-scanner                     
6) cisco-torch                   23) Oscanner                     
7) copy-router-config            24) Powerfuzzer                     
8) DBPwAudit                     25) sfuzz                     
9) Doona                         26) SidGuesser                     
10) DotDotPwn                    27) SIPArmyKnife                     
11) Greenbone-Security-Assistant 28) sqlmap                     
12) GSD                          29) Sqlninja                     
13) HexorBase                    30) sqlsus                     
14) Inguma                       31) THC-IPV6                     
15) jSQL                         32) tnscmd10g                     
16) Lynis                        33) unix-privesc-check                     
17) Nmap                         34) Yersinia
\x1b[0;30;31m99) EXIT\x1b[0m \x1b[0;30;33m   35) openvas          
"""
	emeliyyat(arac2)
#---------------------------------------------------
def wireless_attacks():
	os.system("clear")
	arac3="""\x1b[0;30;35m==================Wireless Attacks==================\x1b[0m\n
\x1b[0;30;36m
1) Aircrack-ng                   17) kalibrate-rtl                     
2) Asleap                        18) KillerBee                     
3) Bluelog                       19) Kismet                     
4) BlueMaho                      20) mdk3                     
5) Bluepot                       21) mfcuk                     
6) BlueRanger                    22) mfoc                     
7) Bluesnarfer                   23) mfterm                     
8) Bully                         24) Multimon-NG                     
9) coWPAtty                      25) PixieWPS                     
10) crackle                      26) Reaver                     
11) eapmd5pass                   27) redfang                     
12) Fern-Wifi-Cracker            28) RTLSDR-Scanner                     
13) Ghost-Phisher                29) Spooftooph                     
14) GISKismet                    30) Wifi-Honey                     
15) Gqrx                         31) Wifitap                     
16) gr-scan                      32) Wifite
\x1b[0;30;31m99) EXIT\x1b[0m \x1b[0;30;33m"""
	emeliyyat(arac3)
#-------------------------------------------------------
def exploitation_tools():
	os.system("clear")
	arac4="""\x1b[0;30;35m==================Exploitation Tools==================\x1b[0m\n
\x1b[0;30;36m
1) Armitage                      10) exploitdb                     
2) Backdoor-Factory             11) jboss autopwn                     
3) BeEF                          12) Linux-Exploit-Suggester                     
4) cisco-auditing-tool           13) Maltego Teeth                    
5) cisco-global-exploiter        14) SET                     
6) cisco-ocs                     15) ShellNoob                     
7) cisco-torch                   16) sqlmap                     
8) Commix                        17) THC-IPV6                     
9) crackle                       18) Yersinia
\x1b[0;30;31m99) EXIT\x1b[0m \x1b[0;30;33m"""
	emeliyyat(arac4)
#-------------------------------------------------------
def forensics_tools():
	os.system("clear")
	arac5="""\x1b[0;30;35m==================Forensics Tools==================\x1b[0m\n
\x1b[0;30;36m
1) Binwalk                       12) Foremost                     
2) bulk-extractor                13) Galleta                     
3) Capstone                      14) Guymager                     
4) chntpw                        15) iPhone-Backup-Analyzer                     
5) Cuckoo                        16) p0f                     
6) dc3dd                         17) pdf-parser                     
7) ddrescue                      18) pdfid                     
8) DFF                           19) pdgmail                     
9) diStorm3                      20) peepdf                     
10) Dumpzilla                    21) RegRipper                     
11) extundelete                  22) Volatility
                                 23) Xplico

\x1b[0;30;31m99) EXIT\x1b[0m \x1b[0;30;33m"""
	emeliyyat(arac5)
#----------------------------------------------------
def web_applications():
	os.system("clear")
	arac6="""\x1b[0;30;35m==================Web Applications==================\x1b[0m\n
\x1b[0;30;36m
1) apache-users                  21) plecost                     
2) Arachni                       22) Powerfuzzer                     
3) BBQSQL                        23) ProxyStrike                     
4) BlindElephant                 24) Recon-ng                     
5) Burp Suite                    25) Skipfish                     
6) CutyCapt                      26) sqlmap                     
7) DAVTest                       27) Sqlninja                     
8) deblaze                       28) sqlsus                     
9) DIRB                          29) ua-tester                     
10) DirBuster                    30) Uniscan                     
11) fimap                        31) Vega                     
12) FunkLoad                     32) w3af                     
13) Grabber                      33) WebScarab                     
14) jboss-autopwn                34) Webshag                     
15) joomscan                     35) WebSlayer                     
16) jSQL                         36) WebSploit                     
17) Maltego Teeth                37) Wfuzz                     
18) PadBuster                    38) WPScan                     
19) Paros                        39) XSSer                     
20) Parsero                      40) zaproxy 
\x1b[0;30;31m99) EXIT\x1b[0m \x1b[0;33;36m"""
	emeliyyat(arac6)
#------------------------------------------------
def stress_testing():
	os.system("clear")
	arac7="""\x1b[0;30;35m==================Stress Testing==================\x1b[0m\n
\x1b[0;30;36m
1) DHCPig                        8) Reaver                     
2) FunkLoad                      9) rtpflood                     
3) iaxflood                     10) SlowHTTPTest                     
4) Inundator                    11) t50                     
5) inviteflood                  12) Termineter                     
6) ipv6-toolkit                 13) THC-IPV6                     
7) mdk3                         14) THC-SSL-DOS  
\x1b[0;30;31m99) EXIT\x1b[0m \x1b[0;30;33m"""
	emeliyyat(arac7)
#-------------------------------------------------
def sniffing_spoofing():
	os.system("clear")
	arac8="""\x1b[0;30;35m==================Sniffing Spoofing==================\x1b[0m\n
\x1b[0;30;36m
1) Burp suite
2) DNSChef                      18) sctpscan                     
3) fiked                        19) SIPArmyKnife                     
4) hamster-sidejack             20) SIPp                     
5) HexInject                    21) SIPVicious                     
6) iaxflood                     22) SniffJoke                     
7) inviteflood                  23) SSLsplit                     
8) iSMTP                        24) sslstrip                     
9) isr-evilgrade                25) THC-IPV6                     
10) mitmproxy                   26) VoIPHopper                     
11) ohrwurm                     27) WebScarab                     
12) protos-sip                  28) Wifi-Honey                     
13) rebind                      29) Wireshark                     
14) responder                   30) xspy                     
15) rtpbreak                    31) Yersinia                     
16) rtpinsertsound              32) zaproxy
\x1b[0;30;31m99) EXIT\x1b[0m \x1b[0;30;33m"""
	emeliyyat(arac8)
#---------------------------------------------------
def password_attacks():
	os.system("clear")
	arac9="""\x1b[0;30;35m==================Password Attacks==================\x1b[0m\n
\x1b[0;30;36m
1) acccheck                     19) Maskprocessor                     
2) Burp Suite                   20) multiforcer                     
3) CeWL                         21) Ncrack                     
4) chntpw                       22) oclgausscrack                     
5) cisco-auditing-tool          23) PACK                     
6) CmosPwd                      24) patator                     
7) creddump                     25) phrasendrescher                     
8) crunch                       26) polenum                     
9) DBPwAudit                    27) RainbowCrack                     
10) findmyhash                  28) rcracki-mt                     
11) gpp-decrypt                 29) RSMangler                     
12) hashid identifier           30) SQLdict                     
13) HexorBase                   31) Statsprocessor                     
14) Hydra                       32) THC-pptp-bruter                     
15) John the Ripper             33) TrueCrack                     
16) Johnny                      34) WebScarab                     
17) keimpx                      35) wordlists                     
18) Maltego Teeth               36) zaproxy
\x1b[0;30;31m99) EXIT\x1b[0m \x1b[0;30;33m"""
	emeliyyat(arac9)
#------------------------------------------------
def maintaining_access():
	os.system("clear")
	arac10="""\x1b[0;30;35m==================Maintaining Access==================\x1b[0m\n
\x1b[0;30;36m
1) CryptCat                      9) polenum                     
2) Cymothoa                     10) PowerSploit                     
3) dbd                          11) pwnat                     
4) dns2tcp                      12) RidEnum                     
5) httptunnel                   13) sbd                     
6) HTTPTunnel                   14) U3-Pwn                     
7) Intersect                    15) Webshells                     
8) Nishang                      16) Weevely  
                                17) Winexe
                                \x1b[0;30;31m99) EXIT\x1b[0m \x1b[0;30;33m
"""
	emeliyyat(arac10)
#---------------------------------------------------------
def hardware_hacking():
	os.system("clear")
	arac11="""\x1b[0;30;35m==================Hardware Hacking==================\x1b[0m
\x1b[0;30;36m
1) android-sdk
2) apktool
3) Arduino
4) dex2jar
5) Sakis3G
6) smali
\x1b[0;30;31m99) EXIT\x1b[0m \x1b[0;30;33m
"""
	emeliyyat(arac11)
#-----------------------------------------------------
def reverse_engineering():
	os.system("clear")
	arac12="""\x1b[0;30;35m==================Rerverse Engineering==================\x1b[0m\n
\x1b[0;30;36m
1) apktool
2) dex2jar
3) diStorm3
4) edb debugger
5) jad
6) javasnoop
7) JD-GUI
8) OllyDbg
9) smali
10) Valgrind
\x1b[0;30;31m99) EXIT\x1b[0m \x1b[0;30;33m
"""
	emeliyyat(arac12)
#---------------------------------------------------------
def reporting_tools():
	os.system("clear")
	arac13="""\x1b[0;30;35m==================Reporting Tools=================\x1b[0m\n
\x1b[0;30;36m
1) CaseFile
2) CutyCapt
3) dos2unix
4) Dradis
5) KeepNote
6) MagicTree
7) etagoofil
8) Nipper-ng
9) pipal
\x1b[0;30;31m99) EXIT\x1b[0m \x1b[0;30;33m
"""
	emeliyyat(arac13)
#-----------------------------------------------------------
def butun():
	goster=""
	goster2=""
	os.system("clear")
	while True:
		arachamsi="""
\x1b[0;30;35m==================KALI LINUX TOOLS==================\x1b[0m\n
\x1b[0;30;33m1) Reporting_tools
2) Reverse_engineering
3) Hardware_hacking
4) Maintaining_access
5) Password_attacks
6) Sniffing_spoofing
7) Stress_testing
8) Web_applications
9) Forensics_tools
10) Exploitation_tools
11) Wireless_attacks
12) Vulnerablitiy_analysis
13) Information_gathering
\x1b[0;30;31m99) EXIT\x1b[0m \x1b[0;30;36m

>>> {}{}:""".format(goster,goster2)
		os.system("clear")
		giriwhamsi=input(arachamsi)
		if not giriwhamsi:
			goster2="Bir islem secin\n"
			goster=""
		elif giriwhamsi=="1":
			goster2=""
			goster=""
			os.system("clear")	
			reporting_tools()
		elif giriwhamsi=="2":
			goster2=""
			goster=""
			os.system("clear")
			reverse_engineering()
		elif giriwhamsi=="3":
			goster2=""
			goster=""
			os.system("clear")
			hardware_hacking()
		elif giriwhamsi=="4":
			goster2=""
			goster=""
			os.system("clear")
			maintaining_access()
		elif giriwhamsi=="5":
			goster2=""
			goster=""
			os.system("clear")
			password_attacks()
		elif giriwhamsi=="6":
			goster2=""
			goster=""
			os.system("clear")
			sniffing_spoofing()
		elif giriwhamsi=="7":
			goster2=""
			goster=""
			os.system("clear")
			stress_testing()
		elif giriwhamsi=="8":
			goster2=""
			goster=""
			os.system("clear")
			web_applications()
		elif giriwhamsi=="9":
			goster2=""
			goster=""
			os.system("clear")
			forensics_tools()
		elif giriwhamsi=="10":
			goster2=""
			goster=""
			os.system("clear")
			exploitation_tools()
		elif giriwhamsi=="11":
			goster2=""
			goster=""
			os.system("clear")
			wireless_attacks()
		elif giriwhamsi=="12":
			goster2=""
			goster=""
			os.system("clear")
			vulnerablitiy_analysis()
		elif giriwhamsi=="13":
			goster2=""
			goster=""
			os.system("clear")
			information_gathering()
		elif giriwhamsi=="99":
			os.system("clear")
			break
		else:
			goster="Listeye uyqun islem secin\n"
			continue
#---------------------------------------------------------------
arac=r"""
$$\   $$\           $$\ $$\    $$\        $$\                      ___    ____
$$ | $$  |          $$ |\__|   $$ |       \__|          __    __   $$ \   $$ /
$$ |$$  /  $$$$$$\  $$ |$$\    $$ |       $$\ $$$$$$$\  $$\   $$\   $$ \ $$ /
$$$$$  /   \____$$\ $$ |$$ |   $$ |       $$ |$$  __$$\ $$ |  $$ |   $$ $$ / 
$$  $$<     $$$$$$ |$$ |$$ |   $$ |       $$ |$$ |  $$ |$$ |__$$ |    $$$ |
$$ |\$$\   $$  _$$ |$$ |$$ |   $$ |       $$ |$$ |  $$ |$$    $$ |   $$ $$ \
$$ | \$$\  \$$$$$$ |$$ |$$ |   $$$$$$$$$\ $$ |$$ |  $$ |$$$$$$$$ |  $$ / $$ \
\__|  \___\ \______|\__|\__|   \_________\\__|\__|  \__|\________| $$_/   $$_\
"""
robort="""\x1b[0;30;36m[]================================[]
	Yapimci >>> Efrahim.B
[]================================[]\x1b[0m
 \x1b[0;30;32m               

               \x1b[0;30;36m{}\x1b[0m  \x1b[0;30;32m

=============================================================""".format(arac)
#-----------------------------------------------------------------
def kali_linux_tools():
	pass
pyt_versionkali=sys.version_info.major
system_versionkali=os.name
if system_versionkali=="posix":
	mb_or_rootkali=pwd.getpwuid( os.getuid() ).pw_name
	if pyt_versionkali<3 and mb_or_rootkali=="root":
		print("\n>>> Proqram yalniz Python3 ile calisiyor\n")
	elif pyt_versionkali>=3 and mb_or_rootkali!="root":
		print(">>>\x1b[0;30;41m'root'\x1b[0m izni yok")
	elif pyt_versionkali>=3 and mb_or_rootkali=="root":
		islemkali()
else: # Eger basqa bir isletim sisteminde islese veya python3 deyl basqa surumu ile caliwdirilsa <<HAZIR>>
	print("\n>>>Proqram yalnizca Linux isletim sistemlerinde calisir\n")


