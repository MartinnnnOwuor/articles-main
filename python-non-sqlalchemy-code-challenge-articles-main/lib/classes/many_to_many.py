class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError("Title must be a string")
        if not 5 <= len(value) <= 50:
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Author must be an instance of Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be an instance of Magazine")
        self._magazine = value


class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set([article.magazine for article in self._articles]))

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine")
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        return list(set([article.magazine.category for article in self._articles]))

    @staticmethod
    def top_publisher():
        magazines = Magazine.all
        if not magazines:
            return None
        return max(magazines, key=lambda magazine: len(magazine.articles()))


class Magazine:
    all = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []
        self.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be a string")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set([article.author for article in self._articles]))

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        authors = {}
        for article in self._articles:
            author = article.author
            if author in authors:
                authors[author] += 1
            else:
                authors[author] = 1
        return [author for author, count in authors.items() if count > 2]

