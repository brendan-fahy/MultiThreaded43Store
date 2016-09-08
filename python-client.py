from multiprocessing.dummy import Pool as ThreadPool 

def store(fortyThree):
    with open('43.txt', 'a') as f:
        f.write(fortyThree)

fortyThreeToStore = ["43", "43", "43", "43", "43", "43"]

multiThreadPool = ThreadPool(4) 
results = multiThreadPool.map(store, fortyThreeToStore)
multiThreadPool.close() 
multiThreadPool.join() 



