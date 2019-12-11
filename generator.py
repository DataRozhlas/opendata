#%%
import yaml
import datetime
import json

#%%
with open('datasets.yaml', 'r', encoding='utf-8') as f:
    sets = yaml.safe_load(f)

#%%
sets

# %%
with open('./api/package_list.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps({
            'success': True,
            'result': list(map(lambda x: x['uid'], sets))
        }, ensure_ascii=False))
# %%
for dset in sets:
    with open('./api/' + dset['uid'] + '.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps({
            'success': True,
            'result': dset
        }, ensure_ascii=False))

# %%
