#!/usr/bin/env python

import re
import contextlib
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input_file",
        type=argparse.FileType("r"),
        default="-",
        help="input Hatena Blog article written in Markdown mode",
    )
    args = parser.parse_args()

    with contextlib.closing(args.input_file) as f:
        l = f.readlines()

    IN_CODEBLOCK = False

    print("---\n", end="")  # front matterの表示
    print("title: \n", end="")
    print("date: \n", end="")
    print("---\n", end="")
    print("\n", end="")
    for i in l:
        if re.match(r"^```", i) != None:  # コードブロック内では置換しない
            if IN_CODEBLOCK:
                IN_CODEBLOCK = False
            else:
                IN_CODEBLOCK = True
        if not IN_CODEBLOCK:
            i = re.sub(r"^#####\s", r"### ", i)  # 小見出し
            i = re.sub(r"^####\s", r"## ", i)  # 中見出し
            i = re.sub(r"^###\s", r"# ", i)  # 大見出し
        print(i, end="")


if __name__ == "__main__":
    main()
