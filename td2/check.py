"""TD2: check your page. Run `python check.py` from the td2 folder. Do not modify this file."""
from html.parser import HTMLParser
from pathlib import Path

VOID = {"meta", "img", "input", "br", "hr", "link"}


class Node:
    def __init__(self, tag, attrs):
        self.tag, self.attrs, self.children, self.text = tag, dict(attrs), [], ""

    def all(self, tag):
        """Every element with this tag inside this one."""
        found = []
        for child in self.children:
            if child.tag == tag:
                found.append(child)
            found += child.all(tag)
        return found

    def words(self):
        return (self.text + " ".join(c.words() for c in self.children)).strip()


class Tree(HTMLParser):
    def __init__(self):
        super().__init__()
        self.root = Node("root", [])
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs)
        self.stack[-1].children.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        self.stack[-1].text += data.strip()


tree = Tree()
tree.feed(Path("index.html").read_text(encoding="utf-8"))
page = tree.root


def section(name):
    return [s for s in page.all("section") if s.attrs.get("id") == name][0]


def check(name, test):
    try:
        ok = test()
    except Exception as error:  # show the problem and go on with the next check
        print(f"[  ] {name}  ->  {type(error).__name__}: {error}")
        return
    print(f"[OK] {name}" if ok else f"[  ] {name}")


def labelled(field):
    return any(label.attrs.get("for") == field.attrs.get("id") for label in page.all("label"))


check("2A page title", lambda: page.all("title")[0].words() != "" and "TODO" not in page.all("title")[0].words())
check("2B header with one h1", lambda: len(page.all("h1")) == 1 and len(page.all("header")[0].all("h1")) == 1)
check("2C nav with a list of 3 internal links", lambda: {"#about", "#figures", "#search"} <= {
    a.attrs.get("href") for li in page.all("nav")[0].all("li") for a in li.all("a")})
check("3A section about: h2 and paragraph", lambda: bool(section("about").all("h2") and section("about").all("p")))
check("3B link to Eurostat", lambda: any("europa.eu" in a.attrs.get("href", "") for a in section("about").all("a")))
check("3C image with alt text", lambda: any(i.attrs.get("src") == "images/network.svg" and i.attrs.get("alt")
                                           for i in section("about").all("img")))
check("4A table with a caption", lambda: section("figures").all("table")[0].all("caption")[0].words() != "")
check("4B header row in thead with th", lambda: len(section("figures").all("thead")[0].all("th")) >= 2)
check("4C at least 3 data rows in tbody", lambda: len([r for r in section("figures").all("tbody")[0].all("tr")
                                                      if len(r.all("td")) >= 2]) >= 3)
check("5A form with method get", lambda: section("search").all("form")[0].attrs.get("method", "get").lower() == "get")
check("5B select named country, with label", lambda: any(
    s.attrs.get("name") == "country" and len(s.all("option")) >= 3 and labelled(s) for s in page.all("select")))
check("5C number field named year, with label", lambda: any(
    i.attrs.get("name") == "year" and i.attrs.get("type") == "number" and "required" in i.attrs and labelled(i)
    for i in page.all("input")))
check("5D submit button", lambda: bool(section("search").all("form")[0].all("button")))
check("6A footer naming the source", lambda: "eurostat" in page.all("footer")[0].words().lower())
