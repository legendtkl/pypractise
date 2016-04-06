import mockserver, subprocess

#threading.Thread.join(th)
def start_mockserver(base_dir):
	subprocess.Popen("/usr/bin/python mockserver.py %s" % base_dir, shell = True)

def stop_mockserver():
	mockserver.stop_mockserver()
