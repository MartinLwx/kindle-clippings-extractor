import argparse
from rich import print
from collections import defaultdict


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--title",
        type=str,
        help="the title of the book you want to extract",
    )
    parser.add_argument(
        "--file",
        type=str,
        help="the path of My Clipping.txt",
    )

    return parser.parse_args()


def read(path: str) -> str:
    with open(path, "r") as f:
        return f.read()


def retrieve_by_title(content: str, title: str) -> list[str]:
    component = content.split("=" * 10 + "\n")
    highlights = defaultdict(list)
    for comp in component:
        if comp == "":
            continue
        infos, highlight = comp.split("\n\n")
        if highlight.strip() == "":
            continue
        highlight = highlight.strip()  # remove "\n" in both sides
        book_title, _ = infos.split("\n")
        highlights[book_title].append(highlight)

    while True:
        candidates = [book_title for book_title in highlights if title in book_title]
        if len(candidates) > 1:
            print(
                "[red underline]These books match your input, please provide a more specific title."
            )
            print("\n".join([f":books:[green]{line}" for line in candidates]))
            user_input = input("Which book do you want to extract?\n")
            title = user_input.strip()
        elif len(candidates) == 1:
            return highlights[candidates[0]]
        else:
            print(
                "[red]No matching books found, please provide the correct book title."
            )


def markdownize(lines: list[str]) -> list[str]:
    """Currently, This function only add a leading `- ` to all lines"""
    return ["- " + s for s in lines]


def main():
    args = get_args()
    all_clippings = read(args.file)
    highlights = retrieve_by_title(all_clippings, args.title)
    ans = markdownize(highlights)

    with open(f"{args.title}.md", "w") as out:
        out.write("\n".join(ans))


if __name__ == "__main__":
    main()
