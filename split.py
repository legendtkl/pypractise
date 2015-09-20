__author__ = "legendtkl"

import HTMLParser

def xml_spec_character(s):
	characters = [['&nbsp;',''],['&amp;','&'], ['&lt;', '<'],['&gt;','>'],['&quot;','"'],['&qpos;',"'"]]
	for c in characters:
		s = s.replace(c[0],c[1])
	return s

if __name__ == "__main__":
	s = "_dv=2&amp;nw=382613&amp;caid=nflmobile_live&amp;asnw=382613&amp;ssnw=382613&amp;csid=nflmobile_iphone&amp;vdur=300&amp;flag=+sltp+exvt+rema+slcb+aeti&amp;prof=382613:nfl_ios_live&amp;resp=m3u8&amp;mode=live;&amp;module=LiteSSHelper&amp;_fw_lpi=874192139156386460916113894912741976254,1425600&amp;_fw_lpu=http%3A//aws-live-video.mobile.nfl.com/20_NFL_COM_LIVE/video_h12.m3u8&amp;_fw_syncing_token=%7Bc%7D0475457eb5800050cbb"
	sections = HTMLParser.HTMLParser().unescape(s).split('&')
	for section in sections:
		p = section.split('=')
		if p[0]=='nw':
			print p[1]
