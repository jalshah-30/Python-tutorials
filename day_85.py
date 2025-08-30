'''Creating command line utility in python'''

import argparse
import requests

# def download_file(url,local_filename):
#     local_filename = output
#     # NOTE the stream=True parameter below
#     with requests.get(url, stream=True) as r:
#         r.raise_for_status()
#         with open(local_filename, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=8192): 
#                 # If you have chunk encoded response uncomment if
#                 # and set chunk_size parameter to None.
#                 #if chunk: 
#                 f.write(chunk)
#     return local_filename

parser = argparse.ArgumentParser()

parser.add_argument("url",help="URL of the file, to download")
parser.add_argument("output",help="name of the file")
# parser.add_argument("--o","--output",help="optional",default=None)

args=parser.parse_args()

print(args.output)
print(args.url)


def download_file(url,local_filename):
    
    local_filename = args.output
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename

download_file(args.url,args.output)