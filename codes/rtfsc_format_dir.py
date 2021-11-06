import os
import sys


def output(dir_path, max_level, level, just_length=50):
    if level >= max_level:
        return
    dirs = os.listdir(dir_path)
    if len(dirs) == 0:
        return
    max_size = max([len(dir) for dir in dirs])
    for d in sorted(dirs):
        if os.path.isdir(os.path.join(dir_path, d)):
            print(("| - " * level + "| " + d + "| - " * (max_level - level-1)).ljust(just_length) + " ||")
            output(os.path.join(dir_path, d), max_level, level + 1)


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Example: python ~/GoogleDrive/workcache/rtfsc_format_dir.py . > ~/Downloads/mysql-dir.txt")
        exit(0)

    skip_dirs = [".git", "BUILD", "man", "cmake", ".vscode"]
    #walk_dirs = ["storage"]
    _out = {}
    root = sys.argv[1]
    max_level = 2
    level = 1
    just_length = 50
    for d in sorted(os.listdir(root)):
        if os.path.isdir(os.path.join(root, d)) and d not in skip_dirs:
            print(("| " + d +  " | - " * (max_level - level)).ljust(just_length) + " ||")
            output(d, max_level, level)
