import csv
import os

exclusion_list = [
    "OBR.",
    "Obr.",
    "Obr",
    "Fig.",
    "FIG.",
    "/",
    "PATENTANSPRÜCHE",
    "Fig",
    "Figur",
    "Anspruch",
    "Anspruchs",
    "Ansprüche",
    "und",
    "bis",
    "oder",
    "Patentansprüchen",
    "Seite",
    "US",
    "WO",
    "Figure",
    "Figures",
    "FIG",
    "CLAIMS",
    "to",
    "page",
    "Page",
    "pages",
    "Pages",
    "and",
    "or",
    "between",
    "claim",
    "claims",
    "obr",
    "od",
    "ke",
    "mezi",
    "alespoň",
    "být",
    "do",
    "až",
    "nebo",
    "NÁROKY",
    "OBR",
    "nároky",
    "nárok",
    "NÁROK",
    "mít",
    "na",
    "než",
    "nároku",
    "+/-",
    "+",
    "-",
    "zejména",
    "výhodně",
    "výhodněji",
    "nejlépe",
    "nejméně",
    "nepřesahuje",
    "über",
    "wird",
    "werden",
    "von",
    "um",
    "nahe",
    "mit",
    "kann",
    "ist",
    "einer",
    "bei",
    "als",
    "Claims",
    "of",
    "at",
    "about",
    "sind",
    "zwischen",
    "Figuren",
]


def txt_file_load(file_path: str) -> list:
    with open(file_path, encoding="UTF-8") as f:
        contents = f.read()
    return contents.split()


def string_list_stripper(string_list: list) -> list:
    stripped_contents_list = list()
    for i in string_list:
        stripped_contents_list.append(i.strip(',.<>!:"";?()'))
    return stripped_contents_list


def find_indices(list_to_check, item_to_find):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(idx)
    return indices


def reference_mark_extractor(extraction_source: list) -> list:
    ref_marks = list()
    for i in extraction_source:
        if i not in ref_marks:
            for k in find_indices(extraction_source, i):
                if k + 1 >= len(extraction_source):
                    break
                elif extraction_source[k + 1] == "":
                    continue
                elif extraction_source[k + 1][0].isnumeric():
                    ref_marks.append(i)
    return ref_marks


def ref_mark_repetitons_remover(ref_marks: list) -> list:
    unique_ref_marks = list()
    ref_marks_set = set(ref_marks)
    for i in ref_marks_set:
        if not i.isnumeric() and i.isalnum() and i not in exclusion_list:
            unique_ref_marks.append(i)
    unique_ref_marks.sort()
    return unique_ref_marks


def unique_ref_marks_csv_exporter(unique_ref_marks):
    with open("csv_file.csv", mode="w", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file)
        for item in unique_ref_marks:
            writer.writerow([item])


def main():
    contents_list = string_list_stripper(txt_file_load(os.path.join("file.txt")))
    ref_marks = reference_mark_extractor(contents_list)
    unique_ref_marks = ref_mark_repetitons_remover(ref_marks)
    unique_ref_marks_csv_exporter(unique_ref_marks)


if __name__ == "__main__":
    main()