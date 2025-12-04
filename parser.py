from bs4 import BeautifulSoup as bs
import requests as req
from fake_useragent import UserAgent
import argparse


class ParsNews:
    def __init__(self):
        self.headers={'user-agent':UserAgent().random}
        self.gen_link=[]
        self.completed_article_list=[]
        self.page_count=0
    
    def genLinksLst(self):
        for offset in range(0,int(self.page_count)):
            link=f'https://news.ycombinator.com/?p={offset}'
            self.gen_link.append(link)
    
    def getHTML(self):
        page = 0
        try:
            for link in self.gen_link:
                page += 1
                
                #отправляем ответ
                resp = req.get(url=link, headers=self.headers)
                resp.encoding='utf-8'
                soup=bs(resp.text,'lxml')

                #нахождени родительского элемента
                content=soup.find_all('span','titleline')

                #парсинг линков и названий
                for txt in content:
                    self.completed_article_list.append(f'{txt.a.text}:\t{txt.a['href']}')
                print(f'page:{page}, find artice:{len(self.completed_article_list)}')
        except Exception as _ex:
            print(_ex)
    
    def saveArticleIn_txt(self): #примитивный способ сохранания в файл
        with open('article_list.txt', 'w') as file:
            for news in self.completed_article_list:
                file.write(news+'\n')

    def main(self):
        #переопределяет количество страниц или оставляем как есть(0)
        parser=argparse.ArgumentParser()
        parser.add_argument('-c', '--count')
        args = parser.parse_args()

        #если мы задали определенное количество страниц
        if args.count:
            self.page_count=args.count
        
        self.genLinksLst()
        parse.getHTML()
        self.saveArticleIn_txt()

if __name__ == '__main__':
    parse = ParsNews()
    parse.main()






