#!/usr/bin/python
import sys
import json
import os
from regipy.registry import RegistryHive
from regipy.plugins.utils import run_relevant_plugins

TYPE=""
PATH=""

def system():
    #execute for system.dat
    f = open('system_json.json','w')
    try:
        reg = RegistryHive(PATH)
        result = run_relevant_plugins(reg, as_json=True)
        f.writelines(json.dumps(result))
        print("success")
        f.close()
    except:
        f.close()
        print("failed")
        os.system("DEL system_json.json")

def software():
    #execute for software.dat
    f = open('software_json.json','w')
    try:
        reg = RegistryHive(PATH)
        result = run_relevant_plugins(reg, as_json=True)
        f.writelines(json.dumps(result))
        print("success")
        f.close()
    except:
        f.close()
        print("failed")
        os.system("DEL software_json.json")

def ntuser():
    #execute for ntuser.dat
    f = open('ntuser_json.json','w')
    try:
        reg = RegistryHive(PATH)
        result = run_relevant_plugins(reg, as_json=True)
        f.writelines(json.dumps(result))
        print("success")
        f.close()
    except:
        f.close()
        print("failed")
        os.system("DEL ntuser_json.json")

def main():
    global TYPE,PATH
    try:
        TYPE = sys.argv[1]
        PATH = sys.argv[2]

        if TYPE in ("SYSTEM","system"):
            system()
        elif TYPE in ("SOFTWARE","software"):
            software()
        elif TYPE in ("NTUSER","ntuser"):
            ntuser()
    except:
        print("Failed command")
        exit(0)
    

if __name__ == "__main__":
    main()
