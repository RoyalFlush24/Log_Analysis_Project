#!/usr/bin/env python3

import psycopg2

# What are the most popular three articles of all time?
query1_title = ("What are the most popular three articles of all time?")
query1 = ("select articles.title, count(*) as views from articles "
          "join log on log.path like concat "
          "('%', articles.slug, '%') where log.status like '%200%' "
          "group by articles.title, log.path order by views desc limit 3")

# Who are the most popular article authors of all time?
query2_title = ("Who are the most popular article authors of all time?")
query2 = ("select authors.name, count(*) as views from articles "
          "join authors on articles.author = authors.id "
          "join log on log.path like concat('%', articles.slug, '%')"
          "where log.status like '%200%' group by authors.name "
          "order by views desc")

# On which days did more than 1% of requests lead to errors?
query3_title = ("On which days did more than 1% of requests lead to errors?")
query3 = ("select day, perc from (""select day, round((sum(requests)"
          "/(select count(*) from log where substring(cast "
          "(log.time as text), 0, 11) = day) * 100), 2) as perc from "
          "(select substring(cast(log.time as text), 0, 11) as day, "
          "count(*) as requests from log where status like '%404%' "
          "group by day) as log_percentage group by day "
          "order by perc desc) as final_query where perc >= 1")

# Connecting to the database to fetch the data I need.


def connect(database_name="news"):
    """Connect to the PostgreSQL database. Returns a database connection """
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print ('Unable to connect to the database')

# Get the results for my queries above


def get_query_results(query):
    """Return query results for given query """
    db, cursor = connect()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()

# Formating how I want my query results to print


def print_query_results(query_results):
    print (query_results[1])
    for index, results in enumerate(query_results[0]):
        print ('\t', index+1, '-->', results[0], '\t ---> ', str(results[1]),
               'views')


def print_error_results(query_results):
    print (query_results[1])
    for results in query_results[0]:
        print ('\t', results[0], '-->', str(results[1]) + '% errors!')

# Storing the results of the queries
if __name__ == '__main__':
    popular_articles_results = get_query_results(query1), query1_title
    popular_authors_results = get_query_results(query2), query2_title
    load_error_days = get_query_results(query3), query3_title

# Printing the results of the queries
    print_query_results(popular_articles_results)
    print_query_results(popular_authors_results)
    print_error_results(load_error_days)
