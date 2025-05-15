import os
import sys
import json

import beaquery
from beaquery import beaqueryq

class BEAHier():

    def __init__(self):
        self.ce = [
        "DOCUMENT_ROOT", "HTTP_COOKIE", "HTTP_HOST", "HTTP_REFERER",
        "HTTP_USER_AGENT", "HTTPS", "PATH", "QUERY_STRING", "REMOTE_ADDR",
        "REMOTE_HOST", "REMOTE_PORT", "REMOTE_USER", "REQUEST_METHOD",
        "REQUEST_URI", "SCRIPT_FILENAME", "SCRIPT_NAME", "SERVER_ADMIN",
        "SERVER_NAME", "SERVER_PORT", "SERVER_SOFTWARE",
        ]
        self.bhf = '/var/www/localhost/htdocs/beahierarchy.html'
        self.bhj = '/var/www/localhost/wlib/beahierarchy.json'
        self.BN = beaqueryq.BEAQueryQ()
        self.cfn = 'beahier.py'

    def renewform(self):
        htmla=[]
        htmla.append('<html><body>')
        htmla.append('<form action="%s" method="GET" target="_blank">' % (self.cfn))

        htmla.append('<label for "action">action:</label>')
        htmla.append('<select name="action">')
        for i in ['ShoworUpdate', 'Show', 'Update']:
            htmla.append('<option value="%s" >%s</option>' % (i,i))

        htmla.append('<input type="submit" value="Submit">')
        htmla.append('</form>')
        htmla.append('<footer>')
        htmla.append('Show can take a while the first time it is invoked')
        htmla.append('</footer>')
        htmla.append('<footer>')
        htmla.append('Update will always take a while')
        htmla.append('</footer>')
        htmla.append('</body></html>')
        return htmla

    def updatehier(self):

        hd = self.BN.hierarchy('json')
        js = json.JSONEncoder().encode(hd)
        nfn=self.bhj.replace('.json', '.txt')
        with open(nfn, 'w') as fp:
            fp.write(js)
            print('updatehier: updating json', file=sys.stderr)
            os.replace(nfn, self.bhj)

        htm = self.BN.hierarchyhtml(hd)
        nfn=self.bhf.replace('.html', '.txt')
        with open(nfn, 'w') as fp:
            fp.write(htm)
            print('updatehier: updating html', file=sys.stderr)
            os.replace(nfn, self.bhf)

        print("Content-Type: text/html\n\n")
        print(htm)

    def beahier(self):
        if os.path.exists(self.bhf):
            with open(self.bhf) as fp:
               htm = fp.read()
               print("Content-Type: text/html\n\n")
               print(htm)
               sys.exit()
        else:
            hd = self.BN.hierarchy('json')
            js = json.JSONEncoder().encode(hd)
            if not os.path.exists(self.bhj):
                print('beahier: saving json', file=sys.stderr)
                with open(self.bhj, 'w') as fp:
                    fp.write(js)

            htm = self.BN.hierarchyhtml(hd)
            print('beahier: saving html', file=sys.stderr)
            with open(self.bhf, 'w') as fp:
                fp.write(htm)

            print("Content-Type: text/html\n\n")
            print(htm)

        # print("Content-Type: text/html\n\n")


    def cgienv(self):
        # print("Content-Type: text/html\n\n")
        print('<html><body>')
        for v in self.ce:
            if v in os.environ:
                print('%s %s<br>' % (v, os.environ[v]) )
            else:
                print('%s<br>' % (v))
        print('</body></html>')

    def beahierform(self):
         #print("Content-Type: text/html\n\n")
         htmla=self.renewform()
         print(''.join(htmla))

def main():

    CF = BEAHier()
    # CF.updatehier() # for debugging


    if 'QUERY_STRING' in os.environ:
        qs=''
        if len(os.environ['QUERY_STRING']) > 0 :
            qs=os.environ['QUERY_STRING']
            print('%s' % (qs), file=sys.stderr)
            if qs == 'action=Update':
                CF.updatehier()
            elif qs == 'action=Show':
                CF.beahier()
            else:
                CF.beahierform()
        else:
            print('truncated QUERY_STRING', file=sys.stderr)
            CF.beahierform()
    else:
        print('no QUERY_STRING', file=sys.stderr)
        CF.beahierform()

if __name__ == '__main__':
    main()

