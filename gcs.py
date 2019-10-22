from googleapiclient.discovery import build


class GCSBuildClient(object):
    def __init__(self, project_id):
        self.service = build('cloudbuild', 'v1', cache_discovery=False)
        self.project_id = project_id

    def run_trigger(self, trigger_id, commit_sha):
        body = {
            "commitSha": commit_sha,
            "projectId": self.project_id,
        }
        req = self.service.projects().triggers().run(projectId=self.project_id, triggerId=trigger_id, body=body)
        return req.execute()

    def list_triggers(self):
        req = self.service.projects().triggers().list(projectId=self.project_id)
        return req.execute()
