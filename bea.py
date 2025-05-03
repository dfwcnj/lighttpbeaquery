import datetime
import os
import sys
import types
import json

from urllib.parse import parse_qs

class BEAdata():

    def __init__(self):

        ### docker jspath
        self.jspath = '/var/www/localhost/wlib/beahierarchy.json'
        ### testing jspath
        #self.jspath = '../../projects/beaquery/src/beaquery/beahierarchy.json'

        from beaquery import beaqueryq
        self.BQ = beaqueryq.BEAQueryQ()

        self.forselmap = {
            'NIPA'                    : self.beanipasel,
            'NIUnderlyingDetail'      : self.beanipasel,
            'MNE'                     : self.beasel,
            'FixedAssets'             : self.beanipasel,
            'ITA'                     : self.beasel,
            'IIP'                     : self.beasel,
            'InputOutput'             : self.beasel,
            'IntlServTrade'           : self.beasel,
            'IntlServSTA'             : self.beasel,
            'GDPbyIndustry'           : self.beasel,
            'Regional'                : self.beasel,
            'UnderlyingGDPbyIndustry' : self.beasel,
        }
        self.getdatamap = {
            'NIPA' : self.getnipadata,
            'NIUnderlyingDetail' : self.getniunderlyingdetaildata,
            'MNE' : self.getmnedata,
            'FixedAssets' : self.getfixedassetsdata,
            'ITA' : self.getitadata,
            'IIP' : self.getiipdata,
            'InputOutput' : self.getinputoutputdata,
            'IntlServTrade' : self.getintlservtradedata,
            'IntlServSTA' : self.getintlservstadata,
            'GDPbyIndustry' : self.getgdpbyindustrydata,
            'Regional' : self.getregionaldata,
            'UnderlyingGDPbyIndustry' : self.getunderlyinggdpbyindustrydata,
        }

    # dictionary to namespace
    def d2ns(self, qsd):
        """ d2ns(qsd)
        qsd - python dictionary
        convert dictionary to types.SimpleNamespace
        """
        args = types.SimpleNamespace()
        for k in qsd.keys():
            args.__dict__[k] = qsd[k][0]
        # for beaqueryq plot
        for k in ['splitkey','xkey','ykey','unitskey']:
            args.__dict__[k] = None
        return args

    def loadbds(self):
        """ loadbds
        load json representing the BEA data hierarchy
        """
        with open(self.jspath) as fp:
            bds = json.load(fp)
            return bds

    #
    # get the BEA data
    #
    def getbeadata(self, bds, dsn, args):
        if dsn in list(self.getdatamap.keys()):
            data = self.getdatamap[dsn](args)
            if data == None:
                self.beadatasetpage(bds, 'no data for %s' % dsn)
            return data
        else:
            print('no get data function for %s' % dsn, file=sys.stderr)
            sys.exit()

    def getnipadata(self, args):
        data = self.BQ.getNIPAdata(args)
        return data

    def getniunderlyingdetaildata(self, args):
        data = self.BQ.getNIUnderlyingDetaildata(args)
        return data

    def getmnedata(self, args):
        data = self.BQ.getMNEdata(args)
        return data

    def getfixedassetsdata(self, args):
        data = self.BQ.getFixedAssetsdata(args)
        return data

    def getitadata(self, args):
        data = self.BQ.getITAdata(args)
        return data

    def getiipdata(self, args):
        data = self.BQ.getIIPdata(args)
        return data

    def getinputoutputdata(self, args):
        data = self.BQ.getInputOutputdata(args)
        return data

    def getintlservtradedata(self, args):
        data = self.BQ.getIntlServTradedata(args)
        return data

    def getintlservstadata(self, args):
        data = self.BQ.getIntlServSTAdata(args)
        return data

    def getgdpbyindustrydata(self, args):
        data = self.BQ.getGDPbyIndustrydata(args)
        return data

    def getregionaldata(self, args):
        data = self.BQ.getRegionaldata(args)
        return data

    def getunderlyinggdpbyindustrydata(self, args):
        data = self.BQ.getUnderlyingGDPbyIndustrydata(args)
        return data

    #
    # generate selects for forms
    #
    def beanipasel(self, bds, dsn):
        htmla = []
        htmla.append('<nobr>Dataset </nobr>')
        htmla.append('<input type="text" name="DatasetName" value="%s" readonly><br>' % (dsn))
        for i in range(1, len(bds[dsn]['Parameter'])):
            pn = bds[dsn]['Parameter'][i][0]
            pr = bds[dsn]['Parameter'][i][3]
            mv = bds[dsn]['Parameter'][i][5]
            av = bds[dsn]['Parameter'][i][6]

            if pn == 'TableID': # same as TableName
                continue

            if pn == 'Year': # choices too complicated for a select
                cmt = 'comma separated list, or X for all'
                htmla.append('<label>%s %s' % (pn, cmt))
                htmla.append('<input type="text" name="Year"><br>')
                htmla.append('</label>')
                continue

            htmla.append('<label for "%s">%s:</label>' % (pn,pn))
            if pr == '1' and mv == '1':
                htmla.append('<select name="%s" id="%s" required multiple><br>' % (pn,pn))
            elif mv == '1':
                htmla.append('<select name="%s" id="%s" multiple><br>' % (pn,pn))
            else:
                htmla.append('<select name="%s" id="%s"><br>' % (pn,pn))

            if av != '':
                avs = 'AllValue'
                htmla.append('<option value="%s" label="%s">%s</option>' % (av,avs,avs))
            if pn in bds[dsn]['ParameterValue']:
                for i in range(1, len(bds[dsn]['ParameterValue'][pn])):
                    pv = bds[dsn]['ParameterValue'][pn][i]
                    if pn == 'ShowMillions' and pv[0] == 'N':
                        htmla.append('<option value="%s" label="%s" selected="selected" >%s</option>' % (pv[0], pv[1],pv[1]))
                    else:
                        htmla.append('<option value="%s" label="%s">%s</option>' % \
                                 (pv[0], pv[1], pv[1]))
            else:
                print(bds[dsn]['Parameter'][i])
                sys.exit()
            htmla.append('</select><br>')
        return htmla

    def beasel(self, bds, dsn):
        htmla = []
        htmla.append('<nobr>Dataset </nobr>')
        htmla.append('<input type="text" name="DatasetName" value="%s" readonly><br>' % (dsn))
        for i in range(1, len(bds[dsn]['Parameter'])):
            pn = bds[dsn]['Parameter'][i][0]
            pr = bds[dsn]['Parameter'][i][3]
            mv=''
            av=''
            if len(bds[dsn]['Parameter'][i]) == 7:
                mv = bds[dsn]['Parameter'][i][-2]
                av = bds[dsn]['Parameter'][i][-1]
            elif len(bds[dsn]['Parameter'][i]) <= 6:
                mv = bds[dsn]['Parameter'][i][-1]

            htmla.append('<label for "%s">%s:</label>' % (pn,pn))

            if pr == '1' and mv == '1':
                htmla.append('<select name="%s" id="%s" required multiple><br>' % (pn,pn))
            elif mv == '1':
                htmla.append('<select name="%s" id="%s" multiple><br>' % (pn,pn))
            else:
                htmla.append('<select name="%s" id="%s"><br>' % (pn,pn))

            if av != '':
                avs = 'AllValue'
                htmla.append('<option value="%s" label="%s">%s</option>' % (av,avs,avs))
            if pn in bds[dsn]['ParameterValue']:
                for i in range(1, len(bds[dsn]['ParameterValue'][pn])):
                    pv = bds[dsn]['ParameterValue'][pn][i]
                    if pn == 'ShowMillions' and pv[0] == 'N':
                        htmla.append('<option value="%s" label="%s" selected="selected" >%s</option>' % (pv[0], pv[1], pv[1]))
                    else:
                        htmla.append('<option value="%s" label="%s">%s</option>' % \
                                 (pv[0], pv[1], pv[1]))
            else:
                print(bds[dsn]['Parameter'][i])
                sys.exit()
            htmla.append('</select><br>')
        return htmla

    #
    # bea data form for a dataset
    #
    # Parameter type []
    # ParameterValue type {}
    def beadataform(self, bds, dsn):
        htmla=[]
        htmla.append('<div class="beadata">')
        htmla.append('<form action="bea.py" method="GET" target="_blank">')

        # per dataset form elements
        if dsn in self.forselmap:
            sel = self.forselmap[dsn](bds, dsn)
            htmla.extend(sel)
        else:
            print('dsn %s not implemented', file=sys.stderr)
            sys.exit()

        htmla.append('</select>')

        htmla.append('<label for "format">format:</label>')
        htmla.append('<select name="format">')
        for i in ['HTML', 'CSV', 'CSVZipFile']:
            htmla.append('<option value="%s" >%s</option>' % (i,i))

        htmla.append('<input type="submit" value="Submit">')
        htmla.append('</form')
        htmla.append('</div>')
        return htmla

    def beadatapage(self, bds, qs):
        qsd = parse_qs(qs)
        dsn = qsd['DatasetName'][0]
        htmla=[]
        htmla.append('<html><body>')

        htmla.extend(self.beadataform(bds, dsn))

        htmla.append('<footer>BEA forbids >3 ALL parameters</footer>')
        htmla.append('<footer><a href="beahier.py" target="_blank">BEA data structure</a></footer>')
        htmla.append('</body></html>')
        return htmla

    def beadatasetform(self, bds):
        bdsa = bds['Datasets']
        htmla=[]
        htmla.append('<div class="dataset">')
        htmla.append('<form action="bea.py" id="bdsf" method="GET">')

        htmla.append('<label for "dataset">BEA Dataset:</label>')
        htmla.append('<select name="DatasetName">')
        for i in range(1, len(bdsa)):
            dsv = bdsa[i]
            if dsv[0] == 'APIDatasetMetaData':
                continue
            htmla.append('<option value="%s" >%s</option>' % (dsv[0], dsv[1]))
        htmla.append('</select>')

        htmla.append('<input type="submit" value="Submit">')
        htmla.append('</select>')

        htmla.append('</form')
        htmla.append('</div>')
        return htmla

    def beadatasetpage(self, bds, msg):
        htmla=[]
        htmla.append('<html><body>')

        htmla.extend(self.beadatasetform(bds))

        htmla.append('<p>%s</p>' % msg)
        htmla.append('<footer>BEA forbids >3 ALL parameters</footer>')
        htmla.append('<footer><a href="beahier.py" target="_blank">BEA data structure</a></footer>')
        htmla.append('</body></html>')
        return htmla

    def csvzipfilename(self, qsd):
        dn = qsd['DatasetName'][0]
        now=datetime.datetime.now()
        did=''
        if 'TableName' in qsd.keys():
            did=qsd['TableName'][0]
        elif 'TableID' in qsd.keys():
            did=qsd['TableID'][0]
        elif 'SeriesID' in qsd.keys():
            did=qsd['SeriesID'][0]
        elif 'Indicator' in qsd.keys():
            did=qsd['Indicator'][0]
        elif 'TypeOfInvestment' in qsd.keys():
            did=qsd['TypeOfInvestment'][0]
        elif 'TypeOfService' in qsd.keys():
            did=qsd['TypeOfService'][0]
        elif 'Channel' in qsd.keys():
            did=qsd['Channel'][0]

        ymd='%d%d%d' % (now.year,now.month,now.day)
        fn='%s%s%s.zip' % (dn,did,ymd)
        return fn

    def csvfilename(self, qsd):
        dn = qsd['DatasetName'][0]
        now=datetime.datetime.now()
        did=''
        if 'TableName' in qsd.keys():
            did=qsd['TableName'][0]
        elif 'TableID' in qsd.keys():
            did=qsd['TableID'][0]
        elif 'SeriesID' in qsd.keys():
            did=qsd['SeriesID'][0]
        elif 'Indicator' in qsd.keys():
            did=qsd['Indicator'][0]
        elif 'TypeOfInvestment' in qsd.keys():
            did=qsd['TypeOfInvestment'][0]
        elif 'TypeOfService' in qsd.keys():
            did=qsd['TypeOfService'][0]
        elif 'Channel' in qsd.keys():
            did=qsd['Channel'][0]

        ymd='%d%d%d' % (now.year,now.month,now.day)
        fn='%s%s%s.csv' % (dn,did,ymd)
        return fn

    def beahome(self, bds):

        if bds == None:
            bds = self.loadbds()
        qs=''
        msg = ''
        if 'QUERY_STRING' in os.environ:
            qs=os.environ['QUERY_STRING']
        if qs == '':
            dsp = self.beadatasetpage(bds, msg)
            print("Content-Type: text/html\n\n")
            print('\n'.join(dsp))
        else:
            qsd = parse_qs(qs)
            # print a page to chose a dataset
            if len(qsd.keys()) == 1:
                dp = self.beadatapage(bds, qs)
                print("Content-Type: text/html\n\n")
                print('\n'.join(dp))
            elif len(qsd.keys()) == 2:
                print('beahome: should not happen', file=sys.stderr)
                sys.exit()
            else:
                # we supposedly have enough parameters to retrieve data
                args = self.d2ns(qsd) # beaquery wants types.SimpleNamespace
                data = self.getbeadata(bds, args.DatasetName, args)
                if type(data) == type([]):
                    if len(data) == 1:
                        data=data[0]
                    else:
                        print(data, file=sys.stderr)
                        data=None
                if data==None:
                    dp=self.beadatasetpage(bds, 'no data')
                    print("Content-Type: text/html\n\n")
                    print('\n'.join(dp))
                elif 'Error' in data.keys():
                   msg=data['Error']
                   dsp = self.beadatasetpage(bds, msg)
                   print("Content-Type: text/html\n\n")
                   print('\n'.join(dsp))
                elif 'Data' not in data.keys():
                   msg=data
                   dsp = self.beadatasetpage(bds, msg)
                   print("Content-Type: text/html\n\n")
                   print('\n'.join(dsp))
                else:
                    if 'format' in qsd:
                        if qsd['format'][0] == 'CSV':
                            fn = self.csvfilename(qsd)

                            print('Content-Type: text/csv')
                            print('Content-Disposition: attachment;filename=%s\n\n' % (fn))
                            self.BQ.print2csv(data)
                        if qsd['format'][0] == 'CSVZipFile':
                            fn = self.csvzipfilename(qsd)
                            qsd['csvzipfn'] = ['/tmp/BEA/%s' % (fn)]
                            args = self.d2ns(qsd)

                            zfn = self.BQ.d2csvzipfile(data, args)

                            ct=bytes('Content-Type: application/octet-stream\n', 'utf-8')
                            #cda=bytes('Content-Disposition: attachment;\n',
                            #          'utf-8')
                            cdf=bytes('Content-Disposition: filename="%s";\n\n' % (fn), 'utf-8')
                            print(ct, file=sys.stderr)
                            #print(cda, file=sys.stderr)
                            print(cdf, file=sys.stderr)

                            with open(zfn, 'rb') as fzp:
                                sys.stdout.buffer.write(ct)
                                #sys.stdout.buffer.write(cda)
                                sys.stdout.buffer.write(cdf)
                                sys.stdout.buffer.write(fzp.read())
                        elif qsd['format'][0] == 'HTML':
                            html = self.BQ.d2html(data, args)
                            print("Content-Type: text/html\n\n")
                            print(html)
                        else:
                            print(data)

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

    #qs = 'DatasetName=MNE'
    #os.environ['QUERY_STRING'] = qs
    CF = BEAdata()
    bds = CF.loadbds()
    CF.beahome(bds)

if __name__ == '__main__':
    main()


