# Extract the domain name from a URL
# https://www.codewars.com/kata/514a024011ea4fb54200004b

import re

def domain_name(url):
    match = re.search(r'^(https?://)?(www\.)?(?P<domain>[^\.]+)\.', url)
    return match['domain'] if match else ''
