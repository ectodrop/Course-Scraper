import graph

g = graph.Graph()

course = "something"
while True:
    course = input("Enter a course code (Ending in H3): ")
    if course == "": break
    n = input("Enter a max depth to search: ")
    if n == "": break
    g.find_in_connections(course, max_depth = int(n))