import os
import sys
import glob
import uuid
import random

OUT_DIR = "./dirs/"

MD_TEMPLATE = """---
layout: page
title: Files
permalink: /{permalink}/
---

# Directory listing for /{permalink}
[**<-back**](/{parent})  
"""


USER_MD_TEMPLATE = """---
layout: page
title: {title}
permalink: /{permalink}/{title}/
---

[**<-back**](/{permalink})  
"""


def clean(directory):
	files = glob.glob(f'{directory}/*')
	for f in files:
	    os.remove(f)

def make_filename(name):
	suffix = random.choice(str(uuid.uuid4()).split('-'))
	return f"{name}{suffix}.markdown"


def make_listing(text, link, is_dir=False):
	if is_dir:
		return f"[**:file_folder: {text}/**](/{link})  \n"
	else:
		if text.endswith(".md") or text.endswith(".markdown"):
			filename = text.split('.')[0]
			return f"[**:page_facing_up: {text}**]({filename}) ([download]({text}))  \n"
		else:
			return f"[**:page_facing_up: {text}**]({text})  \n"

def get_filenames_links(directory):
	d = [ (p.split('/')[-1], p) for p in  glob.glob(f"{directory}/*")]
	return d

def markdown_to_jekyll_page(filepath):
	filepath_l = filepath.split('/')
	filename = filepath_l[-1]
	t = filename.split('.')[0]
	p = '/'.join(filepath_l[:-1])

	content = USER_MD_TEMPLATE.format(title=t, permalink=p) 
	with open(filepath, "r") as fh:
		line = fh.readline()
		content += f"{line}"
		while line:
			line = fh.readline()
			content += f"{line}"


	return content, t


def _traverse(parent, directory, save_dir):
	dir_listing = get_filenames_links(directory)
	template = MD_TEMPLATE.format(permalink=directory, parent=parent)
	dirs = []
	for name_link in dir_listing:
		name = name_link[0]
		link = name_link[1]
		
		if os.path.isdir(link):
			dirs.append(link)
		elif link.endswith(".md") or link.endswith(".markdown"):
			content, fname = markdown_to_jekyll_page(link)
			fname = make_filename(fname)

			with open(f"{save_dir}/{fname}", "w") as fh:
				fh.write(content)

		template += make_listing(name, link, os.path.isdir(link))


	filename = directory.split('/')[-1]
	filename = make_filename(filename)

	with open(f"{save_dir}/{filename}", "w") as fh:
		fh.write(template)
	
	for d in dirs:
		_traverse(directory, d, save_dir)

def traverse(parent):
	if not os.path.exists(parent):
		print(f"{parent} does not exist in the root directory.")
		exit()
	else:
		save_dir = f"{OUT_DIR}{parent}"
		if not os.path.exists(save_dir):
			os.mkdir(save_dir)
		print(save_dir)
		clean(save_dir)
		_traverse("", parent, save_dir)


if __name__ == "__main__":
	pwd = sys.argv[1]
	if pwd[-1] == '/':
		pwd = pwd[:-1]

	traverse(pwd)

