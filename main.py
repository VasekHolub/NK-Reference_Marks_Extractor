import csv
import os
import re

def exclusion_list_load(file_path: str) -> list:
    with open(file_path, encoding="UTF-8") as f:
        contents = f.read()
    return contents.split()


def txt_file_load(file_path: str) -> list:
    with open(file_path, encoding="UTF-8") as f:
        contents = f.read()
    return contents.split()


def string_list_stripper(string_list: list) -> list:
    stripped_contents_list = list()
    for i in string_list:
        stripped_contents_list.append(i.strip(',.<>!:"";?()'))
    return stripped_contents_list


def find_indices(list_to_check: list, item_to_find: str) -> list:
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(idx)
    return indices


def reference_mark_extractor(extraction_source: list) -> list:
    ref_marks = list()
    for i in extraction_source:
        if i not in ref_marks and i not in exclusion_list_load(
            os.path.join("exclusion_list.txt")
        ):
            for k in find_indices(extraction_source, i):
                if k + 1 >= len(extraction_source):
                    break
                elif extraction_source[k + 1] == "":
                    continue
                elif (
                    extraction_source[k + 1][0].isnumeric()
                    and i not in ref_marks
                    and not i.isnumeric()
                ):
                    ref_marks.append(i)
    return ref_marks


def ref_marks_csv_exporter(ref_marks: list):
    with open("csv_file.csv", mode="w", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file)
        for item in ref_marks:
            writer.writerow([item])


def main():
    contents_list = string_list_stripper(txt_file_load(os.path.join("file.txt")))
    ref_marks = reference_mark_extractor(contents_list)
    ref_marks_csv_exporter(ref_marks)


if __name__ == "__main__":
    main()
