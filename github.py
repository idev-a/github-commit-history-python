import requests
from pandas import DataFrame
import pdb

from logger import logger

usernames = [
	'aave',
	'compound-finance'
]

ACCESS_TOKEN = '**********************'

class Github:
	commit_history = []

	def __init__(self):
		self.session = requests.Session()

	def get_headers(self):
		return {
			'Accept': 'application/vnd.github.v3+json',
			'content-type': "application/json",
			'authorization': f"token {ACCESS_TOKEN}"
		}

	def list_commits(self, username, repo):
		res = self.session.get(f'https://api.github.com/repos/{username}/{repo}/commits', headers=self.get_headers())
		if res.status_code == 200:
			for commit in res.json():
				_commit = commit['commit']
				self.commit_history.append({
					'timestamp': _commit['committer']['date'],
					'username': username,
					'repo': repo,
					'committer': _commit['committer']['email'],
				})
		else:
			logger.warning(f'^^^ cannot find out any commits for this repo {repo}')

	def list_repos(self):
		for username in usernames:
			res = self.session.get(f'https://api.github.com/users/{username}/repos', headers=self.get_headers())
			if res.status_code == 200:
				for repo in res.json():
					self.list_commits(username, repo['name'])

			else:
				logger.warning(f'^^^ cannot find out repos for user {username}')


	def convert2df(self):
		if self.commit_history:
			mydf = DataFrame(self.commit_history, columns=['timestamp', 'username', 'repo', 'committer'])
			mydf.to_csv('output.csv', index=False)


	def run(self):
		self.list_repos()
		self.convert2df()
					

if __name__ == '__main__':
	github = Github()
	github.run()