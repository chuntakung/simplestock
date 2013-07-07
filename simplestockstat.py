import os
import sys
import jinja2
import webapp2
import json
from parse_cepd import Cepd_parser


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])
    
class MainPage(webapp2.RequestHandler):

    def get(self):

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render())

class MacroPage(webapp2.RequestHandler):
    def get(self):
        #url = 'http://index.cepd.gov.tw/Result.aspx?lang=1&type=it02&p=1^1^2008,6,2013,6^^,,^SR0001,SR0007,SR0008,SR0009,^'
        #parser = Cepd_parser()
        #parser.feed(parser.fetch_url(url))
        #data = {"data": json.dumps(parser.out)}
        template = JINJA_ENVIRONMENT.get_template('macro.html')
        self.response.write(template.render())
        #self.response.write(json.dumps(jsonData))
        
class StatRequest(webapp2.RequestHandler):
    def get(self):
        datatype = self.request.get('datatype')
        datatype = (int)(datatype)
        datatype = '%(num)02d' %{"num":datatype}
        url = 'http://index.cepd.gov.tw/Result.aspx?lang=1&type=it01&p=1^1^2008,6,2013,6^^,,^SR00'+datatype+',^'
        parser = Cepd_parser()
        parser.feed(parser.fetch_url(url))
        self.response.headers['Content-Type'] = "application/json"
        self.response.write(json.dumps(parser.out))
        
                
application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/macro.html', MacroPage),
    ('/data.json', StatRequest)
], debug=True)