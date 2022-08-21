"""Inject story data into template to create epub source."""


from datetime import datetime
from pathlib import Path
from typing import List

from jinja2 import Environment, FileSystemLoader
from ruyaml import YAML


BUILD_PATH = Path("build/OEBPS")


def get_data():
    """Get data from story.yaml and validate it."""
    yaml = YAML(typ="safe")

    with open("story.yaml", encoding="UTF-8") as fin:
        data = yaml.load(fin)

    # Validate data
    assert "title" in data
    assert "author" in data
    assert "date" in data
    assert "description" in data
    assert "story" in data

    assert isinstance(data["story"], list)

    for line in data["story"]:
        assert isinstance(line, str)

    return data


def jinja2_env():
    """Create jinja2 env that can find templates under template/OEBPS."""
    loader = FileSystemLoader(searchpath="template/OEBPS")
    return Environment(loader=loader)


def inject_content_opf(
    title: str, author: str, date: str, description: str, date_modified: str
):
    """Inject metadata into content.opf file."""
    env = jinja2_env()
    template = env.get_template("content.opf.template")

    content = template.render(
        title=title,
        author=author,
        date=date,
        description=description,
        date_modified=date_modified,
    )

    file = BUILD_PATH / "content.opf"
    file.write_text(content)


def inject_toc_html(title: str):
    """Inject title to create toc.html file."""
    env = jinja2_env()
    template = env.get_template("toc.html.template")

    content = template.render(title=title)

    file = BUILD_PATH / "toc.html"
    file.write_text(content)


def inject_toc_ncx(title: str, author: str):
    """Inject title and author to create tox.ncs file."""
    env = jinja2_env()
    template = env.get_template("toc.ncx.template")

    content = template.render(title=title, author=author)

    file = BUILD_PATH / "toc.ncx"
    file.write_text(content)


def inject_story_html(title: str, author: str, story: List[str]):
    """Inject the complete data into poem.html."""
    env = jinja2_env()
    template = env.get_template("story.html.template")

    content = template.render(title=title, author=author, story=story)

    file = BUILD_PATH / "story.html"
    file.write_text(content)


def main():
    """Entrypoint for script."""
    data = get_data()

    title = data["title"]
    author = data["author"]
    date = data["date"]
    description = data["description"]
    story = data["story"]
    date_modified = str(datetime.now())

    inject_content_opf(
        title=title,
        author=author,
        date=date,
        description=description,
        date_modified=date_modified,
    )
    inject_toc_html(title=title)
    inject_toc_ncx(title=title, author=author)
    inject_story_html(title=title, author=author, story=story)


if "__main__" in __name__:
    main()
