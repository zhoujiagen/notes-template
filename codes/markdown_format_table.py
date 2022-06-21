# -*- coding: utf-8 -*

import sys
import re

# ^\|.+\|\r?\n$
# |fchmod|change permissions of a file|
# |fchmod||

if __name__ == "__main__":
    """Output formatted tables in Markdown documents"""

    if len(sys.argv) < 2:
        print("Example: python markdown_format_table.py sample.md")
        exit(0)

    lines = []
    with open(sys.argv[1], mode='r', encoding="utf-8") as f:
        lines = f.readlines()

    tr_pattern = re.compile("^\|.+\|\r?\n$")
    rows = []
    max_column_cnt = 0
    for line in lines:
        if re.fullmatch(tr_pattern, line) is not None:
            row = [col.strip() for col in line[1:len(line) - 2].split("|")]
            if len(row) > max_column_cnt:
                max_column_cnt = len(row)
            rows.append(row)

    max_sizes = []
    for i in range(max_column_cnt):
        max_sizes.append(max([len(row[i]) for row in rows]))

    for row in rows:
        for i in range(len(row)):
            if len(row[i]) <= max_sizes[i]:
                dis = max_sizes[i] + 1 - len(row[i])
            row[i] = "{data}{padding}".format(data=row[i], padding=" " * dis)

        print("|{line}|".format(line="|".join(row)))
