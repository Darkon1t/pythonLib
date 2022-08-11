from subprocess import check_output, check_call
import requests
from bs4 import BeautifulSoup


URL = "https://pypi.org/search/?q=pip&o="
HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/88.0.4324.190 Safari/537.36", "accept": "*/*"}


def get_version():
    # get info from site PyPi
    data = requests.get(URL, headers=HEADERS)
    if data.status_code == 200:
        soup = BeautifulSoup(data.text, "html.parser")
        card = soup.find("a", class_="package-snippet")
        actual_version = card.find("span", class_="package-snippet__version").get_text(strip=True)
        return actual_version
    else:
        return []


def your_version_pip():
    version = check_output("pip -V", encoding="utf-8").split()
    return {
        "version": version[1],
        "path": version[3] + version[4]
    }


def button_state():
    pip_version = "".join(get_version().split(".")).ljust(4, "0")
    if not pip_version.isdigit():
        pip_version = "".join([el for el in pip_version if el.isdigit()]).ljust(4, "0")
    your_version = your_version_pip()
    your_version["version"] = "".join(your_version["version"].split(".")).ljust(4, "0")
    if not your_version["version"].isdigit():
        your_version["version"] = "".join([el for el in your_version["version"] if el.isdigit()]).ljust(4, "0")

    # comparing module versions

    flag = True
    if your_version["version"] == pip_version:
        flag = False
    else:
        flag = True
    return flag
