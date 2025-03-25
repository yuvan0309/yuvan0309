import requests
import numpy as np
import matplotlib.pyplot as plt
import os

USERNAME = "your-github-username"
TOKEN = os.getenv("GH_TOKEN")

headers = {"Authorization": f"token {TOKEN}"}

def get_github_stats():
    repos_url = f"https://api.github.com/users/{USERNAME}/repos"
    repos = requests.get(repos_url, headers=headers).json()
    
    total_commits = 0
    total_pull_requests = 0
    total_issues = 0
    total_reviews = 0

    for repo in repos:
        repo_name = repo['name']
        commits_url = f"https://api.github.com/repos/{USERNAME}/{repo_name}/commits"
        pulls_url = f"https://api.github.com/repos/{USERNAME}/{repo_name}/pulls?state=all"
        issues_url = f"https://api.github.com/repos/{USERNAME}/{repo_name}/issues?state=all"
        
        total_commits += len(requests.get(commits_url, headers=headers).json())
        total_pull_requests += len(requests.get(pulls_url, headers=headers).json())
        total_issues += len(requests.get(issues_url, headers=headers).json())

    # Simulating code review data (GitHub API does not provide direct code review counts)
    total_reviews = total_pull_requests * 0.5  # Assume half of PRs get reviewed

    return [total_reviews, total_issues, total_pull_requests, total_commits]

def create_radar_chart(stats):
    labels = ['Code Review', 'Issues', 'Pull Requests', 'Commits']
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    stats += stats[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, stats, color='lime', alpha=0.4)
    ax.plot(angles, stats, color='lime', linewidth=2)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, color="white")

    plt.savefig("github_activity.png", transparent=True)

stats = get_github_stats()
create_radar_chart(stats)
