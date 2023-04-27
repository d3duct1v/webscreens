# Webscreens
Webscreens is a Python tool that takes screenshots from a list of URLs then creates a zip archive of the output directory containing the screenshots.

## Installation
Chrome and chromedriver installation on Kali.

### 1. Install Chrome Browser
```bash
sudo apt update
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb

# Get Version
google-chrome-stable --no-sandbox
```

### 2. Download Chrome Driver
Goto https://chromedriver.chromium.org/downloads follow the installed version link for download URL.  Use that URL in the first `wget` command.
```bash
wget https://chromedriver.storage.googleapis.com/112.0.5615.49/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin/
chmod 755 /usr/local/bin/chromedriver
```

### 3. Install Selenium
Selenium provides a convenient API to access Selenium WebDrivers like Firefox, Ie, Chrome, Remote etc. The current supported Python versions are 3.5 and above.
```bash
pip3 install selenium
```

## Usage
```
usage: webscreens [-h] [-i INFILE] [-D OUT_DIR]

            :::       ::: :::::::::: :::::::::   ::::::::   ::::::::  :::::::::  :::::::::: :::::::::: ::::    :::  ::::::::  
            :+:       :+: :+:        :+:    :+: :+:    :+: :+:    :+: :+:    :+: :+:        :+:        :+:+:   :+: :+:    :+: 
            +:+       +:+ +:+        +:+    +:+ +:+        +:+        +:+    +:+ +:+        +:+        :+:+:+  +:+ +:+        
            +#+  +:+  +#+ +#++:++#   +#++:++#+  +#++:++#++ +#+        +#++:++#:  +#++:++#   +#++:++#   +#+ +:+ +#+ +#++:++#++ 
            +#+ +#+#+ +#+ +#+        +#+    +#+        +#+ +#+        +#+    +#+ +#+        +#+        +#+  +#+#+#        +#+ 
             #+#+# #+#+#  #+#        #+#    #+# #+#    #+# #+#    #+# #+#    #+# #+#        #+#        #+#   #+#+# #+#    #+# 
              ###   ###   ########## #########   ########   ########  ###    ### ########## ########## ###    ####  ######## 

            webscreens takes a list of URLs and saves a PNG screenshot into the designated directory.

options:
  -h, --help            show this help message and exit
  -i INFILE, --infile INFILE
                        File with a list of urls to screenshot.
  -D OUT_DIR, --dir OUT_DIR
                        Directory to put screenshots. *Does not have to exist.*

Example:
    python3 webscreens.py -i urls -D Google
```

## Additional Information
Setting the Chrome driver inside a Python Script is important for the script to function correctly, the following is what is needed.

### 1. Chrome
```python
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chromedriver_path = '/usr/local/bin/chromedirver'
s = Service(chromedriver_path)

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=s, options=chrome_options)
```

### 2. Firefox
Download the Firefox driver https://github.com/mozilla/geckodriver/releases (browser versions >=60, driver ver. 26)
```python
from selenium import webdirver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False
browser = webdriver.Firefox(capabilities=cap, executable_path=r'/root/Tools/Firefox/geckodriver')
```
