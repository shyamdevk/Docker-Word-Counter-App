from flask import Flask, request, redirect
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, db=0)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        r.lpush('texts', text)
        return redirect('/')

    return '''
        <html>
        <head>
            <title>Word Counter</title>
            <style>
                body { font-family: Arial; background: #f4f4f4; padding: 40px; text-align: center; }
                textarea { width: 400px; height: 120px; padding: 10px; font-size: 16px; }
                input[type=submit] {
                    padding: 10px 20px;
                    background-color: #007BFF;
                    color: white;
                    border: none;
                    cursor: pointer;
                    font-size: 16px;
                    border-radius: 5px;
                    margin-top: 10px;
                }
                h1 { color: #333; }
            </style>
        </head>
        <body>
            <h1>Word Counter App</h1>
            <form method="post">
                <textarea name="text" placeholder="Enter a sentence..."></textarea><br>
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
