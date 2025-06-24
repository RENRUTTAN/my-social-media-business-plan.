import os
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <html>
    <head>
        <title>AI-Powered Social Media Business Plan</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background-color: #f5f5f5; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 40px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { color: #333; text-align: center; }
            .btn { display: inline-block; background: #007bff; color: white; padding: 12px 24px; text-decoration: none; border-radius: 5px; margin: 10px 0; }
            .btn:hover { background: #0056b3; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>AI-Powered Social Media Business Plan</h1>
            <p>Welcome to your comprehensive business plan for starting an AI-powered social media posting service.</p>
            <p>This plan will help you achieve your goal of earning $1000/month by offering social media management services to businesses.</p>
            <a href="/business_plan" class="btn">View Complete Business Plan</a>
        </div>
    </body>
    </html>
    '''

@app.route("/business_plan")
def business_plan():
    with open("static/business_plan.html", "r") as f:
        html_content = f.read()
    
    # Add some basic styling to the business plan
    styled_content = f'''
    <html>
    <head>
        <title>AI-Powered Social Media Business Plan</title>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; background-color: #f9f9f9; }}
            .container {{ max-width: 1000px; margin: 0 auto; background: white; padding: 40px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
            h1 {{ color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }}
            h2 {{ color: #34495e; margin-top: 30px; }}
            h3 {{ color: #7f8c8d; }}
            ul {{ margin-left: 20px; }}
            li {{ margin-bottom: 5px; }}
            .back-btn {{ display: inline-block; background: #95a5a6; color: white; padding: 8px 16px; text-decoration: none; border-radius: 3px; margin-bottom: 20px; }}
            .back-btn:hover {{ background: #7f8c8d; }}
        </style>
    </head>
    <body>
        <div class="container">
            <a href="/" class="back-btn">← Back to Home</a>
            {html_content}
        </div>
    </body>
    </html>
    '''
    
    return styled_content

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


