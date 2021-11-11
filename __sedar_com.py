import time
import json
from sedar_com import *

if __name__ == '__main__':
    start_time = time.time()

    a = Handler()

    final_data = a.Execute('aHR0cHM6Ly93d3cuc2VkYXIuY29tL0Rpc3BsYXlQcm9maWxlLmRvP2xhbmc9RU4maXNzdWVyVHlwZT0wMyZpc3N1ZXJObz0wMDA1MjA5Mw==', 'overview', '', '')
    print(json.dumps(final_data, indent=4))

    elapsed_time = time.time() - start_time
    print('\nTask completed - Elapsed time: ' + str(round(elapsed_time, 2)) + ' seconds')
