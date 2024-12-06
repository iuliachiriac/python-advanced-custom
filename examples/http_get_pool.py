from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool as ProcessPool
import time

import requests


def get_url_resp(url):
    resp = requests.get(url)
    return len(resp.text)


urls = [
    'https://docs.python.org/3/whatsnew/3.13.html',
    'http://www.python.org/about/',
    'http://www.python.org/doc/',
    'http://www.python.org/download/',
    'http://www.python.org/getit/',
    'http://www.python.org/community/',
]

if __name__ == '__main__':
    d1 = time.time()
    syncres = [get_url_resp(url) for url in urls]
    # list(map(get_url_resp, urls))
    d2 = time.time()
    print(f'Serial result: {syncres}\nExecution time: {d2 - d1:.10f}\n')

    d1 = time.time()
    # make the Pool of thread workers
    pool = ThreadPool(7)

    # open the urls in their own threads
    # and return the results
    asyncres = pool.map(get_url_resp, urls)

    # close the pool and wait for the workers to finish
    pool.close()
    pool.join()

    d2 = time.time()

    print(f'Concurrent result (threads): {asyncres}\nExecution time: {d2 - d1:.10f}\n')

    d1 = time.time()
    # make the Pool of process workers
    pool = ProcessPool(7)

    # open the urls in their own processes
    # and return the results
    asyncres = pool.map(get_url_resp, urls)

    # close the pool and wait for the work to finish
    pool.close()
    pool.join()

    d2 = time.time()

    print(f'Concurrent result (processes): {asyncres}\nExecution time: {d2 - d1:.10f}\n')
