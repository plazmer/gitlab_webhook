settings = {}

for row in open('settings.tsv', 'r'):
    repo, email, tg_id = row.split("\t")
    if not settings.get(repo):
        settings[repo] = []
    settings[repo].append(tg_id)
