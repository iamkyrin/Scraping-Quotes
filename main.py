import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []
for i in range(1, 11):

    url = f"https://quotes.toscrape.com/page/{i}"

    response = requests.get(url)


    soup = BeautifulSoup(response.text, "lxml")
    num = 0
    print(F"<-----------------PAGE {i}----------------->")
    for paragraph in soup.find_all(class_="text"):
        num += 1

        print(f"-- {num}. {paragraph.text}")
        data.append(paragraph.text)


        df = pd.DataFrame(data)
        df.to_excel(f'quotes.xlsx', index=False)
print(data)
