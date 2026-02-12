def extract_title(markdown):
    markdown_lines = markdown.split("\n")
    for line in markdown_lines:
        if line.startswith("# "):
            return line[2:]
    raise Exception("Error: Markdown does not contain h1 header.")
