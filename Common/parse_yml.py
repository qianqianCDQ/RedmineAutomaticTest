import yaml

# 解析yaml文件
def parse_yml(file, section, key):
    with open(file, 'r', encoding="utf8") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data[section][key]


if __name__ == "__main__":
    value = parse_yml("my_yaml_4.yml", "websites", "URL")
    print(value)