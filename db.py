settings = []

for row in open('settings.tsv', 'r'):
    try:
        repo, email, tg_id, kind = row.strip().split("\t")
        settings.append({"repo": repo, "email": email, "tg_id": tg_id, "kind": kind})
    except:
        pass


def get(repo, kind):
    response = []
    for i in settings:
        if (i.get("repo") == "*" or i.get("repo") == repo) and (i.get("kind") == "*" or i.get("kind") == kind):
            response.append(i.get("tg_id"))

    return set(response)
