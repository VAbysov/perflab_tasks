import json
import sys


def get_args(raw_path_1, raw_path_2):
    path_1 = raw_path_1.replace('\\', '/').replace('"',"")
    path_2 = raw_path_2.replace('\\', '/').replace('"',"")
    with open(path_1) as f_1:
        t = json.load(f_1)
    with open(path_2) as f_2:
        v = json.load(f_2)  
    return t, v
    

def val(t, v):
    if isinstance(t, dict):
        for key, value in t.items():
            if isinstance(value, dict):
                val(value, v)
            elif isinstance(value, list):
                val(value, v)
            if key == "id":
                if "value" in t:
                    for d in v["values"]:
                        if d["id"] == t[key]:
                            t["value"] = d["value"]
                            continue
    elif isinstance(t, list):
        for sub_t in t:
            val(sub_t, v)


def report(rep):
    with open('report.json', 'w', encoding='utf-8') as f:
        json.dump(rep, f, ensure_ascii=False, indent=4)


raw_path_1 = sys.argv[1]
raw_path_2 = sys.argv[2]
args = get_args(raw_path_1, raw_path_2)
rep = args[1]

val(args[0], args[1])
report(rep)

