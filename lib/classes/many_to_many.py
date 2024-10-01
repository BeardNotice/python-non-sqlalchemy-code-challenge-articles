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
            raise TypeError("Author must be an instance of the Author class.")
        
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise TypeError("Magazine must be an instance of the Magazine class.")
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50:
            if hasattr(self, "_title"):
                raise Exception("Title cannot be modified once set.")
            else:
                self._title = title
        else:
            raise ValueError("Title must be a string between 5 and 50 characters long.")
    

class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            if hasattr(self, '_name'):
                raise Exception("Name cannot be modified once set.")
            else:
                self._name = name
        else:
            raise ValueError("Name must be a non-empty string.")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(author=self, magazine=magazine, title=title)

    def topic_areas(self):
        unique_categories = {article.magazine.category for article in self.articles()}
        return list(unique_categories) if unique_categories else None


class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all_magazines.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError("Name must be a string between 2 and 16 characters long.")
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category):
            self._category = category
        else:
            raise ValueError("Category must be a non-empty string.")

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        unique_contributors = {article.author for article in self.articles()}
        return list(unique_contributors) if unique_contributors else None

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            if isinstance(article.author, Author):
                if article.author in author_counts:
                    author_counts[article.author] += 1
                else:
                    author_counts[article.author] = 1
        
        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        return contributing_authors if contributing_authors else None
    
    @classmethod
    def top_publisher(cls):
        top_magazine = None
        top_amount = 0

        for magazine in cls.all_magazines:
            article_count = len(magazine.articles())
            if article_count > top_amount:
                top_amount = article_count
                top_magazine = magazine

        return top_magazine if top_magazine else None