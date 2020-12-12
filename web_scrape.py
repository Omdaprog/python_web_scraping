from urllib.request import Request , urlopen
from bs4 import BeautifulSoup
import requests
import os 




path = "C:\\Users\\imed\\Desktop\\majduub-web-scrape"
url = 'https://www.marcelwanders.com'
url1 = 'https://www.marcelwanders.com/projects/'
url2 = 'https://www.marcelwanders.com/work/'




req = Request(url1)
html_page = urlopen(req)
soup = BeautifulSoup(html_page, "lxml")
image_src = []
links = []
folder_name = []
errors = []



for link in soup.findAll('a'):
    L = link.get('href')
    if "/work/" in L:
        links.append(L)
        folder_name.append(L[5:].replace('/',''))


def get_image_link(link, project):
    r = requests.get('https://www.marcelwanders.com' + link)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')
    for image in images: 
        try:
            print(project + "========>" + image['data-src'])
        except:
            errors.append(image)

def imagedownload(url, folder):
    try: 
        os.mkdir(os.path.join(path, folder))
    except:
        pass

    os.chdir(os.path.join(path, folder))
    r = requests.get('https://www.marcelwanders.com' + url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')
    for index, image in enumerate(images):
        try:
            link = "https://www.marcelwanders.com" + str(image['data-src'])
        except:
            link = "https://www.marcelwanders.com" + str(image['src'])
        
        with open(folder + str(index) + '.png' , 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print("download " + folder + str(index) + "................")
    

for index, i in enumerate(links):
    imagedownload(i , folder_name[index])
    # get_image_link(i , folder_name[index])


