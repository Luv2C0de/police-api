class Crime:

    def __init__(self, title, police_number, address, district):
        self.title = title
        self.police_number = police_number
        self.address = address
        self.district = district

    @property
    def getTitle(self):
        return self.title

    def __str__(self):
        return "Record: ('{}', '{}', '{}', '{}')".format(self.title, self.police_number, self.address, self.district)
