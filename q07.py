# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.handler = handler
        self.root = RouteTrieNode(self.handler)

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root
        self._insert(node, handler, path, 0)

    def _insert(self, node, handler, path, idx):
        if idx == len(path):
            return

        if path[idx] not in node.children:
            node.insert(path[idx])

        curr_node = node.children[path[idx]]

        if idx == len(path) - 1:  # leaf node
            curr_node.handler = handler

        self._insert(curr_node, handler, path, idx + 1)

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        curr_node = self.root

        for sub_path in path:
            if sub_path not in curr_node.children:
                return None
            else:
                curr_node = curr_node.children[sub_path]

        return curr_node.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = {}

    def insert(self, path):
        # Insert the node as before
        new_node = RouteTrieNode()

        self.children[path] = new_node


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root_handler = root_handler
        self.not_found_handler = not_found_handler
        self.routes = RouteTrie(self.root_handler)

    def add_handler(self, path, handler=None):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie

        splited_path = self.split_path(path)
        self.routes.insert(splited_path, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        if path == '' or path == '/':
            return self.routes.handler

        splited_path = self.split_path(path)

        result = self.routes.find(splited_path)

        if result is None:
            return self.not_found_handler
        else:
            return result

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here

        if path[-1] == '/':
            path = path[:-1]
        return path.split('/')


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# Edge Cases
print(router.lookup("/"))
# should print 'root handler'
print(router.lookup(""))
# should print 'root handler'
print(router.lookup("/home/about/"))
# should print 'about handler' 

print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one

# Other router
print('-----------------------------------------------------')
router.add_handler("/Sega/about", 'about Sega handler')
print(router.lookup("/Sega/about"))  # Should print about Sega handler
router.add_handler("/Sega/Video Games")
print(router.lookup("/Sega/Video Games"))  # Should print not Found handler
router.add_handler("/Sega/Video Games/Sonic", 'Sonic handler')
print(router.lookup("/Sega/Video Games/Sonic"))  # Should print Sonic handler
print(router.lookup("/Sega/Video Games/Sonic/"))  # Should print Sonic handler

print('-----------------------------------------------------')
router.add_handler("/Nintendo/about", 'about Nintendo handler')
print(router.lookup("/Nintendo/about"))  # Should print about Nintendo handler
router.add_handler("/Nintendo/Video Games")
print(router.lookup("/Nintendo/Video Games"))  # Should print not Found handler
router.add_handler("/Nintendo/Video Games/Mario", 'Mario handler')
print(router.lookup("/Nintendo/Video Games/Mario"))  # Should print Mario handler
