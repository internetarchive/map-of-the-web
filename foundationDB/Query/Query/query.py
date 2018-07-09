import fdb
import json

fdb.api_version(520)
db = fdb.open()

def query(domain_name):
    value = db[fdb.Subspace(('domain-index', ))[domain_name]]
    if domain_name == "":
        return ""
    if value == None:
        result = "Not in database!"
        return result
    information = {}
    domain_index = {}
    value = db[fdb.Subspace(('domain-index', ))[domain_name]]
    domain_index[domain_name] = "domain-index"
    information["domain-index"] = bytes.decode(value)
    #information["archive"] = "2018-05-16"
    result = json.dumps(information, sort_keys = True, indent = 4, separators = {':', ', '})
    #result = str(result).replace(',', ', \n')
    #result = 'internet archive, create date:' + bytes.decode(value)
    print (result)
    return result

