import HTMLParser

html = '874192139156386460916113894912741976254%2C1425600'
html1 = 'http%3A//aws-live-video.mobile.nfl.com/20_NFL_COM_LIVE/video_h12.m3u8'
html_parser = HTMLParser.HTMLParser()
txt = html_parser.unescape(html1)
print txt
