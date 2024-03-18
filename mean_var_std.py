import numpy as np

def calculate(lists):
    if len(lists) == 9:
        x = np.array(lists)
        x = x.reshape(3, 3) 
        a = list(x.mean(axis=1))
        b = list(x.mean(axis=0))
        c = list(x.var(axis=1))
        e = list(x.std(axis=1))
        d = list(x.var(axis=0))
        f = list(x.std(axis=0))
        g = list(x.max(axis=1))
        h = list(x.max(axis=0))
        i = list(x.min(axis=1))
        j = list(x.min(axis=0))
        k = list(x.sum(axis=0))
        l = list(x.sum(axis=1))
        m = x.flatten().mean()
        n = x.flatten().var()
        o = x.flatten().std()
        p = x.flatten().max()
        q = x.flatten().min()
        r = x.flatten().sum()
        calculations = {
            'mean': [b, a, m],
            'variance': [d, c, n],
            'standard deviation': [f, e, o],
            'max': [h, g, p],
            'min': [j, i, q],
            'sum': [k, l, r]
        }

        return calculations
    else:
        raise ValueError("List must contain nine numbers.")