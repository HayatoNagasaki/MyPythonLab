import requests
import HtmlParser as par



parser=par.parser

response=requests.get("https://www.amazon.com/Microsoft-Surface-Studio-Certified-Refurbished/dp/B07FB141WR/ref=as_li_ss_tl?ref_=Oct_DLandingS_PC_83da27db_NA&smid=A19N59FKNWHX7C&linkCode=sl1&tag=asher0c-20&linkId=aa1a8df17bc2fb359fa0246a56ecbd38&language=en_US")


html = response.text

#feed = parser.feed(html)

#print(feed)
