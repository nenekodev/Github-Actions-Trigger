import requests
import json
import os

def run():
    GH_TOKEN = os.environ.get('GITHUB_TOKEN')
    GH_USER = os.environ.get('GITHUB_USER')
    GH_REPO = os.environ.get('GITHUB_REPO')
    GH_BRANCH =  os.environ.get('GITHUB_BRANCH')
    GH_ACTION =  os.environ.get('GITHUB_ACTION_FILE')

    header = {'Authorization': f'token {GH_TOKEN}',
                "Accept": "application/vnd.github.v3+json"}

    # run workflow
    requests.post(
        f'https://api.github.com/repos/{GH_USER}/{GH_REPO}/actions/workflows/{GH_ACTION}/dispatches',
        data = json.dumps({"ref": GH_BRANCH }), headers = header)
    
    # delete workflow runs
    runsListJson = requests.get(
        f'https://api.github.com/repos/{GH_USER}/{GH_REPO}/actions/runs',
        headers = header)
    runsList = json.loads(runsListJson.content)
    workflowList = runsList['workflow_runs']

    for x in range(len(workflowList)):
        if workflowList[x]['conclusion'] == 'success':
            completedNum = workflowList[x]['id']
            deleteUrl = f'https://api.github.com/repos/{GH_USER}/{GH_REPO}/actions/runs/{str(completedNum)}'
            requests.delete(
                deleteUrl,
                headers = header)

# SCF handler
def main_handler(event, context):
    return run()
