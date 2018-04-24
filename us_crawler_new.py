import requests
global date
import bs4 as bs 
import datetime
import pytz
#import os
import uuid
import json,time,django
from treciproj import settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "treciproj.settings")
django.setup()
from RaceApp.models import Country,Podesavanja
global headers
headers = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)', 'origin': 'http://www.equibase.com',
                'x-requested-with': 'XMLHttpRequest'}
def get_proxy():
    bumbum = 'http://api.proxyrotator.com/?apiKey=xPEjwuFkAhRrX2v43ZgVzcMWpQ9Gfs8H'

    r = requests.get(bumbum)

    jsonik = json.loads(r.text)
    proxies = {
        'http' : 'http://' + jsonik['proxy'],
    }
    print(jsonik['proxy'])
    return proxies
def get_table(table):
    #soup = bs.BeautifulSoup(table,'lxml')
    i=0
    print("Table TEST")
    dictlist = []
    for tr in table.find_all('tr'):
            
            i+=1
            tds = tr.find_all('td')
            if(i==1):
                sire = (tds[0].text)
            if(i==3):
                dict = {
            'sire' : sire,
            'name' : tds[0].text,
            'foals' : tds[2].text,
            'starters' : tds[3].text.replace(" ", "").replace("(", ",").replace(")",""),
            'winners' :  tds[4].text.replace(" ", "").replace("(", ",").replace(")",""),
            'BW (%)' : tds[5].text.replace(" ", "").replace("(", ",").replace(")",""),
            'earnings' : tds[6].text.replace("$", "").replace(",",""),
            'ael' : tds[7].text,
                }
            # print(dict)
                dictlist.append(dict)
            if(i==5):
                sire = (tds[0].text)
            if(i==7):
                dict = {
                'sire' : sire,
                'name' : tds[0].text,
                'mares' : tds[1].text,
                'foals' : tds[2].text,
                'starters' : tds[3].text.replace(" ", "").replace("(", ",").replace(")",""),
                'winners' :  tds[4].text.replace(" ", "").replace("(", ",").replace(")",""),
                'BW (%)' : tds[5].text.replace(" ", "").replace("(", ",").replace(")",""),
                'earnings' : tds[6].text.replace("$", "").replace(",",""),
                'ael' : tds[7].text,
                }   
                #print(dict)
                dictlist.append(dict)
            if(i==9):
                sire = (tds[0].text)
            if(i==11):
                dict = {
                'sire' : sire,
                'mares' : tds[1].text,
                'foals' : tds[2].text,
                'starters' : tds[3].text.replace(" ", "").replace("(", ",").replace(")",""),
                'winners' :  tds[4].text.replace(" ", "").replace("(", ",").replace(")",""),
                'BW (%)' : tds[5].text.replace(" ", "").replace("(", ",").replace(")",""),
                'earnings' : tds[6].text.replace("$", "").replace(",",""),
                'ael' : tds[7].text,
                }   
                #print(dict)
                dictlist.append(dict)
    return(dictlist)
def get_horses(racelist):
    proxies = {
    'http' : 'http://159.65.107.239:8888',
    'https' : 'https://159.65.107.239:8888',
    }
    headers = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)', 'origin': 'http://www.equibase.com',
                'x-requested-with': 'XMLHttpRequest'}
    for race in racelist:
        ##proxies = get_proxy()
        horselist = []
        #http://www.equibase.com/static/entry/
        url = race['URL']
        try:
            reqhor = requests.get(url)
        except:
            time.sleep(6)
            reqhor = requests.get(url)
        supa = bs.BeautifulSoup(reqhor.text, 'lxml')
        for tr in supa.find_all('tr'):
            tds = tr.find_all('td')
        #print(type(tds))
            if(len(tds)==12 or len(tds)==11):
                #print(tds)
                horsename = tds[2].text.strip(' \t\n\r').strip()[:-4].replace(" ", "%20")
                #print(horsename)
                print("itsthis")
                horseurl = 'http://www.equineline.com/Free5XPedigreeSearchResults.cfm?horse_name=' + horsename + '&page_state=LIST_HITS&foaling_year=&dam_name=&include_sire_line=Y'             
                #soup = bs.BeautifulSoup(horsereq.text, 'lxml')
                #h4 = soup.find('h4')
                #import requests 

                headers = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)', 
                                'x-requested-with': 'XMLHttpRequest','Accept-Encoding' : 'gzip, deflate', 
                                'Cache-Control': 'max-age=0', 'Connection' : 'keep-alive', 'Cookie' : 'CFID=42760483; CFTOKEN=bdd03ad8b9d75f10%2D2152DD43%2D5056%2DBE2F%2D78E5D1FFBA809844; TIMEVISITED=%7Bts%20%272018%2D04%2D21%2015%3A43%3A55%27%7D; __unam=10bb875-162e9bbc10f-42955c48-10',
                                'Host' : 'www.equineline.com','Referer' : "equineline.com",
                                'Upgrade-Insecure-Requests' : '1' }
                                #http://www.equineline.com/Free5XPedigreeSearchResults.cfm?horse_name=' + horsename + '&page_state=LIST_HITS&foaling_year=&dam_name=&include_sire_line=Y'
                                #http://www.equineline.com/Free-5X-Pedigree.cfm/=Winner%20(JPN)?page_state=DISPLAY_REPORT&reference_number=9851563&registry=T&horse_name==Winner%20(JPN)&dam_name==Winner%20Balance%20(JPN)&foaling_year=2013&include_sire_line=Y
                #horsename = "Jack(AUS)"
                while(1):
                    horsereq = requests.get("http://www.equineline.com/Free5XPedigreeSearchResults.cfm?horse_name=" + horsename + "&page_state=LIST_HITS&foaling_year=&dam_name=&include_sire_line=Y",headers=headers,proxies=proxies)
                    try:
                        soup = bs.BeautifulSoup(horsereq.text, 'lxml')
                        print(horsereq.text)
                        horsrl = soup.find('a').get('href')
                    except: 
                        try:
                            ime = horsereq.headers['x-cache-proxyname']
                        except:
                            ime= horsereq.history[0].headers['x-cache-proxyname']
                        payld = {
                        'name' : ime,
                        }
                        print(ime)
                        headers={'Authorization' : 'Zm9ybXVsYTE='}
                        ipic = proxies.get('http')
                        ipic = ipic[0:-1] + '9'
                        print(ipic)
                        stop = requests.post(ipic + '/api/instances/stop', json=payld,headers=headers)
                    else:
                        
                        url = 'http://www.equineline.com/' + horsrl
                        print(url)
                        start = url.find('reference_number=')
                        end = url.find('&registry')
                        refnum = url[start+17:end]
                        print(refnum)
                        break

                referer = "http://www.equineline.com/Free-5X-Pedigree.cfm?page_state=PROCESS_SUBMIT&horse_name=" + horsename.replace(" ", "%20")
                headers = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)', 
                                'x-requested-with': 'XMLHttpRequest','Accept-Encoding' : 'gzip, deflate', 
                                'Cache-Control': 'max-age=0', 'Connection' : 'keep-alive', 'Cookie' : "CFID=42760483; CFTOKEN=bdd03ad8b9d75f10%2D2152DD43%2D5056%2DBE2F%2D78E5D1FFBA809844; TIMEVISITED=%7Bts%20%272018%2D04%2D21%2015%3A43%3A55%27%7D; __unam=10bb875-162e9bbc10f-42955c48-14",
                                'Host' : 'www.equineline.com','Referer' : referer,
                                'Upgrade-Insecure-Requests' : '1' }
                link = url
                while(1):
                        
                    maker = requests.get(link,headers=headers,timeout=9,proxies=proxies)
                    supica = bs.BeautifulSoup(maker.text,'lxml')
                    table = supica.find_all('div',class_='col-xs-2 col2-pedigree')
                    #print(maker.text)
                
                    #print("\n\nKEK\n\n")
                    #print(table[0])
                    try:
                        horsebride = table[0].find_all('div')[1].text #prvi zavrsen
                    except: 
                        ime = maker.headers['x-cache-proxyname']
                        payld = {
                        'name' : ime,
                        }
                        print(ime)
                        headers={'Authorization' : 'Zm9ybXVsYTE='}
                        ipic = proxies.get('http')
                        ipic = ipic[0:-1] + '9'
                        print(ipic)
                        stop = requests.post(ipic + '/api/instances/stop', json=payld,headers=headers)
                    else:
                        break

                #print(horsebride)
                def name_fix(horse_html):
                    horsebride = horse_html
                    if(horsebride[0]==" "):
                        horsebride = horsebride[1:]
                    sechorseb = horsebride[1:]
                    zarezj = sechorseb.find(",")

                    sechorseb = sechorseb[zarezj+2:].replace("  ", "")


                    #dudu = sechorseb.find_all(" ")
                    #print(sechosreb[dudu:])
                    sechorseb = sechorseb.replace(" ", ",")
                    print(sechorseb[-1])
                    sechorseb = sechorseb[:-1]
                    if(sechorseb[-1]==","):
                        sechorseb = sechorseb[:-1]
                    #print(listic)
                    lenic = len(sechorseb)
                    firsthorse = horsebride[1:zarezj-1] + (sechorseb[0:lenic-2])
                    return firsthorse



                tabletwo = supica.find_all('div',class_='col-xs-2 col3-pedigree')
                horsehuss = tabletwo[0].find_all('div')[1].text

                final_string = (name_fix(horsebride)) + "," + (name_fix(horsehuss)) + "\n"

#print(r.headers)


                    
                horselist.append(final_string)
        race['Horses'] = horselist
        print("list: ", horselist)
    return racelist


def get_events():
    global date
    while(1):
        try:
            r = requests.get('http://www.equibase.com/static/entry/index.html?SAP=TN')
        except:
            time.sleep(3)
            #r = requests.get('http://www.equibase.com/static/entry/index.html?SAP=TN')
        else:
            break
    soup = bs.BeautifulSoup(r.text,'lxml')
    #print(soup)
    table = soup.find('table')
    #print(table)
    tr = table.find_all('tr')
    #Featured Tracks	Today	Tomorrow	Future	Past
    length = len(tr)
    eventlist = []
    for i in range(1,length,1):
        tds = tr[i].find_all('td')
        #print(tds[1])
        name = tds[0].text
        try:
            url = 'http://www.equibase.com' + tds[1].find('a').get('href')
            date = tds[1].find('a').text
        except:
            print("No event today at " + name)
        else:
            print(url)
            #url = 'http://www.equibase.com' + tds[1].find('a').get('href')
            events = {
                'date' : date,
                'name' : name,
                'url' : url,
            }
            eventlist.append(events)
    print(eventlist)
    get_races(eventlist)

def get_races(eventlist):
    for race in eventlist:
        url = race['url']
        try:
            r = requests.get(url)
        except:
            time.sleep(3)
            r = requests.get(url)
        racelist = []
        soup = bs.BeautifulSoup(r.text,'lxml')
        for tr in soup.find_all('table'):
            tds = tr.find_all('td')
            length = len(tds)
            for i in range(0,length,8):
                #print(tds[i])
                #print(tds)
                x = tds[2+i].text.strip(' \t\n\r')
            # print("X = " + x)
                #print(dir(x))
            # x = str(x)
                #print(type(x))
                x = x.replace(" ", "")
                url = tds[0+i].find('a')
                #print(url)
                url = 'http://www.equibase.com' + url.get('href')
                tabledic = {
                    'Race: ' : tds[0+i].text,
                    'URL' : url,
                    'Purse' : tds[1+i].text,
                    'Race Type' : x,
                    'Distance' : tds[3+i].text,
                    'Surface' : tds[4+i].text,
                    'Starters' : tds[5+i].text,
                    'Est. Post' : tds[6+i].text,
                    'Horses' : [],
                }
                #print(type(tabledic))
                racelist.append(tabledic)
        race['races'] = get_horses(racelist)
    jsonero = json.dumps(eventlist)
    jsonic = json.loads(jsonero)
    print("DATE:", date) #datum
    o = Country('1','America',jsonero,date) #datum
    o.save()
    datic = datetime.date.today()
    d = str(datic)
    filename = 'USA' + d + '.json'
    path = "USFiles"
    fullpath = os.path.join(path, filename)
    f = open(fullpath,'w')
    f.write(jsonero)
    f.close()
    p = Podesavanja.objects.get(id=1)
    p.is_scraping = 0
    p.save()
    headers={'Authorization' : 'Zm9ybXVsYTE='}
    scaling_payload = {
                    "min": "0",
                    "required": "0",
                    "max": "9",
                    }
    rer = requests.patch('http://159.65.107.239:8889/api/scaling',json=scaling_payload,headers=headers)
    print(rer)
    #horsrl = soup.find('a').get('href')
    
    #jsonero = json.dumps(eventlist)
    #print(jsonero)
    #f = open('racehelpme.json', 'w')
    #f.write(jsonero)
    #f.close()
                #horses['Horses'] = get_horses(horses)

    
#get_events()

while(1):
    #r = requests.get('https://www.equibase.com/static/entry/index.html')
    #soup = bs.BeautifulSoup(r.text,'lxml')
    aa = Country.objects.get(id=1)
    dated = aa.date
    proxies = {
    'http' : 'http://159.65.107.239:8888',
    'https' : 'https://159.65.107.2398888',
    }
    try:
        r = requests.get('http://www.equibase.com/static/entry/index.html?SAP=TN')
    except:
        time.sleep(6)
        r = requests.get('http://www.equibase.com/static/entry/index.html?SAP=TN')
    soup = bs.BeautifulSoup(r.text,'lxml')
    #print(soup)
    #print(soup)
    table = soup.find('table')
    #print(table)
    tr = table.find_all('tr')
    #Featured Tracks	Today	Tomorrow	Future	Past
    length = len(tr)
    eventlist = []
    for i in range(1,length,1):
        tds = tr[i].find_all('td')
        #print(tds[1])
        name = tds[0].text
        try:
            url = 'http://www.equibase.com' + tds[1].find('a').get('href')
            baba = tds[1].find('a').text
        except:
            print("No event today at ", name)
            baba=dated
        else:
            break
    if(dated==baba): 
        print("No new races for date ", dated) #proverava ako je dd jednak dd u u bazi ako jeste spava, ako nije zove event
        print("\nSleeping for 20 minutes")
        time.sleep(1200)
        continue 
    else:
        print("New race! Scraping.")
        p = Podesavanja.objects.get(id=1)
        while(1):
            if (p.is_scraping):
                print("Waiting for other crawlers to finish scraping")
                time.sleep(300)
            else:
                scaling_payload = {
                    "min": "1",
                    "required": "7",
                    "max": "9",
                    }
                headers={'Authorization' : 'Zm9ybXVsYTE='}
                #Zm9ybXVsYTE=
                rer = requests.patch('http://159.65.107.239:8889/api/scaling',json=scaling_payload, headers=headers)
                print(rer)
                #time.sleep(60)
                p.is_scraping = 1
                p.save()
                print("Saving P")
                get_events()
                break

    
#get_events()
