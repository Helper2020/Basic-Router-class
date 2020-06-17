# Basic-Router-class

The router class is a wrapper class that provides
an interface. THe user can add a handlers and do lookups.

The RouteTrieNode stores each part of the path between slashes

And the RouteTrie will store the routes

The dictonary stores the children of each node.
I chose a  dictionary because it provides O(1) access and insert.



RouteTrie methods
Insert()
Time complexity:  O(n) Where n is length of the path
Space complexity: O(n) stack space

find()
Time complexity: O(n) where n is the length of the path
Space complexity: O(1)

RouteTrieNode methods
insert()
Time complexity: O(1)
Space complexity: O(1)

Router methods

add_handler()
where n is the length of the string
Time complexity: O(n)

where n is the length of the string and k is the stack space
Space complexity: O(n+k)

lookup()
Time complexity: O(n)
Space complexity: O(1)

split_patht():
Where n is the length of the string
Time complexity: O(n)
Where n is the length of the array
Space complexity: O(n)
