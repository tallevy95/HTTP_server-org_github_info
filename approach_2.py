import sys
from flask import Flask, json
import requests

app = Flask(__name__)

# --------- GLOBALS ---------
ORG_NAME = sys.argv[1]  # GitHub organization name
URL = "https://api.github.com/orgs/%s/repos"  # When %s will be the organization name


# --------- functions ---------
def get_data(repository):
    """
    Saving the data in a dict
    :param repository: Object of type Repository
    :return: dict type
    """
    data = {"Name": repository["name"], "Owner": repository["owner"]["login"], "URL": repository["url"],
            "Creation Time": repository["created_at"],
            "Number of stars": repository["stargazers_count"]}
    return data


@app.route("/")
def get_repositories():
    url = URL % ORG_NAME
    response = requests.get(url)
    try:
        if len(sys.argv[2]) >= 3:
            phrase = sys.argv[2]
        else:
            phrase = None   # if the given phrase is less than 3 letters so show all
    except:
        phrase = None

    if response.status_code == 200:
        # page = int(request.args.get('page', 1))
        # per_page = int(request.args.get('per_page', 100))  # Number of repositories per page
        # print(per_page)
        # start_idx = (page - 1) * per_page
        # end_idx = start_idx + per_page

        repos = response.json()
        matching_repos = []
        for repo in repos:
            if phrase is not None and phrase in repo["name"].lower():
                temp_dic = get_data(repo)
            elif phrase is None:
                temp_dic = get_data(repo)
            else:   # for the case that we have phrase but don't need to show it
                continue
            matching_repos.append(temp_dic)
        # repos_to_return = matching_repos[start_idx:end_idx]
        formatted_json = json.dumps(matching_repos, indent=4)  # Format the JSON with indentation
        data = app.response_class(
            response=formatted_json,        # the json formatted data
            status=200,                     # OK
            mimetype='application/json'     # make the data easier to read
        )
        return data
    else:
        return "Error fetching repository information", 500


if __name__ == "__main__":
    app.run()
