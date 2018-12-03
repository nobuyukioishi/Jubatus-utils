import re
import subprocess

for i in range(20):
    port_no = 9199 + i
    args = ['/opt/jubatus/bin/jubaclassifier',
            '-f', '/home/member/AOL/classifier/nonlinear.json',
            '-p', str(port_no),
            # '-m', '/home/member/AOL/classifier/model/192.168.88.137_9199_classifier_adl-main-latest.jubatus'
            '-d', '/home/member/AOL/classifier/model',
            '-g', '/home/member/AOL/jubatus-log/log4css.xml',
            '-D']
    res = subprocess.run(args, stdout=subprocess.PIPE)
    if not(res.returncode == 0):
        print("Couldn't make jubatus process at port", port_no)

args = ['ps', 'aux']
res = subprocess.Popen(args, stdout=subprocess.PIPE)
output = subprocess.check_output(('grep', 'jubatus'), stdin=res.stdout)
res.wait()
stdout = output.decode('utf-8')
print(stdout)