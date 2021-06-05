import pickle

class Graph:
    def __init__(self):
        self.course_info = {}
        with open("course_info.pkl", "rb") as f:
            self.course_info = pickle.load(f)
        self._pre_req = "pre-requisites"
        self._pre_req_full = "pre-requisites-full"
        self._desc = "desc"
        
    def is_pre_req(self, curr, code):
        for c in self.course_info[curr][self._pre_req]:
            if code in c:
                return True, type(c) == tuple
        return False, False
    def find_out_connections(self,code, max_depth = 1, depth = 0):
        if depth == max_depth: return
        code = code.upper()
        if "H3" not in code: code += "H3"
        if code not in self.course_info:
            print("Invalid Course Code")
            return 
        if depth == 0:
            print(self.course_info[code][self._desc], self.course_info[code][self._pre_req_full])
        for course in self.course_info.keys():
            pre_req, opt = self.is_pre_req(course, code)
            if pre_req:
                output = "\t"*(depth+1) + self.course_info[course][self._desc]
                if opt: output = "\t"*(depth+1) + f"({self.course_info[course][self._desc]})" 
                print(output)
                self.find_out_connections(course, max_depth, depth + 1)
g = Graph()

course = "something"
while True:
    course = input("Enter a course code (Ending in H3): ")
    n = input("Enter a max depth to search: ")
    if course == "" or n == "": break
    g.find_out_connections(course, max_depth = int(n))