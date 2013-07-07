from sgmllib import SGMLParser
import urllib2



class Cepd_parser(SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        self.is_tbl = False
        self.is_tr = False
        self.is_td = False
        self.row_count = 0
        self.out = []
        
    def fetch_url(self, url):
        return urllib2.urlopen(url).read()
    
    def start_table(self, attrs):
        for element in attrs:
            if(element[0] == 'id'):
                if(element[1] == 'ctl00_ContentPlaceHolder1_TbeObject'):
                    self.is_tbl = True
                    break                
    def end_table(self):
        self.is_tbl = False
        
    def start_tr(self,attrs):
        self.is_tr = True
        if self.is_tbl:
            self.row_count = self.row_count +  1            
    def end_tr(self):
        self.is_tr = False
        
    def start_td(self,attrs):
        self.is_td = True
        
    def end_td(self):
        self.is_td = False
        
    def handle_data(self,text):
        if (self.is_tbl and self.is_tr):        
            if (self.is_td):
                try:
                    text=text.replace(',','')
                    self.out[self.row_count-1].append(text)                    
                except IndexError:
                    self.out.append([])
                    self.out[self.row_count-1].append(text)

                    
                    
            



