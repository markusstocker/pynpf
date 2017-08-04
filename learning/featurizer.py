from datetime import datetime
from sklearn.decomposition import TruncatedSVD


def featurize(data):
    h = data[0]  # header
    d = data[1:len(data)]  # measurements
    t = []  # times
    m = []  # matrix

    for r in d:
        t.append(datetime(int(r[0]), int(r[1]), int(r[2]), int(r[3]), int(r[4]), int(r[5])))
        del r[0:6]  # remove datetime
        r = [float(i) for i in r]  # convert data matrix to numbers
        m.append(r)

    svd = TruncatedSVD(n_components=1)

#    dtidx = daytimeindex(t)
#    dtot = total(m)
#    dttot = total(m[dtidx[0]:dtidx[1]])
#    ntot = total(newparticles(m))
#    dtntot = total(newparticles(m[dtidx[0]:dtidx[1]]))

    # Transposes the matrix first
    return svd.fit_transform(list(map(list, zip(*m))))


# Computes the start and end index of daytime (6 am - 6 pm)
def daytimeindex(t):
    sidx = -1
    eidx = -1
    idx = -1

    for dt in t:
        idx = idx + 1
        h = dt.time().hour
        if sidx == -1 and h >= 6:
            sidx = idx
        if eidx == -1 and h >= 18:
            eidx = idx

    return [sidx, eidx]


def total(m):
    return sum([sum(i) for i in zip(*m)])


# Extracts the data for particles < 10 nm
def newparticles(m):
    n = []
    # Take the first 10 columns
    for r in m:
        n.append(r[0:10])
    return n

