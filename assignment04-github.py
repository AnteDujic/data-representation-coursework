from github import Github
import requests
from config import config as cfg

# Assign the apikey (token)
apiKey = cfg["githubkey"]
g = Github(apiKey)

# Assign the repo to work with
repo = g.get_repo("AnteDujic/data-representation-coursework")

# Get the url for the file
fileInfo = repo.get_contents("andrew.txt")
urlOfFile = fileInfo.download_url

# Get contents of the file
response = requests.get(urlOfFile)
contentOfFile = response.text
# print(contentOfFile)

# Replace contents of the file ("Andrew" => "Ante")
updatedContents = contentOfFile.replace("Andrew", "Ante")
# updatedContents = contentOfFile.replace("Ante", "Andrew")
# print(updatedContents)

# Push the updated file
gitHubResponse = repo.update_file(fileInfo.path, "Change names", updatedContents, fileInfo.sha)
print(gitHubResponse)