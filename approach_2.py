import sys
from flask import Flask, json, request
import requests

app = Flask(__name__)

# --------- GLOBALS ---------
ORG_NAME = sys.argv[1]  # GitHub organization name
URL = "https://api.github.com/orgs/%s/repos?page=%d"  # When %s will be the organization name


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


def pagination_handler(repos, phrase):
    """
    This function handel one page only
    :param repos: response.json() of the repository
    :param phrase: a given phrase
    :return: a list of the requested information
    """
    matching_repos = []

    for repo in repos:
        if phrase is not None and phrase in repo["name"].lower():
            temp_dic = get_data(repo)
        elif phrase is None:
            temp_dic = get_data(repo)
        else:  # for the case that we have phrase but don't need to show it
            continue
        matching_repos.append(temp_dic)
    return matching_repos


@app.route("/")
def get_repositories():
    try:
        if len(sys.argv[2]) >= 3:
            phrase = sys.argv[2]
        else:
            phrase = None   # if the given phrase is less than 3 letters so show all
    except:
        phrase = None

    page = int(request.args.get("page", 1))  # Get the page number from query parameter, default to 1
    url = URL % (ORG_NAME, page)
    response = requests.get(url)

    if response.status_code == 200:
        all_repos = []  # To store repositories from all pages
        while response.status_code == 200:  # Continue while there are more pages
            repos = response.json()
            all_repos.append(repos)

            # Check if there's another page
            if 'next' in response.links:
                url = response.links['next']['url']
                response = requests.get(url)
            else:
                break   # if no other pages

        data = *map(pagination_handler, all_repos, [phrase] * len(all_repos)),

        formatted_json = json.dumps(data, indent=4)  # Format the JSON with indentation
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
