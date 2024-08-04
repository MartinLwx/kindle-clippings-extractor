## Intro
I like reading using Kindle and adding highlights for later review. That's the reason why I wrote this small software (It's actually a script though) to extract all highlights from a specific book.

## Roadmap
- [ ] Support *notes* besides *highlights*.

## Usage
Get the file path of `My Clipping.txt`, and then pass it to `--file`. It will analyze all the clippings within this file and return the highlights you want. The default behavior is saving the highlights to a file named `{title}.md` (the `title` here is equal to your `--title`)

```sh
$ python src/cli.py -h
usage: cli.py [-h] [--title TITLE] [--file FILE]

options:
  -h, --help     show this help message and exit
  --title TITLE  the title of the book you want to extract
  --file FILE    the path of My Clipping.txt
```
