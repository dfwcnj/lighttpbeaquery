import os
import sys

class BEAHier():

    def __init__(self):
        self.ce = [
        "DOCUMENT_ROOT", "HTTP_COOKIE", "HTTP_HOST", "HTTP_REFERER",
        "HTTP_USER_AGENT", "HTTPS", "PATH", "QUERY_STRING", "REMOTE_ADDR",
        "REMOTE_HOST", "REMOTE_PORT", "REMOTE_USER", "REQUEST_METHOD",
        "REQUEST_URI", "SCRIPT_FILENAME", "SCRIPT_NAME", "SERVER_ADMIN",
        "SERVER_NAME", "SERVER_PORT", "SERVER_SOFTWARE",
        ]

    def beahier(self):
        bhf = '/var/www/localhost/htdocs/beahierarchy.html'
        bhj = '/var/www/localhost/wlib/beahierarchy.json'
        try:
            with open(bhf) as fp:
               htm = fp.read()
               print("Content-Type: text/html\n\n")
               print(htm)
               sys.exit()
        except Exception as e:
            import beaquery
            from beaquery import beaqueryq
            BN = beaqueryq.BEAQueryQ()

            hd = BN.hierarchy('json')
            if not os.path.exists(bhj):
                print('beahier: saving json', file=sys.stderr)
                with open(bhj, 'w') as fp:
                    fp.write(hd)

            htm = BN.hierarchyhtml(hd)
            print('beahier: saving html', file=sys.stderr)
            with open(bhf, 'w') as fp:
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


def main():

    CF = BEAHier()
    CF.beahier()

if __name__ == '__main__':
    main()

