#!/usr/bin/python
import sys
import json
import os
from regipy.registry import RegistryHive
from regipy.plugins.utils import run_relevant_plugins

f = open('security_json.txt','w')
try:
    PATH = sys.argv[1]
    reg = RegistryHive(PATH)
    result = reg.get_key('').get_values(as_json=True)
    print(result)
    f.close()
except:
    f.close()
    print("failed")
    os.system("DEL security_json.txt")