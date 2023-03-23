def level_crawler(input_url):
    temp_urls = set() # Initialize an empty set to store the URLs found on the input page
    current_url_domain = urlparse(input_url).netloc # Extract the domain name from the input URL using the urlparse() function

    beautiful_soup_object = BeautifulSoup(
        requests.get(input_url).content, "lxml") # Use the requests library to download the HTML content of the input URL, and then use BeautifulSoup to parse the content

    for anchor in beautiful_soup_object.findAll("a"): # Find all <a> tags in the parsed HTML content
        href = anchor.attrs.get("href") # Extract the href attribute of the <a> tag
        if(href != "" or href != None): # Check if the href attribute is not empty or None
            href = urljoin(input_url, href) # Use urljoin() function to create an absolute URL from the relative URL found in href
            href_parsed = urlparse(href) # Use urlparse() function to parse the absolute URL
            href = href_parsed.scheme + "://" + href_parsed.netloc + href_parsed.path # Reconstruct the absolute URL from the parsed components
            final_parsed_href = urlparse(href) # Use urlparse() function to parse the reconstructed absolute URL
            is_valid = bool(final_parsed_href.scheme) and bool(final_parsed_href.netloc) # Check if the scheme and netloc attributes of the parsed URL are not empty
            if is_valid:
                if current_url_domain not in href and href not in links_extern: # Check if the domain of the parsed URL is different from the domain of the input URL, and if the URL has not already been added to the external links set
                    print("Extern - {}".format(href)) # Print the URL to the console
                    links_extern.add(href) # Add the URL to the external links set
                if current_url_domain in href and href not in links_intern: # Check if the domain of the parsed URL is the same as the domain of the input URL, and if the URL has not already been added to the internal links set
                    print("Intern - {}".format(href)) # Print the URL to the console
                    links_intern.add(href) # Add the URL to the internal links set
                    temp_urls.add(href) # Add the URL to the temporary set of URLs found on the input page

    return temp_urls # Return the set of URLs found on the input page
