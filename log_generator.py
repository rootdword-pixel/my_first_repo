import subprocess

import requests


try:
    git_log = subprocess.check_output(
        ["git", "log", "-n", "5", "--pretty=format:%s"],
        text=True,
        encoding="utf-8",
    )

    prompt = (
        "Summarize these git commits into a professional bulleted list "
        f"for a CHANGELOG:\n{git_log}"
    )

    url = "http://localhost:11434/api/generate"
    data = {
        "model": "qwen2.5-coder:1.5b",
        "prompt": prompt,
        "stream": False,
    }

    print("AI is thinking...")
    response = requests.post(url, json=data, timeout=180)
    response.raise_for_status()

    summary = response.json().get("response", "Error: No response from AI.")

    with open("PROGRESS.md", "a", encoding="utf-8") as f:
        first_commit = git_log.splitlines()[0][:10] if git_log.splitlines() else "no-commits"
        f.write(f"\n## Update Summary ({first_commit}...)\n{summary}\n")

    print("PROGRESS.md updated successfully!")

except subprocess.CalledProcessError:
    print("Error: Are you in a Git repo? Run 'git init' first.")
except requests.exceptions.ConnectionError:
    print("Error: Ollama isn't running. Open the Ollama app first!")
except requests.exceptions.Timeout:
    print("Error: Ollama took too long to respond.")
