
# quick note, I wanted to use TypeError and ValueError in the setters but it was messing up the tests so I changed it.

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
            print("author must be an instance of the Author class.")
        
    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            print("magazine must be an instance of the Magazine class.")
    
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5<=len(title)<=50:
            if hasattr(self, "_title"):
                print("Title can not be modified.")
            else:
                self._title = title
        else:
            print("Title must be a string between 5 and 50 characters long.")
    


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
                print("Name can not be modified.")
            else:
                self._name = name
        else:
            print("Name must be a non-empty string.")

    def articles(self):
        articles_by_author = []
        for article in Article.all:
            if isinstance(article, Article) and article.author == self:
                articles_by_author.append(article)
        return articles_by_author

    def magazines(self):
        unique_mags = {article.magazine for article in self.articles()} # set comprehension
        return list(unique_mags)

    def add_article(self, magazine, title):
        new_article = Article(author=self, magazine=magazine, title=title)
        return new_article

    def topic_areas(self):
        unique_categories = []
        for article in self.articles():
            category = article.magazine.category
            if category not in unique_categories:
                unique_categories.append(category)
        if len(unique_categories) == 0:
            unique_categories = None
        return unique_categories

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
        if isinstance(name, str) and 2<=len(name)<=16:
            self._name = name
        else:
            print("Name must be a string between 2 and 16 characters long.")
    
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category):
            self._category = category
        else:
            print("Category must be a non-empty string.")

    def articles(self):
        articles_in_magazine = []
        for article in Article.all:
            if isinstance(article, Article) and article.magazine == self:
                articles_in_magazine.append(article)
        return articles_in_magazine

    def contributors(self):
        unique_contributors = {article.author for article in self.articles()}
        return list(unique_contributors) if unique_contributors else None
            

    def article_titles(self):
        titles = []
        for article in self.articles():
            titles.append(article.title)
        if len(titles) == 0:
            titles = None
        return titles


    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            if isinstance(article.author, Author):
                if article.author in author_counts:
                    author_counts[article.author]+=1
                else:
                    author_counts[article.author]=1
        contributing_authors = []
        for author, count in author_counts.items():
            if count > 2:
                contributing_authors.append(author)
        
        if len(contributing_authors) == 0:
            return None
        
        return contributing_authors
    
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