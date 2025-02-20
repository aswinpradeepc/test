import requests
import time

# Set your GitHub personal access token
TOKEN = "your_token" 

# Set repository details
REPO_OWNER = "sunithvs"
REPO_NAME = "devb.io"

# GitHub API Headers
HEADERS = {"Authorization": f"token {TOKEN}"}


def get_stargazers(repo_owner, repo_name):
    """Fetches stargazers from a given GitHub repository."""
    stargazers = []
    page = 1

    while True:
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/stargazers?page={page}&per_page=100"
        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            print(f"Error fetching stargazers: {response.json()}")
            break

        data = response.json()
        if not data:
            break

        stargazers.extend(data)
        page += 1
        time.sleep(1)  # Avoid rate limits

    return [user["login"] for user in stargazers]


def get_user_emails(usernames):
    """Fetches emails from users' public commit events."""
    user_emails = {}

    for username in usernames:
        url = f"https://api.github.com/users/{username}/events/public"
        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            print(f"Error fetching events for {username}: {response.json()}")
            continue

        events = response.json()
        for event in events:
            if event["type"] == "PushEvent":
                for commit in event["payload"]["commits"]:
                    email = commit["author"].get("email")
                    if email and "noreply" not in email:
                        user_emails[username] = email
                        break
                if username in user_emails:
                    break

        time.sleep(1)  # Avoid rate limits

    return user_emails


if __name__ == "__main__":
    print("Fetching stargazers...")
    stargazers = get_stargazers(REPO_OWNER, REPO_NAME)
    print(f"Found {len(stargazers)} stargazers.")

    print("Fetching commit emails...")
    emails = get_user_emails(stargazers)

    print("\nGitHub Users with Emails:")
    for user, email in emails.items():
        print(f"{user}: {email}")
