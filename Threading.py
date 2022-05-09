import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done sleeping {seconds}...'


with concurrent.futures.ThreadPoolExecutor() as executor:
    #using map function
    secs = [5,4,3,2,1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)
    # #use list comprihention
    # secs = [5, 4, 3, 2, 1]
    # results = [executor.submit(do_something, sec) for sec in secs]

    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

# #an empty list to store the threads
# threads = []

# for _ in range(10):
#     t = threading.Thread(target=do_something)
#     t.start()
#     threads.append(t)

# #join function to run concurrently
# for thread in threads:
#     thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')