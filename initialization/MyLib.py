from subprocess import call
from subprocess import check_output
from re import search


def convert_dict(lst):
    dictionary = {}
    for ind in range(0, len(lst), 2):   # converts to a dict of type [module]: version
        dictionary[lst[ind]] = lst[ind + 1]
    return dictionary


def get_homepage(data):
    dict_of_homepages = {}
    for module in data.keys():
        pars_info = check_output(f"pip show {module}", encoding="utf-8").split()
        if search("(?P<url>https?://[^\s]+)", ' '.join(pars_info)).group("url"):
            dict_of_homepages[module] = search("(?P<url>https?://[^\s]+)", ' '.join(pars_info)).group("url")
        else:
            dict_of_homepages[module] = 'not found'
    return dict_of_homepages


def get_dataUpdate():   # pars info about modules being updated
    pars_info = check_output("pip list -o", encoding="utf-8").strip().split('\n')[2:]
    data_update = list(map(lambda line: line.split()[0], pars_info))
    return data_update


def moduleUpdate(name_module):
    call(f"pip install {name_module} --upgrade", shell=True)


output_pip = convert_dict(check_output("pip list", encoding="utf-8").split()[4:])
home_pages = get_homepage(output_pip)