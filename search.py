import requests
import lxml.html
import re

# CSVをカンマ区切りで分割しリスト化する
def makelistfromCSV(str_csv):
    return str_csv.split(',')

# 検索ワードCSVをファイルから読み込む
def loadcsv(filename):
    with open(filename, encoding='utf-8') as f:
        for row in f:
            newrow = row.rstrip()
            return makelistfromCSV(newrow)

# googleの検索に必要なURLを作成する
def makeurltosearch(word):
    return "https://www.google.co.jp/search?q=" + word

def downloadsearchresult(word):
    session = requests.Session()
    response = session.get(makeurltosearch(word))
    
    response.encoding = 'Shift_JIS'
    return response.text.encode('utf-8')

def extractsearchcount(word):
    html = downloadsearchresult(word)
    root = lxml.html.fromstring(html)
    resultstats = root.cssselect('div#resultStats')[0].text


    # 「約 5,590,000 件 （0.41 秒）」のようなデータが所得されるので不要部分を消す
    pattern = r'[,\d]{0,} 件'
    count_ken = re.search(pattern, resultstats).group()

    return re.sub('[\, 件]', '', count_ken)


def main(filename):
    searchlist = loadcsv(filename)
    for item in searchlist:
        count = extractsearchcount(item)
        print(item + ':' + str(count))

if __name__ == '__main__':
    main("test1.csv")