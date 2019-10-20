from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)


parser = MyHTMLParser()





class IDParser(HTMLParser):
    """Modified HTMLParser that isolates a tag with the specified id"""
    def __init__(self, id):
        self.id = id
        self.result = None
        self.started = False
        self.depth = {}
        self.html = None
        self.watch_startpos = False
        HTMLParser.__init__(self)
        
    def loads(self, html):
        self.html = html
        self.feed(html)
        self.close()
        
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if self.started:
            self.find_startpos(None)
        if 'id' in attrs and attrs['id'] == self.id:
            self.result = [tag]
            self.started = True
            self.watch_startpos = True
        if self.started:
            if not tag in self.depth: self.depth[tag] = 0
            self.depth[tag] += 1
            
    def handle_endtag(self, tag):
        if self.started:
            if tag in self.depth: self.depth[tag] -= 1
            if self.depth[self.result[0]] == 0:
                self.started = False
                self.result.append(self.getpos())
                
    def find_startpos(self, x):
        """Needed to put the start position of the result (self.result[1])
        after the opening tag with the requested id"""
        if self.watch_startpos:
            self.watch_startpos = False
            self.result.append(self.getpos())
    handle_entityref = handle_charref = handle_data = handle_comment = \
    handle_decl = handle_pi = unknown_decl = find_startpos
                
    def get_result(self):
        if self.result == None: return None
        if len(self.result) != 3: return None
        lines = self.html.split('\n')
        lines = lines[self.result[1][0]-1:self.result[2][0]]
        lines[0] = lines[0][self.result[1][1]:]
        if len(lines) == 1:
            lines[-1] = lines[-1][:self.result[2][1]-self.result[1][1]]
        lines[-1] = lines[-1][:self.result[2][1]]
        return '\n'.join(lines).strip()


def get_element_by_id(id, html):
    """Return the content of the tag with the specified id in the passed HTML document"""
    parser = IDParser(id)
    parser.loads(html)
    return parser.get_result()


