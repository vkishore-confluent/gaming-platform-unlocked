import os.path

f = open(os.path.dirname(__file__) + '/../files/credentials.txt')

for line in f.readlines():
    if (line.split(' = ')[0]) == 'cluster_bootstrap':
        cluster_bootstrap = line.split(' = ')[1].strip()
    elif (line.split(' = ')[0]) == 'cluster_api_key':
        cluster_api_key = line.split(' = ')[1].strip()
    elif (line.split(' = ')[0]) == 'cluster_api_secret':
        cluster_api_secret = line.split(' = ')[1].strip()
    elif (line.split(' = ')[0]) == 'schemaregistry_url':
        schemaregistry_url = line.split(' = ')[1].strip()
    elif (line.split(' = ')[0]) == 'schemaregistry_api_key':
        schemaregistry_api_key = line.split(' = ')[1].strip()
    elif (line.split(' = ')[0]) == 'schemaregistry_api_secret':
        schemaregistry_api_secret = line.split(' = ')[1].strip()

print(cluster_bootstrap, 
        cluster_api_key, 
        cluster_api_secret, 
        schemaregistry_url,
        schemaregistry_api_key,
        schemaregistry_api_secret)