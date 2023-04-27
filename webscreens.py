from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdrvier.chrome.service import Service
import argparse
from argparse import RawTextHelpFormatter
import os
import shutil
from time import sleep
from sys import exit


# Global array
URL_ERRORS = []


def ScrapeIt(url):
    # Set Filename
    url2 = url.split('//')
    outfile = f"{url2[1]}.png"

    try:
        # Setting Selenium
        CHROMEDRIVER_PATH = '/usr/bin/local/chromedriver'
        s = Service(CHROMEDRIVER_PATH)
        WINDOW_SIZE = "1920,1080"

        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--window-size=%s' % WINDOW_SIZE)
        chrome_options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(service=s, options=chrome_options)

        # Fetch URL
        driver.get(url)
        print(f"    {driver.title}")
        sleep(1)
        some_bytes = driver.get_screenshot_as_png()
        with open(outfile, "wb") as binfile:
            binfile.write(some_bytes)
    except:
        print(f"[!] Error: {url}")
        URL_ERRORS.append(url)

    return

def dirChecker(out_dir):
    if os.path.isdir(out_dir):
        # Directory exists
        os.chdir(out_dir)
    else:
        # Directory does not exist
        os.mkdir(out_dir)
        os.chdir(out_dir)
    pic_dir = os.getcwd()

    return out_dir, pic_dir


def urlParser(file_in):
    file1 = open(file_in)
    arr1 = file1.readlines()
    file1.close()
    data1 = []

    for i in arr1:
        data1.append(i.strip())

    return data1


def printHeader():
    head = '''
            :::       ::: :::::::::: :::::::::   ::::::::   ::::::::  :::::::::  :::::::::: :::::::::: ::::    :::  ::::::::  
            :+:       :+: :+:        :+:    :+: :+:    :+: :+:    :+: :+:    :+: :+:        :+:        :+:+:   :+: :+:    :+: 
            +:+       +:+ +:+        +:+    +:+ +:+        +:+        +:+    +:+ +:+        +:+        :+:+:+  +:+ +:+        
            +#+  +:+  +#+ +#++:++#   +#++:++#+  +#++:++#++ +#+        +#++:++#:  +#++:++#   +#++:++#   +#+ +:+ +#+ +#++:++#++ 
            +#+ +#+#+ +#+ +#+        +#+    +#+        +#+ +#+        +#+    +#+ +#+        +#+        +#+  +#+#+#        +#+ 
             #+#+# #+#+#  #+#        #+#    #+# #+#    #+# #+#    #+# #+#    #+# #+#        #+#        #+#   #+#+# #+#    #+# 
              ###   ###   ########## #########   ########   ########  ###    ### ########## ########## ###    ####  ######## 

    '''
    print(head)
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog = 'webscreens',
        description = 'webscreens takes a list of URLs and saves a PNG screenshot into the designated directory.',
        epilog = '''Example:\n    python3 webscreens.py -i urls -D Google''',
        formatter_class = RawTextHelpFormatter
    )
    parser.add_argument('-i', '--infile', dest='infile', help='File with a list of URLs to screenshot.')
    parser.add_argument('-D', '--dir', dest='out_dir', help='Directory to put screenshots. *Does not have to  exist.')
    args = parser.parse_args()

    printHeader()

    # Set Starting Directory
    start_dir = os.getcwd()

    # Read in file to screenshot
    url_array = urlParser(args.infile)

    # Set Working directory
    out_dir, pic_dir = dirChecker(args.out_dir)

    # Run agains the URLs
    print(f"[ ] Fetching screenshots of {len(url_array)} URLs:")
    for url in url_array:
        ScrapeIt(url)

    # Move back to start directory
    os.chdir(start_dir)

    # Zip the PNG files.
    shutil.make_archive(out_dir, 'zip', out_dir)
    print("[*] Output files:")
    print(f"    PNG Directory:  {pic_dir}")
    print(f"    PNG Archive:    {out_dir}")

    # Write list of errored URLs
    if len(URL_ERRORS) != 0:
        filename = f"{out_dir}.ERRORS.txt"
        file1 = open(filename, "a")
        for item in URL_ERRORS:
            file1.write(f"{item}\n")

        print(f"    Error File:     {filename}")
        file1.close()

    exit()
