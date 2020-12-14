#!/usr/bin/python
import sys
import json
import os
from regipy.registry import RegistryHive
from regipy.plugins.utils import run_relevant_plugins

f = open('software_json.txt','w')
try:
    PATH = sys.argv[1]
    reg = RegistryHive(PATH)
    for entry in reg.recurse_subkeys(as_json=True):
        print(entry)
    f.close()
except:
    f.close()
    print("failed")
    os.system("DEL software_json.txt")