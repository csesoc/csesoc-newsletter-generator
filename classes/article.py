class Article:
    def __init__(self, url, title, description, img):
        self.url = url
        self.title = title
        self.description = description
        self.img = img

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
