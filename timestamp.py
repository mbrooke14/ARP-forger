from time import time

t_0 = time()
def stamp(p=4): return f"[{round(time() - t_0, p)}s]"
