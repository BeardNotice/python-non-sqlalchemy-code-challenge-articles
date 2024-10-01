class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise TypeError("author must be an instance of the Author class.")
        
    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise TypeError("magazine must be an instance of the Magazine class.")
    
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5<=len(title)<=50:
            if hasattr(self, "_title"):
                print("Title can not be modified.") #tried raise ValueError but the tests were not passing
            else:
                self._title = title
        else:
            print("Title must be a string between 5 and 50 characters long.") #tried raise ValueError but tests were also not passing here
    


class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            if hasattr(self, '_name'):
                print("Name can not be modified.") # would normally use raise ValueError
            else:
                self._name = name
        else:
            print("Name must be a non-empty string.") # would normally use raise ValueError

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2<=len(name)<=16:
            self._name = name
        else:
            print("Name must be a string between 2 and 16 characters long.") # would normally use raise ValueError
    
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category):
            self._category = category
        else:
            print("Category must be a non-empty string.") # would normally use raise ValueError

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass