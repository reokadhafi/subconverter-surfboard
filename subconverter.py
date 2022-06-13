import binascii
import os
import json
from json import JSONDecodeError
from base64 import b64decode

banner = '''\33[94m
   _____ __  ______  __________  _   ___    ____________  ________________ 
  / ___// / / / __ )/ ____/ __ \/ | / / |  / / ____/ __ \/_  __/ ____/ __ \\
  \__ \/ / / / __  / /   / / / /  |/ /| | / / __/ / /_/ / / / / __/ / /_/ /
 ___/ / /_/ / /_/ / /___/ /_/ / /|  / | |/ / /___/ _, _/ / / / /___/ _, _/ 
/____/\____/_____/\____/\____/_/ |_/  |___/_____/_/ |_| /_/ /_____/_/ |_|
v.1.0.1 \33[33m@reokadhafi\33[0m                                                       
'''
tutor = '''::\33[0m::::::::::::::==[Tutorial]==::::::::::::::::
\33[0m::\33[90m- Masukkan akun vmess di bawah            \33[0m::
\33[0m::\33[90m- Jika akun vmess lebih dari 1 maka       \33[0m::
\33[0m::\33[90m  pisahkan dengan tanda (;) tanpa spasi   \33[0m::
\33[0m::\33[90m- Copas Config langsung dari layar termux \33[0m::
\33[0m::\33[90m  mulai dari [General] sampe akhir FINAL  \33[0m::
::::::::::::::::::::::::::::::::::::::::::::::\33[0m'''

def real_path(file_name):
	return os.path.dirname(os.path.abspath(__file__)) + file_name

def generate(database):
    data_json = parsing(database)
    bug = 'cf-vod.nimo.tv'
    host_akun = data_json['ps']
    server_vmess = data_json['add']
    server_host = data_json['host']
    server_path = data_json['path']
    server_username = data_json['id']
    if server_vmess == bug:
        proxy_payload = (f"{host_akun} = vmess, {bug}, 80,  username={server_username}, tls=false, ws=true, ws-path={server_path}, sni={server_host}, ws-headers=Host:{server_host}, skip-cert-verify=1, tfo=true, udp-relay=true")
    if server_vmess != bug:
        proxy_payload = (f"{host_akun} = vmess, {bug}, 80,  username={server_username}, tls=false, ws=true, ws-path={server_path}, sni={server_vmess}, ws-headers=Host:{server_vmess}, skip-cert-verify=1, tfo=true, udp-relay=true")
    return proxy_payload, host_akun

def parsing(data):
    try:
        data_json = json.loads(b64decode(data.replace("vmess://", "")))
        data_json['ps'] = data_json['add']
    except binascii.Error:
        try:
            data_json = json.loads(b64decode(data.replace("vmess://", "") + '=' * (-len(data) % 4)))
            data_json['ps'] = data_json['add']
        except binascii.Error:
            print('\33\n\n[91mTerjadi Kesalahan Mengurai Json [1]!!!\33[0m')
            print("\33[91mUlangi Gaaess!!!\33[0m\n\n")
            exit()
    except JSONDecodeError:
        print('\33\n\n[91mTerjadi Kesalahan Mengurai Json [2]!!!\33[0m')
        print("\33[91mUlangi Gaaess!!!\33[0m\n\n")
        exit()
    return data_json

def main():
    akun_mentah = input('\n\33[92mCopy akun vmess disini \33[0m=>> ').split(';')
    file_general = open(real_path('/General.conf'),encoding='utf-8').read()
    file_rule = open(real_path('/Rule.conf'),encoding='utf-8').read()
    file_proxy = open(real_path('/Proxy.conf'),'w', encoding='utf-8')
    file_config = open(real_path('/SURFBOARD.conf'),'w', encoding='utf-8')
    select = '✅Select = select,🔁LoadBalance,🚀BestPing'
    loadbalance = '🔁LoadBalance = load-balance'
    bestping = '🚀BestPing = url-test,url=http://www.gstatic.com/generate_204, interval=600, tolerance=100, timeout=5, hidden=false'
    data_nama_akun =[]
    data_proxy = []
    nol = 0
    for database in akun_mentah:
        proxy = generate(database)[0]
        nama_akun = generate(database=database)[1]
        data_nama_akun.append(nama_akun)
        data_proxy.append(proxy)
    print("\n\n\33[92m--------------[GENERATE CONFIG]--------------\33[0m\n")
    file_config.write(f'{file_general}\n')
    print(f'{file_general}\n')
    file_proxy.write('[Proxy]\n')
    print(f'[Proxy]')
    nol = 0
    for i in akun_mentah:
        file_proxy.write(f'{data_proxy[nol]}\n')
        print(f'{data_proxy[nol]}')
        nol +=1
    file_proxy.write('\n[Proxy Group]')
    print('\n[Proxy Group]')
    file_proxy.write(f'\n{select}')
    print(select, end='')
    nol = 0
    for i in akun_mentah:
        file_proxy.write(f', {data_nama_akun[nol]}')
        print(f', {data_nama_akun[nol]}', end='')
        nol +=1
    file_proxy.write(f'\n{loadbalance}')
    print(f'\n{loadbalance}', end='')
    nol = 0
    for i in akun_mentah:
        file_proxy.write(f', {data_nama_akun[nol]}')
        print(f', {data_nama_akun[nol]}', end='')
        nol +=1
    file_proxy.write(f'\n{bestping}')
    print(f'\n{bestping}', end='')
    nol = 0
    for i in akun_mentah:
        file_proxy.write(f', {data_nama_akun[nol]}')
        print(f', {data_nama_akun[nol]}', end='')
        nol +=1
    file_proxy.close()
    file_proxy = open(real_path('/Proxy.conf'),encoding='utf-8').read()
    file_config.write(f'\n{file_proxy}\n')
    file_config.write(f'\n{file_rule}\n')
    file_config.close()
    print(f'\n\n{file_rule}\n')
    print("\n\33[92m--------------[GENERATE CONFIG DONE]--------------\33[0m\n")

if __name__ == '__main__':
    print(banner)
    print(tutor)
    while True:
        try:
            main()
        except (UnicodeDecodeError):
            print("\n\n\33[91mTerjadi Kesalahan Input!!!\33[0m")
            print("\33[91mUlangi Gaaess!!!\33[0m\n\n")
            exit()