from urllib import urlopen
from urllib import FancyURLopener
import json
from requests.exceptions import ConnectionError
from httplib import IncompleteRead

def formatNonAscii(text):
    text = text.replace('\n', ' ').replace('\r', '')
    return ''.join([i if ord(i) < 128 else '' for i in text])

class MyOpener(FancyURLopener):
            version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
            
def main(petitionUrl):
    offset = 0
    title = petitionUrl[:]
    baseUrl = 'https://www.change.org/api-proxy/-/tags/%s/petitions?order=mostrecent&offset=%s&limit=8'
    while(True):
        try:
            url = baseUrl % (title, offset)
            outfile = "%s.txt" % (title)
            myopener = MyOpener()
            raw = myopener.open(url)
            d = json.loads(raw.read())
            for topic in d['items']:
                write_dict = []
                write_dict.append(topic['petition']['slug'])
                open(outfile,'a').write("%s\n" % write_dict)
            if (d["last_page"] == True):
                print "done"
                break
            else:
                offset += 10
        except ConnectionError:
            print "Connection Issue"
            continue
        except IncompleteRead:
            print "IncompleteRead"
            continue
            
    return


