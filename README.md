# Intel-PA.github.io

## What is this?
This is a quick and dirty landing page to be used as a reference for all the documents and work generated over the course of the Intel-PA project. You can create directories in the root of this repo and their contents will be browsable on [the website](https://intel-pa.github.io/)

## Instructions

1. Clone the repo
2. Switch branches: `git checkout jekyll-site` 
3. Create a directory and place in the root directory of the repo (or modify an existing one)
4. If in a BASH environment: `./build_site.sh -d [name of directory] -p`  
   Otherwise:
   1. Run `> python dir_builder.py [name of directory]`. This will generate the necessary markdown to make your newly created directory's contents browsable. These markdown files will be stored under the `dirs` directory.
   2. Run `> git add dirs [name of directory] && git commit -m "update dir: [name of directory]" && git push origin jekyll-site`

The changes should be reflected on the live site as soon as the build passes some tests (should take a couple of minutes)
