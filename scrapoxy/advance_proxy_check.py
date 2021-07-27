import urllib.request
import socket
import urllib.error
import csv

def is_bad_proxy(pip):    
    try:
        proxy_handler = urllib.request.ProxyHandler({'http': pip})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        req=urllib.request.Request('https://www.discogs.com/ru/ru/release/1')  # change the URL to test here
        sock=urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)
        return e.code
    except Exception as detail:
        print("ERROR:", detail)
        return True
    return False

def main():
    socket.setdefaulttimeout(120)

    # two sample proxy IPs
    proxyList = []
    clear_proxy = []
    with open('proxytest.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            proxyList.append(row[0])
    #proxyList = ['125.76.226.9:80', '25.176.126.9:80']

    for currentProxy in proxyList:
        if is_bad_proxy(currentProxy):
            print("Bad Proxy %s" % (currentProxy))
        else:
            print("%s is working" % (currentProxy))
            clear_proxy.append(currentProxy)
    with open('clear_proxy.txt', 'w') as w:
        for item in clear_proxy:
            w.write("%s\n" % item)


if __name__ == '__main__':
    main() 
