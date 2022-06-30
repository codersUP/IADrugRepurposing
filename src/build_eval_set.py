
def build_data(path):
    with open(path, 'r') as fp:
        raw_data = fp.read()

    data = raw_data.split('\n')
    heading = data[0].split('\t')
    data = data[1:]

    drugs = {}
    for info in data:
        drug_info = info.split('\t')
        drug, drug_info = drug_info[0], drug_info[1:]
        drugs[drug] = {}
        for i, item in enumerate(drug_info, 1):
            if i == len(drug_info): continue
            drugs[drug][heading[i]] = item
    
    return drugs

def get_id_from_url(url):
    return url.split('/')[-1]

def get_db_ids(data):
    ids = []
    for drug in data:
        try:
            url = data[drug]['DrugBank']
            ids.append(get_id_from_url(url))
        except KeyError:
            pass
    
    return ids
