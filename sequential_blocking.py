import os
import numpy as np
import re
import falcon
from redis import Redis
from redisworks import Root
from exact_blocking import exact_blocking

# get credentials to redis datastore
url = os.environ.get('REDIS_URL')
host = re.findall('@(.*):', url)[0]
port = re.findall('[0-9]+$', url)[0]
pw = re.findall('h:(.*)@', url)[0]

class Treatment:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        # get covariates to block on; extend and rename as needed
        cov1 = int(req.params['cov1'])
        cov2 = int(req.params['cov2'])
        covs = [cov1, cov2]

        # get existing covariate profile for observations already assigned
        # treatment from redis
        conn = Redis(host=host, port=port, password=pw)
        root = Root(conn=conn)
        dataID = 'data' # name of redis list where profile is stored; rename as needed
        data = root[dataID]

        # assign treatment
        ntr = 4 # number of treatment groups; change as needed
        tr, data = exact_blocking(covs, ntr, data) # replace if needed

        root[dataID] = data # save new covariate profile to redis
        resp.body = 'Treatment=' + str(tr) # return treatment group

app = falcon.API()
app.add_route('/treatment', Treatment())