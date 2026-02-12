from copy_files import check_dirs
from generate_page import generate_page, generate_pages_recursive
import sys

def main():
    basepath = sys.argv[0] if sys.argv == True else "/"
    check_dirs("./static", "./docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

main()
