import requests

class Bitbucket:
    auth = None
    def __init__(self, auth=None, config=None, proxies=None):
        self.auth = auth
        self.config = config
        self.proxies = proxies

    def get_repository(self, name, workspace) ->  requests.Response:
        url=f"https://api.bitbucket.org/2.0/repositories/{workspace}/{name}"
        r = requests.get(url=url, auth=self.auth, proxies=self.proxies)
        return r

    def create_repository(self, name, project, workspace):
        url=f"https://api.bitbucket.org/2.0/repositories/{workspace}/{name}"
        body = {
                "scm": "git",
                "is_private": "true",
                "project": {
                    "key": project
                    }
                }
        r = requests.post(url=url, json=body, auth=self.auth, proxies=self.proxies)
        if not r.ok:
            print(f"Failed to create {workspace}/{name}")
            print(r.text)


    def get_repository_branch_permission(self, name, workspace):
        url=f"https://api.bitbucket.org/2.0/repositories/{workspace}/{name}/branch-restrictions"
        r = requests.get(url=url , auth=self.auth, proxies=self.proxies)

    def set_repository_branch_permission(self, name, workspace, branch, permission):
        print(f"Setting branching permissions: {permission}")
        url=f"https://api.bitbucket.org/2.0/repositories/{workspace}/{name}/branch-restrictions"
        body = {
                "pattern": branch,
                "type": "branchrestriction",
                **permission}

        r = requests.post(url=url, json=body, auth=self.auth, proxies=self.proxies)
        if not r.ok:
            print("Failed to configure branch permissions")
            print(r.text)

    def set_repository_branch_model(self, name, workspace, model):
        print("Setting branching model")
        url=f"https://api.bitbucket.org/2.0/repositories/{workspace}/{name}/branching-model/settings"
        r = requests.put(url=url, json=model , auth=self.auth, proxies=self.proxies)
        if not r.ok:
            print("Failed to configure branching model")
            print(r.text)

    def create_empty_commit(self, name, workspace, branch, message):
        url=f"https://api.bitbucket.org/2.0/repositories/{workspace}/{name}/src"

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        r = requests.post(
                url=url,
                headers=headers,
                data={"message": message, "branch": branch},
                auth=self.auth,
                proxies=self.proxies)

        if not r.ok:
            print("Failed to create empty commit")
            print(r.text)

    def create_branch(self, name, workspace, branch):
        url=f"https://api.bitbucket.org/2.0/repositories/{workspace}/{name}/refs/branches"
        body = {
                "name" : branch,
                "target" : {
                    "hash" : "refs/heads/main",
                    }
                }
        r = requests.post(url=url, json=body, auth=self.auth, proxies=self.proxies)
        if not r.ok:
            print(f"Failed to create {branch}")
            print(r.text)

    def enable_pipelines(self, name, workspace):
        url=f"https://api.bitbucket.org/2.0/repositories/{workspace}/{name}/pipelines_config"

        body = {
                "enabled": True,
                }

        r = requests.put(url=url, json=body, auth=self.auth, proxies=self.proxies)
        if not r.ok:
            print("Failed to enable pipeline")
            print(r.text)



    def get_uuid_for_environment(self, name, workspace, environment):
        url=f"https://api.bitbucket.org/2.0/repositories/{workspace}/{name}/environments/"

        r = requests.get(url=url, auth=self.auth)
        for value in r.json()['values']:
            if value['slug'] == environment:
                return value['uuid']
        if not r.ok:
            print("Failed to fetch deployment environments")
            print(r.text)


    def set_deployment_environment_variable(self, name, workspace, uuid, key, value, is_secure):
        url=f"https://api.bitbucket.org/2.0/repositories/{workspace}/{name}/deployments_config/environments/{uuid}/variables"

        body = {
                "key": key,
                "value": value,
                "secured": is_secure
                }

        r = requests.post(url=url, json=body, auth=self.auth, proxies=self.proxies)
        if not r.ok:
            print("Failed to set deployment environment variable")
            print(r.text)

    def create_report(self, title, details, report_type, report_id, reporter, result, link, data, bitbucket_workspace, bitbucket_repo_slug, bitbucket_commit):
        url=f"http://api.bitbucket.org/2.0/repositories/{bitbucket_workspace}/{bitbucket_repo_slug}/commit/{bitbucket_commit}/reports/{reporter}-{report_id}"
        body = {
                "title": title,
                "details": details,
                "report_type": report_type,
                "reporter": reporter,
                "link": link,
                "result": result,
                "data": data
                }
        r = requests.put(url=url, json=body, auth=self.auth, proxies=self.proxies)
        if not r.ok:
            print(f"Failed to create report {title}")
            print(r.text)

    def create_annotation(self, title, summary, severity, path, line, reporter, report_id, annotation_type, annotation_id, bitbucket_workspace, bitbucket_repo_slug, bitbucket_commit):
        url=f"http://api.bitbucket.org/2.0/repositories/{bitbucket_workspace}/{bitbucket_repo_slug}/commit/{bitbucket_commit}/reports/{reporter}-{report_id}/annotations/{reporter}-{annotation_id}"
        body = {
                "title": title,
                "annotation_type": annotation_type,
                "summary": summary,
                "severity": severity,
                "path": path,
                "line": line
                }
        r = requests.put(url=url, json=body, auth=self.auth, proxies=self.proxies)
        if not r.ok:
            print(f"Failed to create annotation {title}")
            print(r.text)
