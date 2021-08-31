import json

#读取配置文件
with open("Config/config.json", "r") as f:
    conf_json = json.loads(f.read())
