#!/usr/bin/python
import sys
import json
import os
from regipy.registry import RegistryHive
from regipy.plugins.utils import run_relevant_plugins

f = open('system_json.txt','w')
try:
    PATH = sys.argv[1]
    reg = RegistryHive(PATH)
    result = run_relevant_plugins(reg, as_json=True)
    f.writelines(json.dumps(result))
    f.close()
except:
    f.close()
    print("failed")
    os.system("DEL system_json.txt")