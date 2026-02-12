from copy_files import check_dirs
from generate_page import generate_page, generate_pages_recursive
import sys

def main():

    basepath = sys.argv[1] if sys.argv[1] else "/"
    check_dirs("./static", "./docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

main()
