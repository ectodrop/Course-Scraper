import requests
import bs4
import re
import pprint
import pickle
def to_list(string):
        ors = re.split("\[|\]|\.and\.", string)
        l = []
        for i in ors:
            if "or" in i:
                i = tuple(filter(None, tuple(re.split("\.or\.|\.or|or\.", i))))
            l.append(i)
        return list(filter(None, l))
_pre_req = "pre-requisites"
_pre_req_full = "pre-requisites-full"
_desc = "desc"
course_info = {}


url = "https://utsc.calendar.utoronto.ca/print/view/pdf/search_courses/print_page/debug"
r = requests.get(url)

bs = bs4.BeautifulSoup(r.text, features = "html.parser")
div = bs.find("div", {"class":"view-content"})
courses = div.findChildren("div", recursive = False)
print(len(courses))
code = courses[0].find("div", {"class":"views-field views-field-field-course-title"}).text
print(code)
for c in courses:
    code = c.find("div", {"class":"views-field views-field-field-course-title"}).text
    pre_reqs = c.find("span", {"class":"views-field views-field-field-prerequisite"})
    text = "" if pre_reqs == None else pre_reqs.text.split("Prerequisite: ")[1]
    pre_reqs = [] if pre_reqs == None else [a.text for a in pre_reqs.findChildren("a")]
    temp = ""
    # for p in pre_reqs:
    #     if "H3" in p or "and" in p or not re.search(r"\bor",p) == None:
    #         temp += re.sub(",|\.|\(|\)", "", p)  + "."
    # r = temp.rfind("H3")
    # if not r == -1:
    #     if len(temp) >= r+2 and temp[r+2] == "]":
    #         temp = temp[:r+3]
    #     else:
    #         temp = temp[:r+2]
    # else:
    #     temp = ''
    index = code.find("H3")+2
    course_title = code[index:]
    course_info[code[:index]] = {}
    course_info[code[:index]][_pre_req_full] = text
    course_info[code[:index]][_pre_req] = pre_reqs
    course_info[code[:index]][_desc] = code

#pprint.pprint(course_info)
dictionary_data = course_info
a_file = open("course_info.pkl", "wb")
pickle.dump(dictionary_data, a_file)
a_file.close()


