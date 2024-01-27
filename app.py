import re
from flask import Flask, request, render_template
from main import process_query  # import the process_query function from your main.py file

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form['query']
        if user_input:
            result = process_query(user_input)
            # Search for the pattern and replace it with the desired HTML structure
            result = re.sub(r'```(.*?)```', r'<pre class="line-numbers"><code class="language-python">\1</code></pre>', result, flags=re.DOTALL)
            return render_template('index.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)