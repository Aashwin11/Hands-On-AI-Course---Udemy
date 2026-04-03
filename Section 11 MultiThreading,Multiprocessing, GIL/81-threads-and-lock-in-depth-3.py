import requests
import threading, time


def download(url):
    print(f"Starting download:{url}.......")
    response=requests.get(url)
    print(f"Finished downloading from :{url} and size:{len(response.content)} bytes")

urls=[
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg"
] 

start=time.time()
threads=[]

for url in urls:
    t=threading.Thread(target=download,args=(url,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end=time.time()

print(f"Completion time:{end-start:.2f}")