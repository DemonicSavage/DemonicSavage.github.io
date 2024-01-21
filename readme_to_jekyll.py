import requests

REPOS = ["demonicsavage/mikan", "demonicsavage/dsbench"]


def get_github_readme(repo):
    """Get the readme from a GitHub repo."""
    url = "https://raw.githubusercontent.com/{}/master/README.md".format(repo)
    headers = {"Cache-Control": "no-cache"}
    r = requests.get(url, headers=headers)
    if r.text.startswith("404: Not Found"):
        url = "https://raw.githubusercontent.com/{}/main/README.md".format(repo)
        r = requests.get(url, headers=headers)
    return r.text


def get_title_text(content):
    """Get the title text from the content."""
    title = content.splitlines()[0]
    if title.startswith("# "):
        title = title[2:]
    return title


def remove_title_from_readme(content):
    """Remove the title from the content and return the modified content."""
    modified_content = "\n".join(content.splitlines()[1:])
    return modified_content


def add_front_matter(content, title, repo_name):
    """Add front matter to the content and return the modified content."""
    modified_content = "---\n"
    modified_content += "layout: page\n"
    modified_content += "title: {}\n".format(title)
    modified_content += "permalink: /projects/{}/\n".format(repo_name.split("/")[1])
    modified_content += "---\n"
    modified_content += content
    return modified_content


def save_to_file(content, repo):
    """Save the content to a file."""
    with open("{}.markdown".format(repo.split("/")[1]), "w") as f:
        f.write(content)


def readme_to_jekyll(repo):
    """Convert a github repo's readme to jekyll format."""
    content = get_github_readme(repo)
    title = get_title_text(content)
    content = remove_title_from_readme(content)
    content = add_front_matter(content, title, repo)
    save_to_file(content, repo)


def main():
    """Run the script."""
    for repo in REPOS:
        readme_to_jekyll(repo)


if __name__ == "__main__":
    main()
