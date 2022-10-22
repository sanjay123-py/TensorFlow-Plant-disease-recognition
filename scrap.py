from bs4 import BeautifulSoup
import requests

class ScrapExplanation:
    def __init__(self, *args):
        if(len(args)==1):
            self.disease = args[0]
            search_query="https://www.google.com/search?q="
            self.url=search_query+"+".join(self.disease.split(' '))
            self.request_content=requests.get(self.url)
            self.bscontent=BeautifulSoup(self.request_content.text,"html.parser")
            self.div1=self.bscontent.find_all(['div'],class_='kCrYT')
            self.content=[]
            self.error=False
            for i in range(len(self.div1)):
                try:
                    str1 = self.div1[i].div.div.div.div.div.text
                    self.content.append(str1.replace("\xa0...",""))
                except:
                    pass
        else:
            self.content=["Your plant is healthy no worries ;)"]
    # def __repr__(self):
    #     return "\n".join(self.content)