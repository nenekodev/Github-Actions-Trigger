import requests
import json
import os

def run():
    payload = json.dumps({"ref": "master"})
    header = {'Authorization': 'token ' + os.environ.get('GITHUB_TOKEN'),
                "Accept": "application/vnd.github.v3+json"}
    requests.post(
        f'https://api.github.com/repos/' + os.environ.get('GITHUB_USER') + '/' + os.environ.get('GITHUB_REPO') + '/actions/workflows/' + os.environ.get('GITHUB_ACTION_FILE') + '/dispatches',
        data = payload, headers = header)
    
    # delete workflow runs
    runsListJson = requests.get(
        f'https://api.github.com/repos/' + os.environ.get('GITHUB_USER') + '/' + os.environ.get('GITHUB_REPO') + '/actions/runs',
        headers = header)
    runsList = json.loads(runsListJson.content)
    workflowList = runsList['workflow_runs']

    for x in range(len(workflowList)):
        if workflowList[x]['conclusion'] == 'success':
            completedNum = workflowList[x]['id']
            deleteUrl = 'https://api.github.com/repos/' + os.environ.get('GITHUB_USER') + '/' + os.environ.get('GITHUB_REPO') + '/actions/runs/' + str(completedNum)
            requests.delete(
                deleteUrl,
                headers = header)

# SCF entrance
def main_handler(event, context):
    return run()
