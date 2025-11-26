class application:
    def __init__(self, application_name, catogary, company, app_size, no_of_users, ratings):
        self.application_name = application_name
        self.catogary = catogary
        self.company = company
        self.app_size = app_size
        self.no_of_users = no_of_users
        self.ratings = ratings

    def sigup(self):
        print("signup done,")

    def login(self):
        print("welcome to application")

    def logout(self):
        print("thank you for using")

    def show_info(self):
        print("\n--- Application Information ---")
        print("Application Name :", self.application_name)
        print("Category         :", self.catogary)
        print("Company          :", self.company)
        print("App Size (MB)    :", self.app_size)
        print("No. of Users     :", self.no_of_users)
        print("Ratings          :", self.ratings)
        print("--------------------------------")


app1 = application("instagram", "social media", "meta", 42.34, "1M", "4.4")
app2 = application("facebook", "social media", "meta", 29.76, "200k", "4.2")
app3 = application("whatsapp", "social media", "meta", 86.75, "300kM", "4.3")

app1.sigup()
app2.login()
app3.logout()

app1.show_info()
app2.show_info()
app3.show_info()
