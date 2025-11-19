import redis
import psycopg2
import time

r = redis.Redis(host='redis', port=6379, db=0)

conn = psycopg2.connect(
    host="db",
    database="wordcount",
    user="user",
    password="pass"
)
cur = conn.cursor()

def count_words(text):
    return len(text.split())

while True:
    text = r.rpop('texts')  # Get text from Redis list
    if text:
        text = text.decode('utf-8')
        word_count = count_words(text)
        cur.execute("INSERT INTO results (text, word_count) VALUES (%s, %s)", (text, word_count))
        conn.commit()
        print(f"Processed: {text} -> {word_count} words")
    else:
        time.sleep(1)
