#!/usr/bin/python
import sys
import json
import os
from regipy.registry import RegistryHive
from regipy.plugins.utils import run_relevant_plugins

#execute for Ntuser.dat
f = open('ntuser_json.txt','w')
try:
    PATH = sys.argv[1]
    reg = RegistryHive(PATH)
    result = run_relevant_plugins(reg, as_json=True)
    f.writelines(json.dumps(result))
    print("Success")
    f.close()
except:
    f.close()
    print("failed")
    os.system("DEL ntuser_json.txt")
