## Intro
I like reading using Kindle and adding highlights for later review. That's the reason why I wrote this small software (It's actually a script though) to extract all highlights from a specific book.

## Roadmap
- [x] Support *notes* besides *highlights*.
- [ ] Multilingual support. Currently, this small script only support `My Clippings.txt`created in *Chinese*.

## Usage
Get the file path of `My Clippings.txt`, and then pass it to `--file`. It will analyze all the clippings within this file and return the highlights you want. The default behavior is saving the highlights to a file named `{title}.md` (the `title` here is equal to your `--title`)

```sh
$ python src/cli.py -h
usage: cli.py [-h] [--file FILE] --title TITLE

options:
  -h, --help     show this help message and exit
  --file FILE    the path of My Clippings.txt
  --title TITLE  part of the books's title
                 1. If there are multiple matches, this program will let you decide one
                 2. The extracted clippings will be saved to {title}.md by default
```
