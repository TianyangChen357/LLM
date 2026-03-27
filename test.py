import requests

# URL of the file to download
url = "https://www.dropbox.com/scl/fi/rz1nrldgipsh9wsefts0k/DeepPipe_Fine_Tune_Report_20260227.docx?rlkey=vei8t31hl5hwcpmsv7a3bkmws&st=tyyzacjf&dl=0"

# Send a GET request to the URL
response = requests.get(url, allow_redirects=True)

# Open a local file with write-binary permission
with open("DeepPipe_Fine_Tune_Report_20260227.docx", "wb") as file:
    file.write(response.content)

print("File downloaded successfully!")
