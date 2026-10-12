```dataviewjs

const folder = "."; // "." = current folder, or e.g. "Documentation/API"

const HEADING_MARGIN = 1.2;
const HEADING_INDENTATION = 1.25;
const TITLE_SIZE = "1.8em";
const HEADING_SIZE = "1.4em";

const currentPath = dv.current().file.path;
const currentFolder = currentPath.includes("/")
    ? currentPath.substring(0, currentPath.lastIndexOf("/"))
    : "";

const targetFolder = folder === "."
    ? currentFolder
    : folder.replace(/\/+$/, "");

const currentFolderName = currentFolder
    ? currentFolder.split("/").pop()
    : "/";

const titleLabel = dv.el("div", "", {
    attr: {
        style: `font-size: ${TITLE_SIZE}; font-weight: 600; margin-top: 1em;`
    }
});

titleLabel.appendChild(
    document.createTextNode(currentFolderName)
);

// Find files in the target folder and its subfolders
const pages = dv.pages()
    .where(p => {
        const path = p.file.path;
        const parent = path.includes("/")
            ? path.substring(0, path.lastIndexOf("/"))
            : "";

        return (
            path !== currentPath &&
            (targetFolder === ""
                ? true
                : parent === targetFolder ||
                  parent.startsWith(targetFolder + "/"))
        );
    })
    .sort(
        p => p.file.path.slice(
            targetFolder ? targetFolder.length + 1 : 0
        ),
        (a, b) => a.localeCompare(b, undefined, {
            numeric: true,
            sensitivity: "base"
        })
    );

let count = 0;

for (const page of pages) {
    const cache = app.metadataCache.getCache(page.file.path);
    const headings = cache?.headings ?? [];

    if (headings.length === 0) continue;

    let relativePath = targetFolder
        ? page.file.path.slice(targetFolder.length + 1)
        : page.file.path;

    relativePath = relativePath.substring(0, relativePath.length - 3);

    const fileLabel = dv.el("div", "", {
        attr: {
            style: `font-size: ${HEADING_SIZE}; font-weight: 600; margin-top: 1em;`
        }
    });

    fileLabel.appendChild(
        document.createTextNode(relativePath)
    );

    for (const h of headings) {
        const indent =
            (Math.max(0, h.level - 1) + HEADING_MARGIN)
            * HEADING_INDENTATION;

        const line = dv.el("div", "", {
            attr: {
                style: `margin-left: ${indent}em;`
            }
        });

        // Create a real clickable link to the heading
        const link = document.createElement("a");
        link.className = "internal-link";
        link.setAttribute("data-href", page.file.path);
        link.href = page.file.path;
        link.textContent = "" + h.heading;

        line.appendChild(link);

        count++;
    }
}

if (count === 0) {
    dv.paragraph("No headings found in this folder.");
}
```
