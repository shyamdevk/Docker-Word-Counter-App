from flask import Flask
import psycopg2

app = Flask(__name__)

def get_results():
    conn = psycopg2.connect(
        host="db",
        database="wordcount",
        user="user",
        password="pass"
    )
    cur = conn.cursor()
    cur.execute("SELECT text, word_count FROM results ORDER BY id DESC LIMIT 10")
    rows = cur.fetchall()
    conn.close()
    return rows

@app.route('/')
def index():
    results = get_results()
    html = '''
        <html>
        <head>
            <title>Word Count Results</title>
            <style>
                body { font-family: Arial; background: #eaeaea; padding: 40px; text-align: center; }
                h1 { color: #333; }
                ul { list-style-type: none; padding: 0; }
                li {
                    background: white;
                    margin: 10px auto;
                    padding: 15px;
                    border-radius: 8px;
                    width: 60%;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                    font-size: 18px;
                }
                span { font-weight: bold; color: #007BFF; }
            </style>
        </head>
        <body>
            <h1>Recent Word Count Results</h1>
            <ul>
    '''
    for text, count in results:
        html += f'<li><span>{count} words</span>: {text}</li>'
    html += '''
            </ul>
        </body>
        </html>
    '''
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
