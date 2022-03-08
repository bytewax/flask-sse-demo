from uuid import uuid4
from datetime import datetime
import json

from flask import Flask
from flask_sse import sse

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/stream')


@app.route('/event/<action>')
def event(action):
    user_id = uuid4()
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    sse.publish(data=json.dumps(f'user_id: {user_id}, timestamp: {timestampStr}'), type=action)
    return {}, 200