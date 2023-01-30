# index root directory making GITHUB markup for: https://github.com/Amorano/BTEP/wiki/_new

import os

print(os.getcwd())

root = 'emblem'
url = 'https://raw.githubusercontent.com/Amorano/BTEP/main/emblem'
body = ""

for category in os.listdir(root):
	if category.startswith('_'):
		continue
	f = f"{root}/{category}"
	if not os.path.isdir(f):
		continue

	body += f"<h1>{category.upper()}</h1>\n\n"
	for im in os.listdir(f):
		if not im.endswith('.png'):
			continue
		im = f"{f}/{im}"
		im = im.split('/')
		line = f'[<img src="{url}/{im[1]}/{im[2]}" width="128" height="128">]({url}/{im[1]}/{im[2]})\n'
		body += line

	body += "\n\n"

with open('__out.txt', 'w+') as f:
	f.write(body)
