import re
import subprocess

args = ['ps', 'aux']
res = subprocess.Popen(args, stdout=subprocess.PIPE)
output = subprocess.check_output(('grep', 'jubatus'), stdin=res.stdout)
res.wait()
stdout = output.decode('utf-8')

pss = []
for line in stdout.split('\n'):
    formatted_line = re.sub(r' +', ' ', line)
    formatted_line_list = formatted_line.split(' ')
    if '-p' in formatted_line_list:
        pss.append(formatted_line_list)
# print(pss)

pids = []
for ps in pss:
    pids.append(ps[1])
# print(pids)

for pid in pids:
    res = subprocess.run(['kill', str(pid)], stdout=subprocess.PIPE)