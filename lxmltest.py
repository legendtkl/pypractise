__author__ = 'kltao'

import lxml.etree

if __name__ == "__main__":
	parse = lxml.etree.XMLParser(recover=True, encoding='utf8')
	ret = []
	ret = lxml.etree.fromstring(open("0_small.xml", 'r').read(), parse)
	#print len(ret)
	print ret.tag
	print ret.attrib
	for child in ret:
	#	print child.tag, child.attrib
		for l in child:
			for k in l:
				for i in k:
					for j in i:
						for m in j:
							print m.tag, m.attrib, m.text
