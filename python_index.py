s = 'http://mlbads-l3c.mlb.com/ads-v4/freewheel/ad.ts?ad_id=&amp;chunk=14&amp;break=26&amp;partner=mlb&amp;content=31696747&amp;bitrate=500&amp;preset=F672336E3E2992AEA0FADF211A9BE113&amp;pat=010001&amp;pmt=043C01E100010235C60CB169&amp;es=0F0F11E2CE818000EB&amp;es=152538&amp;es=061F98&amp;es=1B0F09E2CE7F130096&amp;chunkdur=5&amp;breakdur=55'

pos = s.index('ad_id')
s1 = s[pos:].replace('&amp;', '&')
for item in s1.split('&'):
	kv = item.split('=')
	if kv[1] == '':
		print kv[0]
	print kv[0], kv[1]
