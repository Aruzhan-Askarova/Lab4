import json
print('Interface Status')
print('================================================================================')
print('DN                                              Description     Speed    MTU  ')
print('----------------------------------------------- --------------  ------  ------')
file = open("/Users/anuarermanov/Downloads/json/sample.json", 'r')
data = json.loads(file.read())
for i in data["imdata"]:
    if len(i["l1PhysIf"]["attributes"]["dn"])==42:
        print(i["l1PhysIf"]["attributes"]["dn"], "                   ", i["l1PhysIf"]["attributes"]["speed"], " ", i["l1PhysIf"]["attributes"]["mtu"])
    else:
        print(i["l1PhysIf"]["attributes"]["dn"], "                    ", i["l1PhysIf"]["attributes"]["speed"]," ", i["l1PhysIf"]["attributes"]["mtu"])