import json
config = {"name":"martin","location":"shanghai"}
#load/dump use to json file
with open("jsonL.txt", 'w+') as f:
    json.dump(config,f) #overwrite the file
with open("jsonL.txt","r") as f:
    newconfig = json.load(f)
print(type(newconfig))
print(newconfig)
#loads/dumps used to string vs json object
config_str = '{"name":"jimmy","location":"USA"}'
config = json.loads(config_str)
print(config)
new_config_str = json.dumps(config)
print(type(new_config_str))