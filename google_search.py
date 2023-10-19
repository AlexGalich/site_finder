from googlesearch import search
import random

import time

# Perform the Google search and get the results

def get_google_link(query):
    time.sleep(random.randint(1,5))
    search_results = search(query,timeout=5, sleep_interval=5)

    # Iterate through the search results and print the first link
    for link in search_results:

       # print("First Link:", link)
        return link  # Exit the loop after printing the first link
    




