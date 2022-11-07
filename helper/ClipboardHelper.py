import pyperclip


def get_text() -> str:
    return pyperclip.paste()


def copy_text(string: str):
    pyperclip.copy(string)
