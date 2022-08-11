import csv


def take_csvdata():
    data_file = []
    with open("../resources/modules.csv", encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';', quotechar=';', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            data_file.append(row)
    new_file = []
    hyperlink_format = '<a href="{link}">{text}</a>'
    for line in data_file:
        new_file.append({
            "module": hyperlink_format.format(link=str(line["link"])[:-1], text=line["module"]),
            "info": line["info"],
            "version": line["version"]
        })
    return new_file
