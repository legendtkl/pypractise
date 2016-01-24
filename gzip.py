import base64,zlib

f = '87146/16625925'
f = base64.b64decode(f)
f = zlib.decompress(f[4:])
print f
