class News:
    def __init__(self, title, description, url, source):
        self.title = title
        self.description = description
        self.url = url
        self.source = source

    def formatted(self):
        return f"{self.title}\nRead more: {self.url}\n\n"
