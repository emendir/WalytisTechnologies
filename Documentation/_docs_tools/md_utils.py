import os

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))


# relative to PROJECT_DIR
DOCS_DIR = ""

# path of config file markdown-link-checker
MLC_CONF = os.path.join(SCRIPT_DIR, "markdown-link-checker.conf")

os.chdir(PROJECT_DIR)


def get_markdown_files(dir: str = PROJECT_DIR) -> list[str]:
    markdown_files = []
    for folder, subfolders, filenames in os.walk(dir):
        # print(folder)
        for filename in filenames:
            if filename[-3:] == ".md":
                markdown_files.append(os.path.join(folder, filename))
    return markdown_files
