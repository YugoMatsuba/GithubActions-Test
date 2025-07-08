import sys
import requests
import os

# イシュー番号をコマンドライン引数から取得
issue_number = sys.argv[1]

# GitHub API用の情報
repo_owner = 'YugoMatsuba'
repo_name = 'GithubActions-Test'
token = os.environ['GITHUB_TOKEN']  # GitHub Actionsにデフォルトで渡されているトークン

# コメント投稿用API
url_comment = f'https://api.github.com/repos/{repo_owner}/{repo_name}/issues/{issue_number}/comments'

# イシューデータ取得用API
url_issue = f'https://api.github.com/repos/{repo_owner}/{repo_name}/issues/{issue_number}'

headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

issue_data = requests.get(url_issue, headers=headers)
response = requests.post(url_comment, headers=headers, json=issue_data)

if response.status_code == 201:
    print('✅ Successfully commented on the issue!')
else:
    result = 10 / 0

