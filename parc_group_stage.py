import requests
import pprint
from bs4 import BeautifulSoup

set_teams = set()
be_or_not = False
r = requests.get("https://liquipedia.net/dota2/The_International/2023")
rtx = r.text
with open(r"C:\Users\Nomad\Downloads\req.txt", "w", encoding="utf-8") as f:
    f.write(rtx)
soup = BeautifulSoup(rtx, "lxml")

search_team = soup.find_all("span", class_="team-template-text")
for x in range(len(search_team)):
    search_team[x] = search_team[x].find("a")
    try:
        set_teams.add(search_team[x].get('title'))
    except BaseException:
            pass

def stat_one_team_group_stage(research_inf):
    if research_inf in set_teams:
        be_or_not = True

    search_team = soup.find_all("span", class_="team-template-text")
    for x in range(len(search_team)):
        search_team[x] = search_team[x].find("a")
        try:
            if search_team[x].get("title")==research_inf:
                Our_team = search_team[x]
            set_teams.add(search_team[x].get('title'))
        except BaseException:
                pass

#group_stage = soup.find_all("td", class_="grouptableslot")
#for q in group_stage:
#    print(q)
    if be_or_not:
        win_lose = soup.find_all("td", {"width": "35px", "style": "white-space:pre"})
        for i in win_lose:
            a = i.find_parent()
            x = Our_team.find_parent()
            if a.find("a").get("title").lower() == research_inf.lower():
                win_rate = a.find("td", {"width": "35px", "style": "white-space:pre"}).text
                win_rate = win_rate.split("-")
                return f"Cтатистика команды {research_inf}\nКоличество побед:{win_rate[0]}\nКоличество лузов:{win_rate[1]}\nВин рейт:{int(win_rate[0])/(int(win_rate[0])+int(win_rate[1]))*100}%"

    else:
        return f"{research_inf} не существует на инте"

def all_stat_group_stage():
    a = ""
    try_to_print_team = soup.find_all("td", class_="grouptableslot")
    for i in try_to_print_team:
        name_team = i.find("a")["title"]
        win_lose = i.find_parent()
        win_lose = win_lose.find("td", {"width": "35px", "style": "white-space:pre"}).text
        win_lose = win_lose.split("-")
        a += f"Cтатистика команды {name_team}\nКоличество побед:{win_lose[0]}\nКоличество лузов:{win_lose[1]}\nВин рейт:{int(win_lose[0])/(int(win_lose[0])+int(win_lose[1]))*100}%\n\n"
    return a
    '''search_team = soup.find_all("td", class_="template-box")
    search_team = list(search_team)
    win_lose = soup.find_all("td", {"width": "35px", "style": "white-space:pre"})
    for x in range(len(search_team)):
        for i in win_lose:
            
            try:
                search_team[x] = search_team[x].find("a")
                a = i.find_parent()
                q = search_team[x].find_parent()
                if a.find("a").get("title").lower() == q.text.lower():
                    win_rate = a.find("td", {"width": "35px", "style": "white-space:pre"}).text
                    win_rate = win_rate.split("-")
                    name_team = search_team[x].get("title")
                    print(f"Cтатистика команды {name_team}\nКоличество побед:{win_rate[0]}\nКоличество лузов:{win_rate[1]}\nВин рейт:{int(win_rate[0])/(int(win_rate[0])+int(win_rate[1]))*100}%")
            except BaseException:
                pass'''

'''try_to_print_team = soup.find_all("td", class_="grouptableslot")
for i in try_to_print_team:
    name_team = i.find("a")["title"]
    win_lose = i.find_parent()
    win_lose = win_lose.find("td", {"width": "35px", "style": "white-space:pre"})
    print(name_team)
    print(win_lose.text)
    win_rate = win_rate.split("-")
    print(i)'''



#for i in range(len(page_all_teams)):
#    page_all_teams[i] = page_all_teams[i].text.strip()
#    print(page_all_teams[i].text.strip())



