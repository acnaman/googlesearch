from unittest import TestCase
import search as s
import lxml.html

def test_makelistfromcsv_twodata():
    csvdata = "a,b"
    madelist = s.makelistfromCSV(csvdata)
    answer = ['a','b']
    assert(madelist == answer)

def test_makelistfromcsv_threedata():
    csvdata = "a,b,c"
    madelist = s.makelistfromCSV(csvdata)
    answer = ['a','b','c']
    assert(madelist == answer)

def test_load_test1csv():
    file = 'test1.csv'
    madelist = s.loadcsv(file)
    answer = ['あいう','えお','かき','くけこ']
    assert(madelist == answer)

def test_load_test2csv():
    file = 'test2.csv'
    madelist = s.loadcsv(file)
    answer = ['abc','de','fg','hij']
    assert(madelist == answer)

def test_makeurltosearch_hogehoge():
    word = 'hogehoge'
    madeurl = s.makeurltosearch(word)
    # 参考：https://so-zou.jp/web-app/tech/search-engine/google/search/
    answer = "https://www.google.co.jp/search?q=hogehoge"
    assert(madeurl == answer)

def test_makeurltosearch_foobar():
    word = 'foobar'
    madeurl = s.makeurltosearch(word)
    # 参考：https://so-zou.jp/web-app/tech/search-engine/google/search/
    answer = "https://www.google.co.jp/search?q=foobar"
    assert(madeurl == answer)

def test_googlesearch_hogehoge():
    word = 'hogehoge'

    html = s.downloadsearchresult(word)
    root = lxml.html.fromstring(html)

    title = root.cssselect('title')[0].text
    answer = 'hogehoge - Google 検索'

    assert(title == answer)

def test_googlesearch_aiueo():
    word = 'あいうえお'

    html = s.downloadsearchresult(word)
    root = lxml.html.fromstring(html)

    title = root.cssselect('title')[0].text    
    answer = 'あいうえお - Google 検索'

    assert(title == answer)

def test_extractsearchcount_hogehoge():
    word = 'hogehoge'

    count = s.extractsearchcount(word)

    # answer = '381000'
    # assert(count == answer)
