#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Article, Author, Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # Create instances of Author and Magazine
    author1 = Author("John Doe")
    magazine1 = Magazine("Tech Weekly", "Technology")

    # Add an article to author1
    article1 = author1.add_article(magazine1, "AI Revolution")

    # Print the created instances to verify their properties
    print(f"Author: {author1.name}")
    print(f"Magazine: {magazine1.name}, Category: {magazine1.category}")
    print(f"Article: {article1.title}, Author: {article1.author.name}, Magazine: {article1.magazine.name}")

    # Create another article to use the Article class and avoid the unused import warning
    article2 = Article(author1, magazine1, "The Future of AI")
    print(f"Another Article: {article2.title}, Author: {article2.author.name}, Magazine: {article2.magazine.name}")

    # don't remove this line, it's for debugging!
    ipdb.set_trace()
