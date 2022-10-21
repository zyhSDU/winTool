class Pair(object):
    def __init__(self, chinese_str: str, english_str: str):
        self.chinese_str: str = chinese_str
        self.english_str: str = english_str


pair_list = [
    Pair("；", ";"),
    Pair("，", ","),
]


def change_chinese_punctuation_to_english(string: str) -> str:
    for i in pair_list:
        string = string.replace(i.chinese_str, i.english_str)
    return string.strip()


def change_english_punctuation_to_chinese(string: str) -> str:
    for i in pair_list:
        string = string.replace(i.english_str, i.chinese_str)
    return string.strip()
