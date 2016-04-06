from subprocess import Popen, PIPE

def execute(cmd):
	p = Popen(cmd, shell=True, stdout = PIPE, stderr = PIPE)
	out, err = p.communicate()
	return p.returncode, out, err

port = execute('''lsof -i:80 | grep -v grep | awk '{if($2!="PID")print $2}' | sort | uniq ''')
print port
