#!/usr/bin/env python
import subprocess
from datetime import datetime
def main():
    ip_target = "10.0.2."
    for ip in range(0,256):
        target=ip_target+str(ip)
        action = "fping -a -C 5 -q "+target
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
    ip_list=[]
    start_time = datetime.now()
    main()
