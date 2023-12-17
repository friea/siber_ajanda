from bs4 import BeautifulSoup
import requests
def bilgeIs_siber_dersler():
    course_names = []
    url="https://bilgeis.net/tr/courses/category/26/bilgi-guvenligi"
    try:
        response = requests.get(url)
        parser = BeautifulSoup(response.text,"html.parser")
        course_divs = parser.find_all("div",{"class":"post-content"})
        for course_div in course_divs:
            content=course_div.find("h2")
            course_names.append(content.text.strip())
            # print(content.text.strip())
        return course_names
    except Exception as e:
        print(e)
        return e
        pass



