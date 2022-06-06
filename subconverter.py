import os
import json
from base64 import b64decode

banner = '''
   _____ __  ______  __________  _   ___    ____________  ________________ 
  / ___// / / / __ )/ ____/ __ \/ | / / |  / / ____/ __ \/_  __/ ____/ __ \\
  \__ \/ / / / __  / /   / / / /  |/ /| | / / __/ / /_/ / / / / __/ / /_/ /
 ___/ / /_/ / /_/ / /___/ /_/ / /|  / | |/ / /___/ _, _/ / / / /___/ _, _/ 
/____/\____/_____/\____/\____/_/ |_/  |___/_____/_/ |_| /_/ /_____/_/ |_|
v.1.0.0                                                       
'''

awal ='''[General]
dns-server = system, 8.8.8.8, 8.8.4.4
skip-proxy = 127.0.0.1, 192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12, 100.64.0.0/10, localhost, *.local
proxy-test-url = http://www.gstatic.com/generate_204
internet-test-url = http://www.gstatic.cn/generate_204
http-listen = 0.0.0.0:1234
socks5-listen = 127.0.0.1:1235
udp-policy-not-supported-behaviour = DIRECT

[Proxy]'''

def real_path(file_name):
	return os.path.dirname(os.path.abspath(__file__)) + file_name

def akunvmess():
    op_file_conf = open(real_path('/SURFBOARD.conf'), 'w', encoding='utf-8')
    print('\33[94m' + banner + '\33[0m')
    print("Script Auto Genarate Config Surfboard")
    print('''\33[90mcatatan: 
+ Masukkan akun vmess di bawah
+ Jika akun vmess lebih dari 1 maka
  pisahkan dengan tanda (;) tanpa spasi
+ Config tersimpan dalam file SURFBOARD.conf
+ atau dapat copas langsung dari layar termux
  mulai dari [General] sampe FINAL\33[0m\n''')
    file = input('\n\33[92mCopy akun vmess disini \33[0m=>> ')
    datacopas = file.split(';')
    print("\n\n\33[92m--------------[PROSESS GENERATE CONFIG]--------------\33[0m\n")
    op_file_conf.write(awal)
    print(f"{awal}", end="")
    data_nama = []
    for database in datacopas:
        dataakun = database.replace("vmess://", "")
        decode = b64decode(dataakun)
        data = json.loads(decode)
        nama_ = f"{data['ps']}"
        data_nama.append(nama_)
        if data["add"] == "cf-vod.nimo.tv":
            akun = (f"\n{data['ps']} = vmess, cf-vod.nimo.tv, 80,  username={data['id']}, tls=false, ws=true, ws-path={data['path']}, sni={data['host']}, ws-headers=Host:{data['host']}, skip-cert-verify=1, tfo=true, udp-relay=true\n")
        if data["add"] != "cf-vod.nimo.tv":
            akun = (f"\n{data['ps']} = vmess, cf-vod.nimo.tv, 80,  username={data['id']}, tls=false, ws=true, ws-path={data['path']}, sni={data['add']}, ws-headers=Host:{data['add']}, skip-cert-verify=1, tfo=true, udp-relay=true\n")
        op_file_conf.write(akun)
        print(akun, end="")

    select = '\n[Proxy Group]\n✅Select = select,🔁LoadBalance,🚀BestPing'
    op_file_conf.write(select)
    print(f"{select}", end="")
    for nama_akun in data_nama:
        op_file_conf.write(f",{nama_akun}")
        print(f",{nama_akun}", end="")

    loadbalance = '''\n\n🔁LoadBalance = load-balance'''
    op_file_conf.write(loadbalance)
    print(f"{loadbalance}", end="")
    for nama_akun in data_nama:
        op_file_conf.write(f",{nama_akun}")
        print(f",{nama_akun}", end="")

    bestping = '''\n\n🚀BestPing = url-test,url=http://www.gstatic.com/generate_204, interval=600, tolerance=100, timeout=5, hidden=false'''
    op_file_conf.write(bestping)
    print(f"{bestping}", end="")
    for nama_akun in data_nama:
        op_file_conf.write(f",{nama_akun}")
        print(f",{nama_akun}", end="")

    rules_files = '''\n\n[Rule]
#BlackDesertMobile
DOMAIN-SUFFIX,saz-m-w01-gm001.pearl-bdm.com,DIRECT
DOMAIN-SUFFIX,saz-m-w01-gm002.pearl-bdm.com,DIRECT
DOMAIN-SUFFIX,saz-m-w01-gm003.pearl-bdm.com,DIRECT
DOMAIN-SUFFIX,saz-m-w01-gm004.pearl-bdm.com,DIRECT
DOMAIN-SUFFIX,saz-m-w01-gm005.pearl-bdm.com,DIRECT
DOMAIN-SUFFIX,saz-m-w02-gm001.pearl-bdm.com,DIRECT
DOMAIN-SUFFIX,saz-m-w02-gm002.pearl-bdm.com,DIRECT
DOMAIN-SUFFIX,saz-m-w02-gm003.pearl-bdm.com,DIRECT
DOMAIN-SUFFIX,saz-m-w02-gm004.pearl-bdm.com,DIRECT
DOMAIN-SUFFIX,saz-m-w01-cht01.pearl-bdm.com,DIRECT

#MobileLegends
DOMAIN-SUFFIX,www.mobilelegends.com,DIRECT
DOMAIN-SUFFIX,m.mobilelegends.com,DIRECT
DOMAIN-SUFFIX,akmcdn.ml.youngjoygame.com,DIRECT
DOMAIN-SUFFIX,akmstatic.ml.youngjoygame.com,DIRECT
DOMAIN-SUFFIX,cdnconfig.aihelp.net,DIRECT
DOMAIN-SUFFIX,akmpicture.youngjoygame.com,DIRECT
DOMAIN-SUFFIX,ip.ml.youngjoygame.com,DIRECT
DOMAIN-SUFFIX,gplog-sg.byteoversea.com,DIRECT
DOMAIN-SUFFIX,xlog.byteoversea.com,DIRECT
DOMAIN-SUFFIX,tnc16-alisg.isnssdk.com,DIRECT
DOMAIN-SUFFIX,ml.aihelp.net,DIRECT
DOMAIN-SUFFIX,newlogin.ml.youngjoygame.com,DIRECT
DOMAIN-SUFFIX,cdn-sdk.aihelp.net,DIRECT
DOMAIN-SUFFIX,ml-staticsrc.s3.amazonaws.com,DIRECT
IP-CIDR,161.117.251.225/32,DIRECT
IP-CIDR,161.52.91.0/24,DIRECT
IP-CIDR,161.52.106.0/24,DIRECT
IP-CIDR,164.52.90.0/23,DIRECT
IP-CIDR,164.52.91.0/24,DIRECT
IP-CIDR,164.52.73.0/24,DIRECT
IP-CIDR,164.52.106.0/23,DIRECT
IP-CIDR,164.52.2.0/24,DIRECT
IP-CIDR,169.54.192.0/18,DIRECT
IP-CIDR,169.55.192.0/18,DIRECT

# Facebook
DOMAIN-SUFFIX,mbasic.facebook.com,✅Select,force-remote-dns
DOMAIN-SUFFIX,cdninstagram.com,✅Select,force-remote-dns
DOMAIN-SUFFIX,facebook.com,✅Select,force-remote-dns
DOMAIN-SUFFIX,facebook.net,✅Select,force-remote-dns
DOMAIN-SUFFIX,fb.com,✅Select,force-remote-dns
DOMAIN-SUFFIX,fb.me,✅Select,force-remote-dns
DOMAIN-SUFFIX,fbcdn.net,✅Select,force-remote-dns
DOMAIN-SUFFIX,instagram.com,✅Select,force-remote-dns
DOMAIN-SUFFIX,whatsapp.net,✅Select,force-remote-dns
DOMAIN-SUFFIX,whatsapp.com,✅Select,force-remote-dns

# Telegram
IP-CIDR,91.108.56.0/22,✅Select,no-resolve
IP-CIDR,91.108.4.0/22,✅Select,no-resolve
IP-CIDR,91.108.8.0/22,✅Select,no-resolve
IP-CIDR,109.239.140.0/24,✅Select,no-resolve
IP-CIDR,149.154.160.0/20,✅Select,no-resolve
IP-CIDR,149.154.164.0/22,✅Select,no-resolve

# LAN
DOMAIN-SUFFIX,local,DIRECT
IP-CIDR,192.168.0.0/16,DIRECT
IP-CIDR,10.0.0.0/8,DIRECT
IP-CIDR,172.16.0.0/12,DIRECT
IP-CIDR,127.0.0.0/8,DIRECT
IP-CIDR,100.64.0.0/10,DIRECT

FINAL,✅Select'''

    op_file_conf.write(f"{rules_files}")
    print(f"{rules_files}")
    op_file_conf.close()

    print("\n\n\33[92m--------------[GENERATE DONE]--------------\33[0m\n")

akunvmess()
