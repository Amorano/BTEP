# index root directory making GITHUB markup for: https://github.com/Amorano/BTEP/wiki/_new

import os

def emblems():
	catcount = 1
	root = 'emblem'
	url = 'https://raw.githubusercontent.com/Amorano/BTEP/main/emblem'
	body = ""
	toc = '<table align="center"><tr><td>'

	for category in os.listdir(root):
		if category.startswith('_'):
			continue
		f = f"{root}/{category}"
		if not os.path.isdir(f):
			continue

		idx = 0
		sub = ""
		for im in os.listdir(f):
			if not im.endswith('.png'):
				continue
			im = f"{f}/{im}"
			im = im.split('/')
			sub += f'[<img src="{url}/{im[1]}/{im[2]}" width="128" height="128">]({url}/{im[1]}/{im[2]})\n'
			idx += 1

		if idx == 0:
			continue

		if (catcount % 4) == 0:
			toc += "</td><td>"
		catcount += 1

		toc += f'<a href="https://github.com/Amorano/BTEP/wiki/Emblem-Index#{category.upper()}">{category.upper()}</a><br>\n'
		body += f"<h1>{category.upper()}</h1>\n\n"
		body += sub
		body += "\n\n"

	toc += "</td></tr></table>"

	with open('__out.txt', 'w+', encoding='utf-8') as f:
		f.write(body)

	with open('__toc.txt', 'w+', encoding='utf-8') as f:
		f.write(toc)

def pilot():
	root = 'pilot'
	url = 'https://raw.githubusercontent.com/Amorano/BTEP/main/pilot'
	body = ""

	for category in os.listdir(root):
		if category.startswith('_'):
			continue
		f = f"{root}/{category}"
		if not os.path.isdir(f):
			continue

		idx = 0
		sub = ""
		for im in os.listdir(f):
			if not im.endswith('.png'):
				continue
			im = f"{f}/{im}"
			im = im.split('/')
			sub += f'[<img src="{url}/{im[1]}/{im[2]}" width="128" height="128">]({url}/{im[1]}/{im[2]})\n'
			idx += 1

		if idx == 0:
			continue

		body += f"<h1>{category.upper()}</h1>\n\n"
		body += sub
		body += "\n\n"

	with open('__pilot.txt', 'w+', encoding='utf-8') as f:
		f.write(body)

def sidebar():

	body = ""
	roots = ['pilot', 'emblem']
	for root in roots:
		body += f"{root}s\n".upper()
		for category in os.listdir(root):
			if category.startswith('_'):
				continue

			f = f"{root}/{category}"
			if not os.path.isdir(f):
				continue
			category = category.upper()
			body += f"* [{category}](https://github.com/Amorano/BTEP/wiki/{root}-{category})\n"
		body += '\n'

	with open('__sidebar.txt', 'w+', encoding='utf-8') as f:
		f.write(body)

if __name__ == "__main__":
	# pilot()
	sidebar()
