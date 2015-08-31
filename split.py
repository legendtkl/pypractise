__author__ = "legendtkl"

s = "_hls_ph=&quot;UAAAAHicFcnBDQAxCAOwWe7PSQTSQPZfrOrPkncIF9o46hWVhoBe06iXozoMbuYEx/ZzOX6EGgHWUearcXwXlHsQFg==&quot;;domain=.fwmrm.net;path=/;"
t = s.replace('&quot;', '"')
print t
items = t.split(';')

for item in items:
	print item.split('=', 1)
