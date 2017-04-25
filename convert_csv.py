import csv
import os


def convert_csv():
    csv_path = "cinderella.csv"
    f = open(csv_path, 'r', encoding='utf-8')
    reader = csv.reader(f)

    csv_path = "cinderella_.csv"
    f = open(csv_path, 'w', encoding='utf-8')
    writer = csv.writer(f, lineterminator='\n')

    for index, row in enumerate(reader):
        jp, rom = row

        if index < 188:
            first_name, last_name = rom.split('_')
            new_rom = last_name + '_' + first_name
        else:
            new_rom = rom

        writer.writerow((jp, new_rom))


def rename_dirs():
    csv_path = "cinderella_.csv"
    f = open(csv_path, 'r', encoding='utf-8')
    reader = csv.reader(f)
    root = "./cinderella/cards"
    for (jp, rom) in reader:
        src_path = os.path.join(root, jp).replace('\ufeff', '')
        dst_path = os.path.join(root, rom)
        os.rename(src_path, dst_path)


rename_dirs()
