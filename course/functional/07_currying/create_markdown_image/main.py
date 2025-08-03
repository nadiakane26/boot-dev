def create_markdown_image(alt_text):
    def with_url(url):
        # Escape any parentheses in the URL by replacing them with encoded sequences. Enclose the url with parentheses (url).
        escaped_url = url.replace("(", "%28").replace(")", "%29")
    
        def with_title(title=None): # Optional title for the image.
            # Enclose the alt_text in square brackets prefixed with an exclamation point ![alt_text].
            image = f"![{alt_text}]({escaped_url})"
            if title: # If a title is passed
                # Enclose it in double quotes.
                title = f'"{title}"'
                # Add the quoted title to the image syntax by first removing the closing parenthesis ) from the end of the image syntax.
                # Add a space and the quoted title with a closing parenthesis ) to the end of the image syntax: ![alt_text](url "title")
                image = image[:-1] + f' {title})'
            return image
        return with_title
                
    return with_url