import os
import sys
import glob

OUT_DIR = "./dirs/"

MARKDOWN_TEMPLATE = """---
layout: page
title: Files
permalink: /<<>>/
---

# Directory listing for /<<>>
[**<-back**](/>><<)  
"""

pwd = sys.argv[1]

def make_listing(text, link, is_dir=False):
	if is_dir:
		return f"[**:file_folder: {text}/**](/{link})  \n"
	else:
		return f"[**:page_facing_up: {text}**]({text})  \n"

def get_filenames_links(directory):
	d = [ (p.split('/')[-1], p) for p in  glob.glob(f"{directory}/*")]
	return d


def traverse(parent, directory):
	d = get_filenames_links(directory)
	template = MARKDOWN_TEMPLATE.replace("<<>>", directory).replace(">><<", parent)
	dirs = []
	for name_link in d:
		name = name_link[0]
		link = name_link[1]
		
		if os.path.isdir(link):
			dirs.append(link)

		template += make_listing(name, link, os.path.isdir(link))

	filename = f"{OUT_DIR}{directory.replace('/', '-')}.markdown"
	
	with open(filename, "w") as fh:
		fh.write(template)

	for d in dirs:
		traverse(directory, d)
# print(MARKDOWN_TEMPLATE.replace("<<>>", pwd))

traverse("", pwd)

