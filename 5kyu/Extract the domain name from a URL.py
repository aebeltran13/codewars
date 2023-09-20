def domain_name(url):
    # Remove "http://" or "https://" if present
    if url.startswith("http://"):
        url = url[7:]
    elif url.startswith("https://"):
        url = url[8:]
    
    # Remove "www." prefix if it exists
    if url.startswith("www."):
        url = url[4:]
    
    # Find the first '/' character to isolate the domain
    slash_index = url.find("/")
    
    # Extract the domain part
    if slash_index != -1:
        domain = url[:slash_index]
    else:
        domain = url
    
    # Split the domain by '.' and return the first part
    domain_parts = domain.split(".")
    return domain_parts[0]