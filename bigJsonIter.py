import json
import re

def get_space_end(level):
    return '  ' * level + '-'

def get_space_expand(level):
    return '  ' * level + '+'

def find_keys(targets, level):
    keys = iter(targets)
    for each in keys:
        if type(targets[each]) is not dict:
            print(get_space_end(level) + each)
        else:
            next_level = level + 1
            print(get_space_expand(level) + each)
            find_keys(targets[each], next_level)

def main():
    with open('items.txt', 'r', encoding='utf-8') as f:
        g_page_config = re.search(r'g_page_config = (.*?);\n', f.read())
        page_config_json = json.loads(g_page_config)
        find_keys(page_config_json, 1)

if __name__ == '__main__':
    main()
