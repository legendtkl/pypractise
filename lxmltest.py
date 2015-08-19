__author__ = 'kltao'

import lxml.etree

if __name__ == "__main__":
	parse = lxml.etree.XMLParser(recover=True, encoding='utf8')
	ret = []
	ret = lxml.etree.fromstring(open("test.xml", 'r').read(), parse)
	print ret.tag
	print ret.attrib
	for child in ret:
		print child.tag, child.attrib
