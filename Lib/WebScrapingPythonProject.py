
import requests
import bs4

page1='https://dream2000.com/catalogsearch/result/?q=iphone'
page2='https://dream2000.com/catalogsearch/result/index/?p=2&q=iphone'
def scrape(url):
    req= requests.get(url)
    code=req.content
    soup= bs4.BeautifulSoup(code, 'html.parser')
    productname=[]
    productprice=[]
    name=soup.find_all("strong",{"class":"product name product-item-name"})
    for i in range(len(name)):
        productname.append(name[i].text)
        #print(productname[i])

    price=soup.find_all('div',{'class':"price-box price-final_price"})

    for i in range(len(price)):
        productprice.append(price[i].text)
        #print(productprice[i])
    for i in range(len(productname)):
        print(productname[i], productprice[i])
print('this is page 1 :')
scrape(page1)
print('this is page 2 :')
scrape(page2)
print('finished')