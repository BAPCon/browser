import os

import requests
import sys
import xml.etree.ElementTree as ET
import zipfile

def get_chrome_driver(target_dir):

    url = ""

    if sys.platform == "win32":
        url = "https://chromedriver.storage.googleapis.com/"+target_dir+"chromedriver_win32.zip"

    resp = requests.get(url)

    try:
        os.mkdir("chromedriver")
    except:
        pass

    f = open("chromedriver_"+sys.platform+".zip","wb")
    f.write(resp.content)
    f.close()



    with zipfile.ZipFile("chromedriver_"+sys.platform+".zip", 'r') as zip_ref:
        zip_ref.extractall("chromedriver")

    

def chrome_install():

    if sys.platform == "win32":

        path = "C:\Program Files (x86)\Google\Chrome\Application"

        target_version = None
        max_version = 0
        for obj in os.listdir(path):
            if obj.count(".") > 1:
                inds = obj.split(".")
                try:
                    for ind in inds:
                        int(ind)
                    if int(obj.replace(".","")) > max_version:
                        max_version = int(obj.replace(".",""))
                        target_version = ".".join(obj.split(".")[:-1])
                except Exception as e: print(e)

        url = "https://chromedriver.storage.googleapis.com/?delimiter=/&prefix=" + target_version

        resp = requests.get(url)

        tree = ET.fromstring(resp.text)

        target_dir = None
        max_version = 0

        for child in tree:
            if child.tag.count("Prefixes") > 0:
                vs = int(child[0].text.replace(".","").replace("/",""))
                if vs > max_version:
                    target_dir = child[0].text

        get_chrome_driver(target_dir)
chrome_install()