# Solution of Log Analysis project
# Full Stack Nanodegree
# Submitted by: Ammar Mustafa

import psycopg2 

# Answer of Quesition 1: 
# What are the most popular three articles of all time?


def most_popular_articles(): 
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    query = """SELECT title,  COUNT(*) as article_views_num
                FROM articles, log
                WHERE slug = SUBSTRING(path, 10)
                GROUP BY title 
                ORDER BY article_views_num desc
                LIMIT 3;"""
    c.execute(query)
    popular_articles = c.fetchall()
    db.close()
    return popular_articles

# Answer of Quesition 2: 
# Who are the most popular article authors of all time?


def most_popular_authors():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    query = """SELECT name,  COUNT(*) as author_articles_views_num
                FROM authors, articles, log
                WHERE (slug = substring(path, 10) 
                and authors.id = articles.author)
                GROUP BY name 
                ORDER BY author_articles_views_num desc;"""
    c.execute(query)
    popular_authors = c.fetchall()
    db.close()
    return popular_authors

# Answer of Quesition 3: 
# On which days did more than 1% of requests lead to errors?


def requests_errors():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    query = """SELECT total_log.log_date, 
                ROUND(((error_num * 100.0) / views_num), 3) AS error_per 
                FROM 
                (SELECT time::date as log_date, COUNT(*) AS error_num FROM log
                 WHERE status LIKE '40%' GROUP BY log_date) AS error_log,
                (SELECT time::date as log_date, COUNT(*) AS views_num FROM log 
                GROUP BY log_date) AS total_log
                WHERE total_log.log_date = error_log.log_date
                AND ROUND(((error_log.error_num * 100.0) / total_log.views_num), 3) > 1
                ORDER BY error_per desc;"""
    c.execute(query)
    popular_authors = c.fetchall()
    db.close()
    return popular_authors



def print_result(rows, str_val):
    for r in rows:
        print(str(r[0]) + ' - ' + str(r[1]) + ' ' + str_val)



print('Q1: What are the most popular three articles of all time?')
print_result(most_popular_articles(), 'views')



print('Q2: Who are the most popular article authors of all time?')
print_result(most_popular_authors(), 'views')



print('Q3: On which days did more than 1% of requests lead to errors?')
print(requests_errors()[0][0].strftime('%B %d, %Y') + ' - ' + str(requests_errors()[0][1]) + '% errors')
