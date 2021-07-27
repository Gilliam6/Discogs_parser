import requests
import csv
import concurrent.futures

proxylist = []
valid_proxy = []

with open("proxytest.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        proxylist.append(row[0]) 
print(proxylist)
def iter(proxy):
    try:
        r = requests.get("https://httpbin.org/ip", proxies = {'http':'http://'+proxy,'https':'http://'+proxy}, timeout = 5)
       # print(proxy + " - Working!")
        valid_proxy.append(proxy)
    except:
        pass
    return proxy
#iter('195.138.83.218:53281')

with concurrent.futures.ThreadPoolExecutor() as exe:
    exe.map(iter, proxylist)
print(valid_proxy)
print(len(valid_proxy))

with open("valid_list.txt", "w") as w:
    for item in valid_proxy:
        w.write("%s\n" % item)
