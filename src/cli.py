import argparse
from rich import print
from collections import defaultdict


class Clipping:
    def __init__(self, highlight: str, note: str | None = None):
        """The note may be empty."""
        self.highlight = highlight
        self.note = note

    def add_note(self, note: str):
        self.note = note

    def __repr__(self):
        """Return markdown format by default"""
        return (
            f"- {self.highlight}"
            if not self.note
            else f"- {self.highlight}\n    {self.note}"
        )


def get_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "--file",
        type=str,
        help="the path of My Clippings.txt",
    )
    parser.add_argument(
        "--title",
        type=str,
        required=True,
        help=(
            "part of the books's title\n"
            "1. If there are multiple matches, this program will let you decide one\n"
            "2. The extracted clippings will be saved to {title}.md by default"
        ),
    )
    return parser.parse_args()


def read(path: str) -> str:
    with open(path, "r") as f:
        return f.read()


def retrieve_by_title(content: str, title: str) -> list[Clipping]:
    """
    Args:
        content: the content of ./My Clippings.txt file
        title: the book title you want to extract
    """
    # NOTE: each highlight/note is separated by a continuous "="
    component = content.split("=" * 10 + "\n")
    highlights: dict[str, list[Clipping]] = defaultdict(list)
    for comp in component:
        if comp == "":
            continue
        infos, undecided = comp.split("\n\n")
        if undecided.strip() == "":
            continue
        undecided = Clipping(undecided.strip())  # remove "\n" in both sides
        book_title, meta_info = infos.split("\n")
        # FIXME: multilingual support
        if "笔记" in meta_info:
            highlights[book_title][-1].add_note(undecided)
        elif "标注" in meta_info:
            highlights[book_title].append(undecided)

    candidates = [book_title for book_title in highlights if title in book_title]

    if len(candidates) > 1:
        print(
            "[red underline]These books match your input, please provide a more specific title."
        )
        print(
            "\n".join(
                [f":books: {idx}. [green]{line}" for idx, line in enumerate(candidates)]
            )
        )
        book_id = int(
            input("Which book do you want to extract? (give the index please)\n")
        )
        return highlights[candidates[book_id]]
    elif len(candidates) == 1:
        return highlights[candidates[0]]
    else:
        print("[red]No matching books found, please provide the correct book title.")


def main():
    args = get_args()
    all_clippings = read(args.file)
    highlights = retrieve_by_title(all_clippings, args.title)

    with open(f"{args.title}.md", "w") as out:
        out.write("\n".join([str(x) for x in highlights]))


if __name__ == "__main__":
    main()
