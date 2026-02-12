from copy_files import check_dirs
from generate_page import generate_page, generate_pages_recursive

def main():
    check_dirs("./static", "./public")
    generate_pages_recursive("content", "template.html", "public")

main()
