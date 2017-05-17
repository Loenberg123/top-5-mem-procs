#!/usr/bin/python
import subprocess

try:
	procs=subprocess.check_output("ps aux | awk '{print $2, $4, $11}' | sort -k2rn | head -n 5",
					stderr=subprocess.STDOUT, universal_newlines=True, shell=True)
except subprocess.CalledProcessError:
	procs=None

pid0=procs.split()[0]
pid1=procs.split()[3]
pid2=procs.split()[6]
pid3=procs.split()[9]
pid4=procs.split()[12]
pids=(pid0,pid1,pid2,pid3,pid4)

mem0=procs.split()[1]
mem1=procs.split()[4]
mem2=procs.split()[7]
mem3=procs.split()[10]
mem4=procs.split()[13]
mems=(mem0,mem1,mem2,mem3,mem4)

cmd0=procs.split()[2]
cmd1=procs.split()[5]
cmd2=procs.split()[8]
cmd3=procs.split()[11]
cmd4=procs.split()[14]
cmds=(cmd0,cmd1,cmd2,cmd3,cmd4)

print 'topMemProcs,top=1 pid='+pids[0]+',mem_perc='+mems[0]+',command="'+cmds[0]+'"\n'
