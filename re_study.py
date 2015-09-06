#!python
import re

text = '<![CDATA[{"carrier":"Verizon","jsonVersion":"1.1","networkType":"wifi","buildVersion":"11.2.0","userId":"545281f5e4b0bb2ac399b6f1","zipCode":"90232","totalBytes":2035312,"timestamp":"1414721287886","platform":"ios","timeDuration":"1","freePreview":"false","tokenType":"verizon","feature":"LIVE_GAME","timeOffset":"1","featureId":"2014103000","token":"5452ac38e4b04aabf94107e2","nflAccess":"Premium"}]]>'
#p = re.findall(r'<![CDATA[feature]]>', text)
p = re.findall("\<\!\[CDATA\[(.*?)\]\]\>", text)
print p
