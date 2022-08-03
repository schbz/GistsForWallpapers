# find the github gist ids in the README.md file, and use them to create a backup of the files in the gists in a directory called 'backup'

import os
import requests


def backup():

    # get the github gist IDs between the [ ] from the README.md file
    gist_ids = []
    with open("README.md", "r") as readme:
        for line in readme:
            if "[" in line:
                gist_ids.append(line.split("[")[1].split("]")[0])
    
    #remove the links
    gist_ids = gist_ids[2:]
    print("downloading: ", gist_ids)
    
    #create a directory called 'backup' if it doesn't already exist
    if not os.path.exists("backup"):
        os.mkdir("backup")

    # get the directory path
    directory_path = os.path.join(os.getcwd(), "backup")

    # iterate over the gist IDs
    for gist_id in gist_ids:
        # get the gist url
        gist_url = "https://api.github.com/gists/" + gist_id

        # get the gist data
        gist_data = requests.get(gist_url).json()
        
        # get the files from the gist
        files = gist_data["files"]

        # iterate over the files
        for file_name, file_data in files.items():
            file_url = file_data["raw_url"]
            file_data = requests.get(file_url).text
            file_path = os.path.join(directory_path, file_name)
            file = open(file_path, "w", encoding="utf-8")
            file.write(file_data)
            file.close()


    print("Gists saved locally at Directory path: " + directory_path)
    
    
backup()
