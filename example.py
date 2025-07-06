import sys
import requests
import os

# イシュー番号をコマンドライン引数から取得
issue_number = sys.argv[1]

# GitHub API用の情報
repo_owner = 'あなたのGitHubユーザー名'
repo_name = 'あなたのリポジトリ名'
token = os.environ['GITHUB_TOKEN']  # GitHub Actionsにデフォルトで渡されているトークン

# コメント投稿用API
url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/issues/{issue_number}/comments'

headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

data = {
    'body': f'This is an automated comment on issue #{issue_number} 🚀'
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
    print('✅ Successfully commented on the issue!')
else:
    print(f'❌ Failed with status code: {response.status_code}')
    print(response.json())

