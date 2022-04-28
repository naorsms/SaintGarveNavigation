from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

option = webdriver.ChromeOptions()
option.add_argument('headless')


class Rabbis:
    """ Contains rabbis attributes and grave location"""

    def __init__(self, name, city, district, coordinate):
        self.name = name
        self.city = city
        self.district = district
        self.coordinate = coordinate


class WebScrape:
    """Contains functions of scrape"""
    GRAVE_DICT = {'קבר דוד המלך ': 'ירושלים', ' קבר שמעון הצדיק ': 'ירושלים', ' קברי הסנהדרין ': 'ירושלים',
                  ' בית הקברות היהודי בהר הזיתים ': 'ירושלים', 'מערת המכפלה ': 'יהודה', ' קבר רחל ': 'יהודה',
                  ' קבר ישי ורות ': 'יהודה', ' קבר אבנר בן נר ': 'יהודה', ' קבר עתניאל בן קנז ': 'יהודה', 'קבר יוסף ': 'שומרון',
                  ' קבר איתמר בן אהרן הכהן ': 'שומרון', ' קבר אלעזר בן אהרן הכהן ': 'שומרון', ' גבעת פינחס ': 'שומרון',
                  ' קבר יהושע בן נון ': 'שומרון', 'קבר רבי שמעון בר יוחאי ': 'הגליל', ' קבר יונתן בן עוזיאל ': 'הגליל',
                  ' קבר רבי יהודה הנשיא ': 'הגליל', ' קברי מרדכי ואסתר ': 'הגליל', ' בית הקברות היהודי העתיק בצפת ': 'הגליל',
                  ' מערת שם ועבר ': 'הגליל', ' מערת הלל ': 'הגליל', 'קבר רבי מאיר בעל הנס ': 'טבריה', ' קבר הרמב"ם ': 'טבריה',
                  ' קבר רחל אשת רבי עקיבא ': 'טבריה', ' קבר האמהות ': 'טבריה', 'נבי רובין ': 'קברים נוספים', ' נבי ימין ': 'קברים נוספים',
                  ' קבר שמואל הנביא ': 'קברים נוספים'}

        #document.getElementsByTagName('p')[1].innerText
        #document.getElementsByClassName('navbox nowraplinks')[0].querySelectorAll('tbody')[0].rows[1].cells[1].innerText

    def wikipedia_scrape(self, url, grave_name):
        driver = webdriver.Chrome()
        driver.get(url + grave_name)
        r = requests.get(url, allow_redirects=True)

browser.execute_script('''window.open("http://bings.com","_blank");''')#open new tab

"https://telechofesh.co.il/קברי-צדיקים/page/0/"
# # document.getElementsByClassName("biz-item grid-noGutter ng-scope")[20].getElementsByClassName("ng-binding")[0].innerText#name
# document.getElementsByClassName("biz-item grid-noGutter ng-scope")[3].getElementsByTagName("a")[0].href#url
# document.getElementsByClassName("col-8_sm-12 entry-title")[0].innerText#name
# document.getElementsByClassName('lead')[0].innerText#decription
# document.getElementsByClassName('details')[0].getElementsByTagName('b')[0].innerText#district and city
# document.getElementsByClassName('icon-single ng-scope')[0].getElementsByTagName("li")[7].getElementsByTagName("a")[0].href#waze api and coordinates