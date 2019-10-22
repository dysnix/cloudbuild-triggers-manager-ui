import re
import settings
from gcs import GCSBuildClient
from flask import Flask, request, render_template

app = Flask(__name__)
build = GCSBuildClient(settings.PROJECT_ID)


@app.route('/', methods=['GET', 'POST'])
def index():
    triggers = []
    for trigger in build.list_triggers()['triggers']:
        if re.search(settings.TRIGGERS_FILTER_REGEX, trigger['description']):
            triggers.append(trigger)

    if request.method == 'POST':
        trigger_id = request.form['trigger_id']
        commit_hash = request.form['commit_hash']

        try:
            status = build.run_trigger(trigger_id, commit_hash)['metadata']['build']['status']
            error = None
        except Exception as exc:
            status = 'ERROR'
            error = str(exc)

        return render_template('index.html', triggers=triggers, status=status, error=error, trigger_id=trigger_id,
                               commit_hash=commit_hash)
    else:
        return render_template('index.html', triggers=triggers)
