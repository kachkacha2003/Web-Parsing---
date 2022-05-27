import requests
from bs4 import BeautifulSoup
from time import sleep
import csv

file = open("vacancies.csv", "w", encoding="utf-8-sig", newline="\n")
file_obj = csv.writer(file)
file_obj.writerow(["Vacancy", "Employer", "Location"])
h = {"Accept-Language": "en-US"}

index = 1

while index <= 5:
    url = f"https://www.hr.ge/search-posting?pg={index}"
    r = requests.get(url, headers=h)

    soup = BeautifulSoup(r.text, "html.parser")
    vacancy_list = soup.find("div", {"class": "ann"})
    vacancies = vacancy_list.find_all("div", {"class": "container"})

    for i in vacancies:
        vacancy = i.div.a.div.text
        employer = i.find("div", {"class": "company"}).text
        location = i.find("span", {"class": "additional-info__location-text"}).text
        file_obj.writerow([vacancy, employer, location])
    index += 1
    sleep(5)
