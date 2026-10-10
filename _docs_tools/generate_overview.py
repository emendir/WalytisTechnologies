#!/usr/bin/env python3
"""
Scan a documentation directory of Markdown files and generate an overview file.

The script extracts a short description from each Markdown file by reading the
first relevant italic line. It supports descriptions that appear either at the
top of the file or directly after a Markdown title. Optionally, a prefix (e.g.
"Umfang: ") can be required and/or removed from the extracted description.

The result is written to a DocsOverview.md file with links to all documents.
"""

from dataclasses import dataclass
import re
import urllib.parse
import os
from md_utils import DOCS_DIR

# --- Configuration ---
DESCRIPTION_PREFIX = "Umfang: "
REQUIRE_PREFIX = False  # If True, only descriptions with prefix are used
URL_ENCODE_LINKS = True  # whether to encode links RFC 3986, e.g. for Obsidian
PARSE_NUMBERING = True  # whether to nest folder and file name numbering

DIR_TO_SCAN = os.path.abspath(DOCS_DIR)


def extract_description(filepath: str) -> str:
    """Extract the description line from a markdown file."""
    with open(filepath, "r", encoding="utf-8") as file:
        lines = file.readlines()

    i = 0
    n = len(lines)

    # Skip initial empty lines
    while i < n and not lines[i].strip():
        i += 1

    # Skip title if present
    if i < n and lines[i].lstrip().startswith("#"):
        i += 1

    # Skip empty lines after title
    while i < n and not lines[i].strip():
        i += 1

    if i >= n:
        return ""

    line = lines[i].strip()

    # Check if italic markdown (_text_)
    if len(line) >= 2 and line.startswith("_") and line.endswith("_"):
        line = line[1:-1].strip()
    else:
        return ""

    # Handle prefix logic
    if DESCRIPTION_PREFIX:
        if line.startswith(DESCRIPTION_PREFIX):
            line = line[len(DESCRIPTION_PREFIX) :].strip()
        elif REQUIRE_PREFIX:
            return ""

    return line


NUMBERED_PREFIX_RE = re.compile(r"^(\d+(?:\.\d+)*)\.\s+(.*)$")


@dataclass
class FileItem:
    filepath: str
    doc_name: str
    description: str
    number: list[int] | None


@dataclass
class FolderItem:
    folder_path: str
    folder_name: str
    number: list[int]
    file_items: list[FileItem] | None


def apply_hierarchical_numbering(folders: list[FolderItem]) -> list[FolderItem]:
    """
    Adds hierarchical numbering based on parent folder numbering.

    Example:
    "1. Intro/2. Topic.md" -> "1.2 Topic"
    """

    def split_number_prefix(name: str):
        match = NUMBERED_PREFIX_RE.match(name)
        if match:
            return match.group(1), match.group(2)
        return None, name

    new_folders = []

    for folder_item in folders:
        # Build hierarchical prefix from folder chain
        prefix_parts = []

        parts = (
            folder_item.folder_path.strip(os.sep).split(os.sep)
            if folder_item.folder_path
            else []
        )

        for part in parts:
            number, name = split_number_prefix(part)
            if number:
                prefix_parts.append(number)
            else:  # reset counting
                prefix_parts = []

        # Construct full prefix (only from numbered parts)
        if parts:
            full_prefix = ".".join([p for p in prefix_parts if p])

        _, folder_name_cleaned = split_number_prefix(folder_item.folder_name)

        new_documents = []

        for doc in folder_item.file_items:
            number, clean_name = split_number_prefix(doc.doc_name)

            new_documents.append(
                FileItem(
                    filepath=doc.filepath,
                    description=doc.description,
                    doc_name=clean_name,
                    number=full_prefix,
                )
            )

        new_folders.append(
            FolderItem(
                folder_path=folder_item.folder_path,
                folder_name=folder_name_cleaned,
                number=full_prefix,
                file_items=new_documents,
            )
        )

    return new_folders


os.chdir(DIR_TO_SCAN)

folders = []

for folder, _, filenames in os.walk("."):
    folders_docs = []

    for filename in filenames:
        if not filename.endswith(".md"):
            continue

        filepath = os.path.join(folder, filename)
        description = extract_description(filepath)

        doc_name = filename[:-3]
        folders_docs.append(FileItem(filepath, doc_name, description, []))

    # sort by filename
    folders_docs = sorted(folders_docs, key=lambda item: item.doc_name)

    # add to list of folders
    folder_path = folder
    folders.append(
        FolderItem(
            folder_path=folder_path,
            folder_name=os.path.basename(folder_path),
            number=None,
            file_items=folders_docs,
        )
    )

# sort by folder name
folders = sorted(folders, key=lambda item: item.folder_path)

if PARSE_NUMBERING:
    folders = apply_hierarchical_numbering(folders)

with open("DocsOverview.md", "w+", encoding="utf-8") as file:
    file.write("<!-- This document is generated by generate_overview.py -->\n\n")

    for folder in folders:
        if (
            not folder.folder_path
            or not folder.file_items
            or folder.folder_name.startswith("_")
        ):
            print("Skipping:", folder_path)
            continue

        if folder.folder_name != ".":
            parts = folder.folder_path.split(os.sep)
            depth = len(parts)
            # Write only new headers
            header_prefix = "#" * depth
            if folder.number:
                header_prefix += f" {folder.number}."
            file.write(f"{header_prefix} {folder.folder_name}\n\n")

        for doc in folder.file_items:
            doc_link = doc.filepath

            if URL_ENCODE_LINKS:
                doc_link = urllib.parse.quote(doc_link)

            if doc.number:
                number_part = f"{doc.number}. "
            else:
                number_part = ""
            file.write(
                f"- [{number_part}{doc.doc_name}]({doc_link}): {doc.description}\n"
            )

        file.write("\n")
