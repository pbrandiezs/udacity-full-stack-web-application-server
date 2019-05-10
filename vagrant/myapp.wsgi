import psycopg2

def query_db(sql):
    db = psycopg2.connect("dbname=www-db")
    cur = db.cursor()
    cur.execute(sql)
    RESULTS = cur.fetchall()
    cur.close()
    db.close()
    return RESULTS

def application(environ, start_response):
    sql = """
    SELECT body 
    FROM articles
    LIMIT 1;
    """
    
    for Result in query_db(sql):
        output = Result[0]

    
    status = '200 OK'
    # output = 'Hello Udacity!'

    response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
