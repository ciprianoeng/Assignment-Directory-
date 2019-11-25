class date():

    def _init_(self):
        self.day = ""
        self.month = ""
        self.year = ""

    def change_date(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

today_date = date()
today_date.day = "19"
today_date.month = "June"
today_date.year = "2019"

change_date = date()
change_date.day = "3"
change_date.month = "August"
change_date.year = "2019"


print(today_date.month + " " + today_date.day + ", " +today_date.year)

print(change_date.month + " " + change_date.day + ", " +change_date.year)