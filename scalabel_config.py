import re
import json

# http://localhost:8686 指向 local-data 文件夹
URL_UNIVERSAL = "http://localhost:8686/items/bdd100k/images/100k/val/"

input_path = "E:\\scalabel\\local-data\\items\\bdd100k\\labels\\drivable\\polygons\\drivable_val.json"
output_path = "E:\\scalabel\\local-data\\items\\bdd100k\\labels\\drivable\\polygons\\drivable_val_new.json"

# 车道线标注的配置参数
lane_config = {
    "attributes": [
        {
            "name": "laneDirection",
            "type": "list",
            "values": ["vertical", "parallel", "background"]
        },
        {
            "name": "laneStyle",
            "type": "list",
            "values": ["solid", "dashed", "background"]
        },
        {
            "name": "laneTypes",
            "type": "list",
            "values": ["road curb", "crosswalk", "double white", "double yellow", "double other color", "single white",
                       "single yellow", "single other color", "background"]
        }
    ],
    "categories": [
        {
            "name": "road curb"
        },
        {
            "name": "crosswalk"
        },
        {
            "name": "double white"
        },
        {
            "name": "double yellow"
        },
        {
            "name": "double other color"
        },
        {
            "name": "single white"
        },
        {
            "name": "single yellow"
        },
        {
            "name": "single other color"
        },
        {
            "name": "background"
        }
    ]
}

# 可行驶区域标注的配置参数
drivable_config = {
    "attributes": [
        {
            "name": "areaType",
            "type": "list",
            "values": ["direct", "alternative"]
        }
    ],
    "categories": [
        {
            "name": "direct"
        },
        {
            "name": "alternative"
        }
    ]
}


def get_full_json(file_path, output_file, config):
    new_contents = {}
    frames = []
    with open(file_path, "r") as f:
        content = f.read()
        contents = json.loads(content)
        for content in contents:
            url = URL_UNIVERSAL + content["name"]
            content["url"] = url
            frames.append(content)

    new_contents['frames'] = frames                     # 写入各帧标注
    new_contents['config'] = config                     # 写入配置参数
    new_contents = json.dumps(new_contents, indent=2)   # 写入json，换行

    with open(output_file, "w") as f:
        f.write(new_contents)


if __name__ == '__main__':
    get_full_json(input_path, output_path, drivable_config)
