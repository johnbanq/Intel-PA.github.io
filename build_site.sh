#!/bin/bash

publish="false"
directory=""

function print_help(){
	printf "USAGE: ./build_site -d <name> [OPTION]\nOPTIONS:\n-d directory to be updated (required)\n-p push changes in the named directory to the jekyll-site branch of the git repo\n"
}

while getopts "pd:" flag; do
	case "${flag}" in
		p) publish="true" ;;
		d) directory="${OPTARG}" ;;
		*) exit 1 ;;
	esac 
done

if [ -z $directory ]; then
	echo "Directory name cannot be empty!"
	print_help
	exit 1
fi



python3 dir_builder.py $directory

if $publish; then
	echo "Pushing changes made to $directory to git:"
	git add dirs $directory && git commit -m "update dir: $directory" && git push origin jekyll-site
fi
