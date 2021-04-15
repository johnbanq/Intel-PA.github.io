import os
import sys
import glob

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

pwd = sys.argv[1]

def clean():
	files = glob.glob(f'{OUT_DIR}*')
	for f in files:
	    os.remove(f)



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


def traverse(parent, directory):
	d = get_filenames_links(directory)
	template = MD_TEMPLATE.format(permalink=directory, parent=parent)
	dirs = []
	for name_link in d:
		name = name_link[0]
		link = name_link[1]
		
		if os.path.isdir(link):
			dirs.append(link)
		elif link.endswith(".md") or link.endswith(".markdown"):
			content, fname = markdown_to_jekyll_page(link)

			with open(f"{OUT_DIR}{fname}.markdown", "w") as fh:
				fh.write(content)

		template += make_listing(name, link, os.path.isdir(link))

	filename = f"{OUT_DIR}{directory.replace('/', '-')}.markdown"
	
	with open(filename, "w") as fh:
		fh.write(template)

	for d in dirs:
		traverse(directory, d)
# print(MARKDOWN_TEMPLATE.replace("<<>>", pwd))



clean()
traverse("", pwd)

# print(markdown_to_jekyll_page("./static/kavi/progress_reports/kavi_31_03_2021_progress_report.md"))

