#! /usr/bin/env python3

import psycopg2
DBNAME = "news"

query1 = "select title,views from article_view limit 3"

query2 = """select authors.name,sum(article_view.views) as views
from article_view,authors
where authors.id=article_view.author
group by authors.name
order by views desc"""

query3 = """select to_char(date,'Mon DD,YYYY') as date,error_percentage
from error_percentages
where error_percentage>1.0"""


def popular_articles(query1):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query1)
    results = c.fetchall()
    for i in range(len(results)):
        title = results[i][0]
        views = results[i][1]
        print("%s -- %d views" % (title, views))
    db.close()


def popular_authors(query2):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query2)
    results = c.fetchall()
    for i in range(len(results)):
        author = results[i][0]
        views = results[i][1]
        print("%s -- %d views" % (author, views))
    db.close()


def error_percentage(query3):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query3)
    results = c.fetchall()
    for i in range(len(results)):
        date = results[i][0]
        error = results[i][1]
        print("%s -- %f percentage" % (date, error))
    db.close()


print("The most popular articles of all time are:")
popular_articles(query1)
print("\nThe most popular article authors of all time are:")
popular_authors(query2)
print("""\nThe days in which more than 1 percentage of requests lead
to errors are:""")
error_percentage(query3)
