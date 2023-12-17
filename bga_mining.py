from bs4 import BeautifulSoup
import requests
from threading import Thread, Event
import time

def cat_wifi(url, course_names):
    cookies = {
        'cc_cookie_demo2': '{"categories":["necessary"],"level":["necessary"],"revision":0,"data":null,"rfc_cookie":false,"consent_date":"2023-07-07T11:16:40.387Z","consent_uuid":"990128e7-a76c-4ca0-9bb9-a027eb24bf19","last_consent_update":"2023-07-07T11:16:40.387Z"}',
    }

    headers = {
        'authority': 'www.bgasecurity.com',
        'accept': '*/*',
        'accept-language': 'tr-TR,tr;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.bgasecurity.com',
        'referer': "https://www.bgasecurity.com/makaleler/ddos-ataklari-ddos-cesitleri-ddos-etkileri-ve-cozumleri/",
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    headers["referer"] = url
    gecici =url.split("/")[4]
    data = {
        'action': 'loadmore',
        'query': '{"makaleler":"","error":"","m":"","p":0,"post_parent":"","subpost":"","subpost_id":"","attachment":"","attachment_id":0,"name":"","pagename":"","page_id":0,"second":"","minute":"","hour":"","day":0,"monthnum":0,"year":0,"w":0,"category_name":"","tag":"","cat":"","tag_id":"","author":"","author_name":"","feed":"","tb":"","paged":0,"meta_key":"","meta_value":"","preview":"","s":"","sentence":"","title":"","fields":"","menu_order":"","embed":"","category__in":[],"category__not_in":[],"category__and":[],"post__in":[],"post__not_in":[],"post_name__in":[],"tag__in":[],"tag__not_in":[],"tag__and":[],"tag_slug__in":[],"tag_slug__and":[],"post_parent__in":[],"post_parent__not_in":[],"author__in":[],"author__not_in":[],"search_columns":[],"ignore_sticky_posts":false,"suppress_filters":false,"cache_results":true,"update_post_term_cache":true,"update_menu_item_cache":false,"lazy_load_term_meta":true,"update_post_meta_cache":true,"post_type":"","posts_per_page":6,"nopaging":false,"comments_per_page":"10","no_found_rows":false,"taxonomy":"makaleler","term":"","order":"DESC"}',
        'page': '1',
    }
    data["query"]=data["query"][:1060]+gecici+data["query"][1060:]
    data["query"]=data["query"][:14]+gecici+data["query"][14:]
    try:
        response = requests.post('https://www.bgasecurity.com/wp-admin/admin-ajax.php',headers=headers, data=data)
        parser = BeautifulSoup(response.text,"html.parser")
        course_divs = parser.find_all("div",{"class":"wordarea"})
        course_divs2= parser.find_all("div",{"class":"pparea"})
        course_divs.extend(course_divs2)
        for course_div in course_divs:
            content=course_div.find("a")
            course_names.append(content["title"].strip())
            # print(content["title"].strip())
        return course_names
    except Exception as e:
        print(e)
        return e
        pass

def bga_makaleler():
    url_adli     = "https://www.bgasecurity.com/makaleler/adli-bilisim-teknikleri-ve-yontemleri-adli-bilisim-cesitleri-bilisim-suclari/"
    url_ag       = "https://www.bgasecurity.com/makaleler/ag-guvenligi-ag-yapilandirma-temel-ag-konulari-ag-katmanlari-ve-islevleri/"
    url_ddos     = "https://www.bgasecurity.com/makaleler/ddos-ataklari-ddos-cesitleri-ddos-etkileri-ve-cozumleri/"
    url_firewall = "https://www.bgasecurity.com/makaleler/firewallips-waf-ids-snort-modsecurity-guvenlik-protokollerinin-kullanimi-kurulumu-ve-konfigurasyonu/"
    url_genel    = "https://www.bgasecurity.com/makaleler/genel-terimsel-kavramlar-tartisamalar-incelemeler/"
    url_pentest  = "https://www.bgasecurity.com/makaleler/pentest-network-pentest-web-pentest-ddos-pentest-cloud-pentest-wireless-pentest-vs/"
    url_web      = "https://www.bgasecurity.com/makaleler/web-ve-uygulama-guvenligi-guvenli-uygulama-nasil-gelistir-gelistirilirken-alinacak-tedbirler-yontemler-neler/"
    url_wifi     = "https://www.bgasecurity.com/makaleler/wireless-guvenligi-wireless-sifreleme-turleri-ve-hassasiyetleri-alinabilecek-yontemler/"
    event = Event()
    all_names=[]
    course_names = []
    thread_adli = Thread(target=cat_wifi, args=(url_adli, course_names))
    thread_ag = Thread(target=cat_wifi, args=(url_ag, course_names))
    thread_ddos = Thread(target=cat_wifi, args=(url_ddos, course_names))
    thread_firewall = Thread(target=cat_wifi, args=(url_firewall, course_names))
    thread_genel = Thread(target=cat_wifi, args=(url_genel, course_names))
    thread_pentest = Thread(target=cat_wifi, args=(url_pentest, course_names))
    thread_web = Thread(target=cat_wifi, args=(url_web, course_names))
    thread_wifi = Thread(target=cat_wifi, args=(url_wifi, course_names))
    # ------------------------------------------------------------------------------------------------------------------
    thread_adli.start()
    thread_ag.start()
    thread_ddos.start()
    thread_firewall.start()
    thread_genel.start()
    thread_pentest.start()
    thread_web.start()
    thread_wifi.start()
    # ------------------------------------------------------------------------------------------------------------------
    thread_adli.join()
    thread_ag.join()
    thread_ddos.join()
    thread_firewall.join()
    thread_genel.join()
    thread_pentest.join()
    thread_web.join()
    thread_wifi.join()
    event.set()
    #-------------------------------------------------------------------------------------------------------------------
    all_names+=course_names
    return all_names

bga_makaleler()
