settings = {}

for row in open('settings.tsv', 'r'):
    try:
        repo, email, tg_id = row.split("\t")
        repo = repo.strip()
        tg_id = tg_id.strip()
        if not settings.get(repo):
            settings[repo] = []
        settings[repo].append(tg_id)
    except:
        pass
