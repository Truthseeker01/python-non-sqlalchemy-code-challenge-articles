from collections import Counter

class Article:

    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.all.append(self)
    
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        if hasattr(self, 'title'):
            raise ValueError('Cannot be changed')
        else:
            if type(value) == str and 50 >= len(value) >= 5:
                self._title = value
            else:
                raise TypeError('title must not be empty string')

class Author:

    my_articles = []

    def __init__(self, name):
        self.name = name

    def articles(self):
        my_articles = [ article for article in Article.all if article.author == self]
        return my_articles

    def magazines(self):
        my_magazines = list({ article.magazine for article in Article.all if article.author == self and isinstance(article.magazine, Magazine)})
        return my_magazines

    def add_article(self, magazine, title):
        return Article(author=self, magazine=magazine, title=title)

    def topic_areas(self):
        self.areas = list({article.magazine.category for article in Article.all if article.author == self and isinstance(article.magazine, Magazine)})
        return self.areas if self.areas else None


    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if hasattr(self, 'name'):
            raise ValueError('name cannot be changed')
        else:
            if type(value) == str and len(value) > 0:
                self._name = value
            else:
                raise TypeError('name must not be an empty string')

class Magazine:

    all = []

    magazine_articles = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.all.append(self)

    def articles(self):
        magazine_articles = [ article for article in Article.all if article.magazine == self]
        return magazine_articles

    def contributors(self):
        return list({article.author for article in Article.all if article.magazine == self})

    def article_titles(self):
        titles = [article.title for article in Article.all if article.magazine == self]
        return titles if titles else None

    def contributing_authors(self):
        all_contributing_authors = [article.author for article in Article.all if article.magazine == self]
        counts = Counter(all_contributing_authors)
        contributing_authors = [author for author, count in counts.items() if count > 1]
        return contributing_authors if contributing_authors else None

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if hasattr(self, 'name'):
            raise ValueError('name cannot be changed')
        else:
            if type(value) == str and 16 >= len(value) >= 2:
                self._name = value
            else:
                raise TypeError('name must not be an empty string and between 2 to 16 characters')
            
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, value):
        if type(value) == str and len(value) > 0:
            self._category = value
        else:
            raise TypeError('Category must not be an empty string')