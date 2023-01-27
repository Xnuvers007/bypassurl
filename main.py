try:
    import requests, os, base64, json, sys, cloudscraper, re, time, random
    from sys import platform
    from urllib.parse import unquote
    from base64 import b64decode
    from html2image import Html2Image

except Exception:
    os.system("pip -r ./requirements.txt")

import credentials

__author__ = "Xnuvers007"
__version__ = "1.1.0"
__license__ = "MIT"
__copyright__ = "Copyright (c) 2023, Xnuvers007"
__credits__ = ["Xnuvers007", "site-shot.com"]


indra = Html2Image(output_path='picturess')

# adfly https://xnuvers007.github.io http://lyksoomu.com/yInl

class Main:
    def screenshot():
        if platform == "win32":
            tanya = str(input("Silahkan Masukan Link : "))
            berinama = str(input("Beri nama file screenshot (TANPA AKHIRAN jpg/png) : "))
            if tanya not in "https://":
                tanya = "https://" + tanya
            indra.screenshot(url=tanya, save_as=berinama+".png")
            print("Screenshot Berhasil Disimpan di folder picturess")

        elif platform == "linux" or platform == "linux2":
            termux = str(input("Apakah Anda Menggunakan Termux? (y/n) : "))
            if termux == "y":
                headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36',
                    }
                link2 = str(input("Masukan Link : "))
                if link2 not in "https://":
                    link2 = "https://" + link2

                try:
                    link = "http://api.screenshotlayer.com/api/capture?access_key={0}&url={1}&viewport=1440x900&width=1300".format(credentials.apikey[0], link2)
                    # get image from response
                    response = requests.get(link, headers=headers)
                except:
                    # jika apikey tidak valid, maka akan menggunakan apikey lain yang valid
                    acak = random.choice(credentials.apikey)
                    if response.status_code != 200:
                        while True:
                            try:
                                link = "http://api.screenshotlayer.com/api/capture?access_key={0}&url={1}&viewport=1440x900&width=1300".format(acak, link2)
                                # get image from response
                                response = requests.get(link, headers=headers)
                                break
                            except:
                                acak = random.choice(credentials.apikey)
                                continue
                    else:
                        pass
                berinama = str(input("Beri nama file screenshot (TANPA AKHIRAN jpg/png) : "))
                time.sleep(3)
                # save image to file
                if response.status_code == 200:
                    with open(f'./{berinama}.png', 'wb') as f:
                        f.write(response.content)
                        print("Screenshot Berhasil Disimpan di folder picturess")
                else:
                    print("APIKEY Tidak Valid")
                    print("Silahkan buat terlebih dahulu apikey terbaru di https://screenshotlayer.com/dashboard , dan gunakan https://temp-mail.org/id/")
                    buka = str(input("Apakah anda ingin membuat apikey baru? (y/n) : "))
                    if buka == "y" or buka == "Y":
                        os.system("xdg-open https://screenshotlayer.com/dashboard")
                        os.system("xdg-open https://temp-mail.org/id/")
                    else:
                        pass
            elif termux == "n":
                tanya = str(input("Silahkan Masukan Link : "))
                berinama = str(input("Beri nama file screenshot (TANPA AKHIRAN jpg/png) : "))
                if tanya not in "https://":
                    tanya = "https://" + tanya
                indra.screenshot(url=tanya, save_as=berinama+".png")
                print("Screenshot Berhasil Disimpan di folder picturess")
            else:
                print("Pilihan Tidak Diketahui")

        elif platform == "darwin":
            tanya = str(input("Silahkan Masukan Link : "))
            berinama = str(input("Beri nama file screenshot (TANPA AKHIRAN jpg/png) : "))
            if tanya not in "https://":
                tanya = "https://" + tanya
            indra.screenshot(url=tanya, save_as=berinama+".png")
            print("Screenshot Berhasil Disimpan di folder picturess")
        else:
            print("Operating System Tidak Diketahui")

    def dekripurl(code):
        a, b = '', ''
        for i in range(0, len(code)):
            if i % 2 == 0: a += code[i]
            else: b = code[i] + b
        key = list(a + b)
        i = 0
        while i < len(key):
            if key[i].isdigit():
                for j in range(i+1,len(key)):
                    if key[j].isdigit():
                        u = int(key[i]) ^ int(key[j])
                        if u < 10: key[i] = str(u)
                        i = j					
                        break
            i+=1
        key = ''.join(key)
        decrypted = b64decode(key)[16:-16]
        return decrypted.decode('utf-8')

    def adfly(url):
        user = cloudscraper.create_scraper(allow_brotli=False)
        respons = user.get(url).text
        out = {
            'error': False,
            'message': 'Success',
            'from_url': url
        }
        try:
            byp = re.findall("ysmm\s+=\s+['|\"](.*?)['|\"]", respons)[0]
        except:
            out['error'] = True
            out['message'] = 'Failed to find bypass'
            return out
        url = Main.dekripurl(byp)
        if re.search(r'go\.php\?u\=', url):
            url = b64decode(re.sub(r'(.*?)u=', '', url)).decode()
        elif '&dest=' in url:
            url = unquote(re.sub(r'(.*?)dest=', '', url))
        out['real_url'] = url
        return out

    def kusonime():
        # Download Anime From Kusonime
        link = str(input("Masukan Link Anime : "))
        if "https://" not in link:
            link = "https://" + link
        link = link.replace("https://kusonime.com/", "")
        link = link.replace("/", "")
        # print("Link : ", link)
        main_link = "https://kusonime-scrapper.glitch.me/api/anime/" + link
        json_load = json.loads(requests.get(main_link).text)

        print("Judul : ", json_load['title'])
        print("Genre : ")
        for genre in json_load['genre']:
            # get name of genre
            # output : genre : name, name, name
            genres = genre['name']
            print(" - ", genres, " ( ", genre['url'], " )")
        
        print("Status : ", json_load['status'])
        seasons = json_load['season']['name']
        print("Season : ", seasons, " ( ", json_load['season']['url'], " )")
        # for seasons in json_load['season']:
        #     # get name of season
        #     # output : season : name, name, name
        #     season = seasons['name']
        #     print("Season : ", season, " ( ", seasons['url'], " )")

        # print("Produser/Studio : ", json_load['producers'])
        produser = json_load['producers']
        produser_name = ", ".join(produser)
        print("Produser/Studio : ", produser_name)
        
        print("Tipe : ", json_load['type'])
        print("Total Episode : ", json_load['total_eps'])
        print("Rating : ", json_load['score'])
        print("Durasi : ", json_load['durasi'])
        print("rilis : ", json_load['release'])
        print("Sinopsis : ", json_load['sinopsis'])
        print("\n")
        for linkdownload in json_load['list_download']:
            print(linkdownload[0], " \n ") #, linkdownload[1], " )")
        for items in json_load["list_download"][0][1]:
            print("==============================================")
            print("Resolusi : "+items['resolusi'])
            print("==============================================")
            for linkurl in items['link_download']:
                print("| "+linkurl['platform'], " : ", linkurl['link']+" |")
            print("==============================================")

        tanya = str(input("Apakah Ingin Membuka Link? (y/n) : "))
        if tanya=="y" or tanya=="Y":
            masukanlik = str(input("Masukan Link : "))
            if platform == "linux" or platform == "linux2":
                os.system("xdg-open " + masukanlik)
            elif platform == "darwin":
                os.system("open " + masukanlik)
            elif platform == "win32":
                os.system("start " + masukanlik)
            else:
                print("Operating System Tidak Diketahui")
        else:
            sys.exit(1)

        # input("Press Enter to exit...")

        # exit(code=None)

    def ahr():
        # Redirect Url via Bypass aHR
        # session = requests.Session()
        masukan = str(input("Masukan Link : "))

        # if "https://" not in masukan:
        #     masukan = "https://" + masukan
        
        # get domain
        masukan = masukan.replace("https://", "") or masukan.replace("http://", "")
        masukan = masukan.replace("&type=2", "")
        match = re.search(r'(?<=url=)[a-zA-Z0-9]+', masukan)
        if match:
            ahr = match.group()
            print("\n")
            print("Real URL : ", base64.b64decode(ahr).decode("utf-8"))
        else:
            print("Bagian 'ahr' tidak ditemukan")
        # masukan = masukan.replace("https://semawur.com/full?api=3f184c48f4342c9bfd30a87a3f14dc9b57934868&url=", "")
        # masukan = masukan.replace("&type=2", "")

        # print("Real URL : ", base64.b64decode(masukan).decode("utf-8"))

        # print("\n")

        tanya = str(input(" Apakah Ingin Membuka Url? (y/n) : "))
        if tanya=="y" or tanya=="Y":
            if platform == "linux" or platform == "linux2":
                os.system("xdg-open " + base64.b64decode(masukan).decode("utf-8"))
            elif platform == "darwin":
                os.system("open " + base64.b64decode(masukan).decode("utf-8"))
            elif platform == "win32":
                os.system("start " + base64.b64decode(masukan).decode("utf-8"))
        else:
            exit(code=None)

        ## response = session.get(masukan, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.52'}, allow_redirects=False)

        # lokasi = response.headers['Location']
        ## lokasi = response.headers.get("location")
        ## print("Lokasi : ", lokasi)
        # time.sleep(12)
        # a = requests.get(lokasi, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.52'}).text

        # print(a)
        # print("Lokasi : ", lokasi)
        ## response = session.get(lokasi, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.52'}, allow_redirects=True)

        ## real = response.url
        # time.sleep(10)
        # # Show HTML
        # print(requests.get(real, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.52'}).text)
        ## print("Real Url : ", real)
        # exit(code=None)

    def main():
        print("\n=====================================\n")
        print("    Redirect Checker by Xnuvers007    \n")
        print("=====================================\n")
        try:
            tanya = int(input('''
        1. Cek Redirect (bit.ly, s.id, tinyurl, dll.)
        2. Cek Redirect (Bypass aHR = semawur, adpaylink, dll.)
        3. Donation
        4. Download Anime (Kusonime)
        5. Cek Redirect (Bypass Adfly)
        6. Exit
        7. Screenshot (Screenshot website/URL)

        masukan pilihan : '''))
        except (ValueError, TypeError, KeyboardInterrupt):
            os.system("clear||cls")
            Main.main()
        if tanya==1:
            masukan = str(input("Masukan Link : "))
            # if user input is domain then add https://
            if "https://" not in masukan:
                masukan = "https://" + masukan
                # masukan = masukan.replace("https://", "")
            
            # url = 'https://www.redirect-checker.org/'
            # data = {'redirecturl_i_want_and_not_you': masukan,
            #         'useragent': '2300'}

            response = requests.get(masukan, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.52'}, allow_redirects=True)

            # get url after redirect from response
            url = response.url

            # get status code from response
            status = response.status_code

            # get all headers from response
            headers = response.headers

            # get all cookies from response
            cookies = response.cookies

            # get all history from response
            history = response.history

            print("\n")

            print("url : ", url)
            print("status : ", status)
            print("Time from headers : ", headers['Date'])
            try:
                print("Server : ", headers['Server'])
                print("Teknologi : ", headers['X-Powered-By'])
            except:
                pass
            print("cookies : ", requests.utils.dict_from_cookiejar(cookies))
            print("history : ", [h.url for h in history])
            if platform == "linux" or platform == "linux2":
                os.system("xdg-open " + url)
            elif platform == "darwin":
                os.system("open " + url)
            elif platform == "win32":
                os.system("start " + url)
            else:
                pass
            input("\nenter to exit")
            exit(code=None)
        elif tanya==2:
            Main.ahr()
        elif tanya==3:
            if platform == "linux" or platform == "linux2":
                os.system("xdg-open https://saweria.co/xnuvers007")
            elif platform == "darwin":
                os.system("open https://saweria.co/xnuvers007")
            elif platform == "win32":
                os.system("start https://saweria.co/xnuvers007")
        elif tanya==4:
            Main.kusonime()
        elif tanya==5:
            url = str(input("Masukan Link : "))
            Main.adfly(url)
            respons = Main.adfly(url)
            print(respons['message'],'\n', respons['from_url'], ' -> ', respons['real_url'] if not respons['error'] else 'Error')
            tanya = str(input(" Apakah Ingin Membuka Url? (y/n) : "))
            if tanya == 'y' or tanya == 'Y':
                if platform == "linux" or platform == "linux2":
                    os.system("xdg-open " + respons['real_url'])
                elif platform == "darwin":
                    os.system("open " + respons['real_url'])
                elif platform == "win32":
                    os.system("start " + respons['real_url'])
            input("Press Enter to exit...")
            exit(code=None)
        elif tanya==6:
            exit(code=None)
        elif tanya==7:
            # call screenshot function
            Main.screenshot()
                
        else:
            print("Pilihan Tidak Ada")
            Main.main()

if __name__ == "__main__":
    while True:
        os.system("cls||clear")
        # mymain = Main()
        Main.main()
        tanya = input("Ulangi Lagi ? (y/n) : ")
        if tanya == "y" or tanya == "Y":
            continue
        else:
            break

