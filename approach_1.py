import sys
import github
import pandas as pd

LIST_REP = []  # each item in format {name: , owner: , url: , creation time: , number of stars:, }


def get_repositories(org, phrase=None):
    """
    :param org: String -> the name of the organization
    :param phrase: String -> a given phrase
    :return: None -> creating a csv file in the directory
    """
    g = github.Github()
    user = g.get_organization(org)
    for repo in user.get_repos():
        if phrase is not None and phrase in repo.name.lower():
            temp_dic = {"Name": repo.name, "Owner": repo.owner.login, "URL": repo.url, "Creation Time": repo.created_at,
                        "Number of stars": repo.stargazers_count}
        elif phrase is None:
            temp_dic = {"Name": repo.name, "Owner": repo.owner.login, "URL": repo.url, "Creation Time": repo.created_at,
                        "Number of stars": repo.stargazers_count}
        else:
            continue
        LIST_REP.append(temp_dic)

    new = pd.DataFrame.from_dict(LIST_REP)
    pd.set_option('display.max_colwidth', 30)
    new.to_csv("data.csv", index=False)


if __name__ == "__main__":
    try:    # if a phrase is given
        get_repositories(org=sys.argv[1], phrase=sys.argv[2])
    except: # if only the organization is given
        get_repositories(org=sys.argv[1])


