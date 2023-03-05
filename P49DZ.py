from jinja2 import Environment, FileSystemLoader
strings = [    {"tag": "h1", "string":"Cтраница с домашним заданием"},
               {"tag": "p", "string": "Домашнее задание выполнено" },
               {"tag": "h3", "string": "Однажды в студеную, зимнюю пору" },
               {"tag": "p", "string": "Я из лесу вышел. И снова зашел." },
               {"tag": "p", "string": "И последняя сторка" },
               ]



file_loader=FileSystemLoader('P49DZ')
env=Environment(loader=file_loader)
tm=env.get_template('main.html')
msg=tm.render(strn=strings,title="Домашнее задание ")
print(msg)
with open("P49DZ/proba.html", "w", encoding="UTF-8") as f:
    f.write(msg)
