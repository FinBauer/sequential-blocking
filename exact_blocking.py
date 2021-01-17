import numpy as np

def exact_blocking(covs, ntr, data):
    """Performs exact blocking on covariates

    Args:
        covs (list): Covariate profile of current observation
        ntr (int): Number of treatment groups
        data (list): Covariate-treatment profile of past observations
            If no past covariates, pass None
            Else, must be list of 2, where first entry is list containing
            all unique past covariates profiles and second entry is list
            containing treatment profiles for each covariate profile. Each
            treatment profile is list of length ntr with number of observations
            assigned to each treatment group

    Returns:
        int : Treatment group assigned to current observation
        list : Updated covariate-treatment profile including current observation
    """
    if data == None:
        data = [[covs], [[0] * ntr]]
        tr = np.random.choice(range(ntr))
        data[1][0][tr] += 1
    else:
        try:
            i = data[0].index(covs)
            matches = np.where(np.array(data[1][i]) == min(data[1][i]))[0]
            tr = int(np.random.choice(matches))
            data[1][i][tr] += 1
        except ValueError:
            data[0].append(covs)
            trs = [0] * ntr
            tr = int(np.random.choice(range(ntr)))
            trs[tr] += 1
            data[1].append(trs)
    return tr, data