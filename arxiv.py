"""Arxiv related helper functions
"""
import re
from urllib.parse import urlparse

pattern = "[0-9]*\.[0-9]*"
def find_index(in_str: str):
    index = None

    if "arxiv.org" in in_str:
        index = url_to_index(in_str)
    elif re.match(pattern, in_str):
        index = in_str
    elif ":" in in_str:
        # deal with format:  arXiv:1909.03460
        index = in_str.split(":")[-1]
    else:
        print(f"{in_str} is unknown.")

    return remove_version(index)

def url_to_index(url: str):
    o = urlparse(url)
    if o.netloc != "arxiv.org":
        print(f"invalid arxiv url: {url}")
        return None

    paths = o.path.split('/')
    index = paths[2] if paths[1] == 'abs' else paths[2][:-4]

    return index

def remove_version(index):
    if index is None:
        return index
    pp = "v[0-9]*"
    if re.search(pp, index) is not None:
        idx = index.find('v')
        index = index[:idx]
    return index


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='')
    add_arg = parser.add_argument
    # add_arg('', help='')
    
    args = parser.parse_args()
    
    url = "https://arxiv.org/abs/1909.03460v1"
    print(url_to_index(url))

    url = "https://arxiv.org/pdf/1909.03460.pdf"
    print(url_to_index(url))

    print(find_index("arxiv:1909.03460"))

    print(find_index("1909.03460v2"))

    print(find_index("1909.03460"))

    print(find_index("190x9.03460"))