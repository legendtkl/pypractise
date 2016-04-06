import sys, zlib, base64

if __name__ == '__main__':
	if len(sys.argv) != 2:
		sys.exit(0)
	cookie = sys.argv[1]
	origin_cookie = base64.b64decode(cookie)
	origin_cookie = zlib.decompress(origin_cookie[4:])
	print origin_cookie
