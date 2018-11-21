#!/usr/bin/env python
import subprocess
import sys
import ipaddress
from datetime import datetime
def main(ip_target,cdir):
    if len(cdir)<1:
        cdir="/24"
    ip_range=str(ip_target)+cdir
    #net = ipaddress.ip_network(ip_range)
    net = list(ipaddress.ip_network(ip_range,False).hosts())
    for ip in net:
        action = "fping -a -C 5 -q "+str(ip)
        try:
            results = subprocess.check_output(action,stderr=subprocess.STDOUT,shell=True)
            results_split = results.split(b":")
            ip=str(results_split[0].decode('UTF-8').strip())
            time=str(results_split[1].decode('UTF-8').strip())
            ip_list.append(ip)
            response = "Host: "+ip + " is detected online. Response time(s) were: " + time
            print(response)
        except subprocess.CalledProcessError as e:
            error = e.output
    print("The following hosts were found to be online and responding to ping requests:")
    print("Detected Hosts:")
    print("==============\n")
    for ip in ip_list:
        print(ip)
    time_elapsed = datetime.now() -start_time
    print('Total time to scan took: (hh:mm:ss.ms) {}'.format(time_elapsed))

if __name__=='__main__':
    if len(sys.argv) < 2:
        print("")
        print("Usage: python pysweep.py <ip> /<CDIR>")
        print("Example: python reconscan.py 192.168.1.101 /27")
        print("")
        print("############################################################")
        pass
        sys.exit()

    # Setting ip targets
    targets = sys.argv
    targets.pop(0)
    target = targets[0]
    ip_list=[]
    start_time = datetime.now()
    if len(targets) > 1:
        cdir = targets[1]
        main(target,cdir)
    else:
        main(target,"/24")
