import os
import sys


def output(dir_path):
    """"""
    total_lines = 0
    for root, dirs, files in os.walk(dir_path, topdown=True):
        print(root)
        max_size = 0
        file_size_dict = {}
        for name in files:
            if len(name) > max_size:
                max_size = len(name)
            try:
                if name.endswith(".h") or name.endswith(".cc") or name.endswith(".ic"):
                    file_lines = sum(1 for line in open(
                        os.path.join(root, name))) - 26
                else:
                    file_lines = sum(1 for line in open(
                        os.path.join(root, name)))
            except UnicodeDecodeError as e:
                print("ERROR", name, e)
                file_lines = 0
            file_size_dict[name] = file_lines
            total_lines = total_lines + file_lines

        # header
        print("""|File|Line|Description|Progress|""")
        print("""|:---|---:|:---|:---|""")
        for name in sorted(files):
            print('|', "[{0}](#{0})".format(name).ljust(max_size*2 + 6),
                  "| {:>5d}".format(file_size_dict[name]), '|||')
        print()
        for name in sorted(files):
            print("## {}".format(name))
        print()
    print("Total lines =", total_lines)


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Example: python ~/GoogleDrive/workcache/rtfsc_format_file_names.py . > ~/Downloads/mysql-innobase.txt")
        exit(0)
    output(sys.argv[1])
