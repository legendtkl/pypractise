import copy

class Playlist():
	def __init__(self):
		self.type = ''	#master playlist or variant playlist
		self.playlist_type = ''	#EVENT / VOD
		self.uri = ''
		self.version = -1
		self.targetduration = 0
		self.media_sequence_number = 0
		self.discontinuity_sequence_number = 0
		self.variant = []
		self.segment = []
		self.band_width = 0
		self.is_live = False
		self.is_encrypted = False
		#master
		self.ext_x_media = ''
		self.ext_x_stream_inf = ''
		
		#unexpected tags
		self.unexpected_tags = []

class Segment ():
	def __init__(self):
		self.sequence_num = 0
		self.duration = ''
		self.uri = ''
		self.has_discontinuity = False
		self.discontinuity_sequence = -1

def parse_playlist(body):
	playlist = Playlist()
	media_number = 0
	discontinuity_number = 0
	
	playlist.type = 'variant'
	segment = Segment()
	body = body.split('\n')
	for line in body:
		if line == '\r\n': 
			continue
		if line.startswith('#[DEBUG]'):
			continue
		if line.startswith('#'):
			item = line.split(',')[0].split(':')
			if item[0]=='#EXT-X-MEDIA-SEQUENCE':
				playlist.media_sequence_number = item[1]
				media_number = int(item[1])
			elif item[0] == '#EXT-X-DISCONTINUITY-SEQUENCE':
				playlist.discontinuity_sequence_nuber = int(item[1])
				discontinuity_number = int(item[1])
			elif item[0] == '#EXT-X-VERSION':
				playlist.version = int(item[1])
			elif item[0] == '#EXT-X-TARGETDURATION':
				playlist.targetduration = int(item[1])
			elif item[0] == '#EXT_X_PLAYLIST_TYPE':
				playlist.playlist_type = item[1]
			elif item[0] == '#EXT_X_DISCONTINUITY':
				segment.has_discontinuity = True
				segment.discontinuity_number = discontinuity_number
				discontinuity_number += 1
			elif item[0] == '#EXTINF':
				segment.duration = item[1]

		elif line.startswith('http'):
			segment.uri = line
			segment.sequence_num = media_number
			media_number += 1
			playlist.segment.append(copy.copy(segment))

	return playlist

if __name__ == "__main__":
	body = '''
#EXTM3U
#EXT-X-VERSION:2
#EXT-X-TARGETDURATION:10
#EXT-X-MEDIA-SEQUENCE:654248
#[DEBUG]Switching from bandwidth [291484] to bandwidth [480047]
#[DEBUG]Type-B Ad Request:http://prod-freewheel.espn.go.com/ad/g/1?_dv=2&nw=87146&csid=watchespn:ios:phone:espn1&caid=17308332&vdur=100&vprn=846897&pvrn=134525&afid=49515690&sfid=801283&flag=+rema+slcb+aeti+exvt+sltp&prof=87146:watchespn_ios_hls_hs&resp=xml&mode=live;&_fw_ae=&&_fw_lpi=128406930711360723624849016599690671139,480047&
#[DEBUG]Media sequence delta:0
#[DEBUG]No CBP was used
#EXT-X-KEY:METHOD=AES-128,URI="https://broadband.espn.go.com/espn3/auth/espnnetworks/m3u8/v1/generateKey?channel=espn1&kid=/espn1-p_061915_121119143_75.key",IV=0x0000000000000000000000000009E340
#EXTINF:10,
http://ak-hls-brs-espn1.espn.go.com/hls/live/218616/p/espn1-p-400/Seg_061915_121119143_1308/segment_061915_121119143_654248.ts
#EXTINF:10,
http://ak-hls-brs-espn1.espn.go.com/hls/live/218616/p/espn1-p-400/Seg_061915_121119143_1308/segment_061915_121119143_654249.ts
#EXTINF:10,
http://ak-hls-brs-espn1.espn.go.com/hls/live/218616/p/espn1-p-400/Seg_061915_121119143_1308/segment_061915_121119143_654250.ts
#EXTINF:10,
http://ak-hls-brs-espn1.espn.go.com/hls/live/218616/p/espn1-p-400/Seg_061915_121119143_1308/segment_061915_121119143_654251.ts
#EXTINF:10,
http://ak-hls-brs-espn1.espn.go.com/hls/live/218616/p/espn1-p-400/Seg_061915_121119143_1308/segment_061915_121119143_654252.ts
#EXTINF:10,
http://ak-hls-brs-espn1.espn.go.com/hls/live/218616/p/espn1-p-400/Seg_061915_121119143_1308/segment_061915_121119143_654253.ts
#EXTINF:10,
http://ak-hls-brs-espn1.espn.go.com/hls/live/218616/p/espn1-p-400/Seg_061915_121119143_1308/segment_061915_121119143_654254.ts
#EXTINF:10,
http://ak-hls-brs-espn1.espn.go.com/hls/live/218616/p/espn1-p-400/Seg_061915_121119143_1308/segment_061915_121119143_654255.ts
#EXTINF:10,
http://ak-hls-brs-espn1.espn.go.com/hls/live/218616/p/espn1-p-400/Seg_061915_121119143_1308/segment_061915_121119143_654256.ts
#EXT-X-CUE-OUT
#EXT-X-DISCONTINUITY
#EXT-X-KEY:METHOD=NONE
#EXTINF:10,
http://prod-freewheel.espn.go.com/ad/l/1?s=a128&t=1441087970765020011&adid=11056184&reid=4275294&arid=0&auid=&n=87146%3B87146%3B82125%3B94047%3B147530%3B376521%3B379619%3B381963%3B383425%3B383426&f=66&r=87146&cn=defaultImpression&et=i&_cc=,,,,,,&tpos=&init=1&_dic=1&cr=http%3A//m1.fwmrm.net/m/1/87146/125/1851773/4275294/SEA_ad_150813_DraftKings_AnywayNFL_CASH_30/SEA_ad_150813_DraftKings_AnywayNFL_CASH_30_layer2_552000/SEA_ad_150813_DraftKings_AnywayNFL_CASH_30_layer2_552000_0.ts
#EXTINF:10,
http://m1.fwmrm.net/m/1/87146/125/1851773/4275294/SEA_ad_150813_DraftKings_AnywayNFL_CASH_30/SEA_ad_150813_DraftKings_AnywayNFL_CASH_30_layer2_552000/SEA_ad_150813_DraftKings_AnywayNFL_CASH_30_layer2_552000_1.ts
#EXTINF:10,
http://m1.fwmrm.net/m/1/87146/125/1851773/4275294/SEA_ad_150813_DraftKings_AnywayNFL_CASH_30/SEA_ad_150813_DraftKings_AnywayNFL_CASH_30_layer2_552000/SEA_ad_150813_DraftKings_AnywayNFL_CASH_30_layer2_552000_2.ts
#EXT-X-DISCONTINUITY
#EXT-X-KEY:METHOD=AES-128,URI="https://broadband.espn.go.com/espn3/auth/espnnetworks/m3u8/v1/generateKey?channel=espn1&kid=/espn1-p_061915_121119143_75.key",IV=0x0000000000000000000000000009E340
#EXTINF:10,
http://ak-hls-brs-espn1.espn.go.com/hls/live/218616/p/espn1-p-400/Seg_061915_121119143_1308/segment_061915_121119143_654257.ts
#EXTINF:7,
http://ak-hls-brs-espn1.espn.go.com/hls/live/218616/p/espn1-p-400/Seg_061915_121119143_1308/segment_061915_121119143_654258.ts
#EXT-X-CUE-IN
#EXT-X-CUE-OUT:180,caid=17308332
#[DEBUG]:#EXTM3U
#[DEBUG]:#EXT-X-VERSION:2
#[DEBUG]:#EXT-X-TARGETDURATION:10
#[DEBUG]:#EXT-X-MEDIA-SEQUENCE:654248
#[DEBUG]:#EXT-X-KEY:METHOD=AES-128,URI="https://broadband.espn.go.com/espn3/auth/espnnetworks/m3u8/v1/generateKey?channel=espn1&kid=/espn1-p_061915_121119143_75.key",IV=0x0000000000000000000000000009E340
'''
	
	playlist = parse_playlist(body)
	print len(playlist.segment)
	for seg in playlist.segment:
		print seg.sequence_num
		print seg.duration
		print seg.uri
		print '\n\n'









