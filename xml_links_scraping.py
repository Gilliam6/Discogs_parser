import requests
from bs4 import BeautifulSoup
import re
import lxml

def xml_parser(url):
    xml_links = []
    xml_body = requests.get(url)
    soup = BeautifulSoup(xml_body.content, 'xml')
    links = soup.find_all('loc')
    for link in links:
        xml_links.append(link.text)
    return xml_links 

xml_links = xml_parser('https://www.discogs.com/sitemap_release.xml')
print(xml_links)

def release_xml_parser(xml_links):
    release_xml_links = []
    n = 1
    for link in xml_links:
        xml_release = requests.get(link)
        soup = BeautifulSoup(xml_release.content, 'xml')
        links = soup.find_all('loc')
        print(n)
        if n % 50 == 0:
            with open('xml_release_links.txt', 'w') as m:
                for link in release_xml_links:
                    m.write("%s\n" % link)
        n += 1
        for l in links:
            release_xml_links.append(l.text)
            print(l.text)
    return release_xml_links

release_xml_links = release_xml_parser(xml_links)
print(len(release_xml_links))
with open('xml_release_links.txt', 'w') as f:
    for link in release_xml_links:
        f.write("%s\n" % link)
