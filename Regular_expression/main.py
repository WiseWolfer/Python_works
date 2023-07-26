import re

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

txt = "Мама", "авТо", "гриБ", 'Яблоко', 'яБлоко', 'ябЛоко', 'яблОко', 'яблоКо', 'яблокО'

for x in txt:
    c = re.findall(r"(^[а-я]*[А-Я][а-я]*)$", x)
    print(c)
