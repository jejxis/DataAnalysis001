import ast
import json

with open('errata_m1.txt', 'r') as inf:
    m1_dict = ast.literal_eval(inf.read())
    
with open('errata_m2.txt', 'r') as inf:
    m2_dict = ast.literal_eval(inf.read())
    
with open('errata_m3.txt', 'r') as inf:
    m3_dict = ast.literal_eval(inf.read())

m1_list = json.dumps(list(m1_dict.values()))
m2_list = json.dumps(list(m2_dict.values()))
m3_list = json.dumps(list(m3_dict.values()))

with open('m1pbs.txt', 'w') as outfile:
    outfile.write(m1_list)
with open('m2pbs.txt', 'w') as outfile:
    outfile.write(m2_list)
with open('m3pbs.txt', 'w') as outfile:
    outfile.write(m3_list)
