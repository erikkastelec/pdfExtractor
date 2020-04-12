class Documents:
    def __init__(self, path: str):
        self.num_docs = 0
        self.docs = []
        self.path = path


class Document:
    def __init__(self, path: str):
        self.author = None
        self.producer = None
        self.subject = None
        self.title = None
        self.path = path
        self.num_pages = None
        self.text = list()
        self.image = []
        self.table = []
        self.paragraphs = []
        self.table_of_contents = []
        self.page_layouts = []
        self.doc = None
        self.extractable = False

    def document_info_to_string(self):
        return "Author: " + self.author + "\n" \
               + "Producer: " + self.producer + "\n" \
               + "Subject: " + self.subject + "\n" \
               + "Title: " + self.title + "\n" \
               + "Number of Pages: " + str(self.num_pages)

    def table_of_contents_to_string(self):
        output_string = ""
        for tup in self.table_of_contents:
            output_string += str(tup[0]) + ': ' + tup[1] + '\n'
        return output_string
