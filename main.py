from flask import Flask, json
import requests

app = Flask(__name__)

# --------- GLOBALS ---------
URL = "https://api.github.com/orgs/%s/repos?page=1"  # When %s will be the organization name

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
    if phrase is None:
        matching_repos = [get_data(repo) for repo in repos]
    else:
        matching_repos = [get_data(repo) for repo in repos if phrase.lower() in repo["name"].lower()]
    return matching_repos


@app.route("/org/<organization>/<phrase>")
@app.route("/org/<organization>")
def get_repositories(organization, phrase=None):
    url = URL % organization    # set the organization name
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
            mimetype='application/json'     # JSON response
        )
        return data
    else:
        return "Error fetching repository information", 500


if __name__ == "__main__":
    app.run()
