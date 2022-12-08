import argparse
import os
import time

MIN_MTU = 1
MAX_MTU = 1000000

def Check(host, mtu, cnt):
    return os.system(f'ping -c {cnt} -M do -s {mtu} {host} -W 2 >/dev/null 2>&1') == 0

def Find_Mtu(host, v, cnt):

    l = MIN_MTU
    r = MAX_MTU

    while r - l > 1:
        mtu = (r + l) // 2
        if Check(host, mtu, cnt):
            if v:
                print(f"SUCCESS, current MTU = {mtu}", f"Current boards is [{l}, {r}]")
            l = mtu
        else:
            if v:
                print(f"FAILED, current MTU = {mtu}", f"Current boards is [{l}, {r}]")
            r = mtu
        # anti ddos timer
        time.sleep(0.5)

    return l


parser = argparse.ArgumentParser()


parser.add_argument('--host', help='hosts for which to determine the optimal MTU')
parser.add_argument('-verbose', default=1, help='detailed output mode')
parser.add_argument('--c', default=1, help='cnt packages')

args = parser.parse_args()

host = args.host
verbose = args.verbose
cnt = args.c

if not cnt.isnumeric():
    print("Cnt is not number")
    exit(1)
else:
    cnt = int(cnt)

if not Check(host, MIN_MTU, cnt):
    print(f"Unavailable or invalid host: {host}")
    exit(1)

print(f"MTU = {Find_Mtu(host,verbose, cnt)}")
