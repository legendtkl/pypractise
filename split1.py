
s = '#EXT-X-VERSION'

#item = s.split(',')[0].split(':')
item = s.split('#')
print item[1]
