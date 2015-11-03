from xml.sax.saxutils import unescape
import HTMLParser

s = 'http%3A//playerdemo.freewheel.tv/hls/stream/1200k_live.m3u8'
#print HTMLParser.HTMLParser().unescape(s)
print s.replace('%3A',':')
