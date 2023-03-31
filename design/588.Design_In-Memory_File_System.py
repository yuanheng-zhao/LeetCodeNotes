# Hash, Trie, Design

class FileSystem:

    class Dir:
        def __init__(self):
            self.files = {} # filename -> content 
            self.dirs = {}  # dirname -> Dir

    def __init__(self):
        self.root_dir = self.Dir()

    def ls(self, path: str) -> List[str]:
        path_q = path.split('/')
        curr_dir = self.root_dir
        while path_q:
            dir_or_file = path_q.pop(0)
            if dir_or_file in curr_dir.files:
                return [dir_or_file]
            elif dir_or_file in curr_dir.dirs:
                curr_dir = curr_dir.dirs[dir_or_file]
            else:
                # Constraint: users will not attempt to retrieve file content or list a directory or file that does not exist.
                pass
        res = list(curr_dir.dirs) + list(curr_dir.files)
        res.sort()
        return res

    def mkdir(self, path: str) -> None:
        path_q = path.split('/')
        curr_dir = self.root_dir
        while path_q:
            direct = path_q.pop(0)
            if direct not in curr_dir.dirs:
                curr_dir.dirs[direct] = self.Dir()
            curr_dir = curr_dir.dirs[direct]
        
    def addContentToFile(self, filePath: str, content: str) -> None:
        path_q = filePath.split('/')
        curr_dir = self.root_dir
        while len(path_q) > 1:
            direct = path_q.pop(0)
            if direct not in curr_dir.dirs:
                curr_dir.dirs[direct] = self.Dir()
            curr_dir = curr_dir.dirs[direct]
        filename = path_q.pop(0)
        if filename in curr_dir.files:
            curr_dir.files[filename] += content
        else:
            curr_dir.files[filename] = content
        
    def readContentFromFile(self, filePath: str) -> str:
        path_q = filePath.split('/')
        curr_dir = self.root_dir
        while len(path_q) > 1:
            direct = path_q.pop(0)
            if direct not in curr_dir.dirs:
                curr_dir.dirs[direct] = self.Dir()
            curr_dir = curr_dir.dirs[direct]
        filename = path_q.pop(0)
        return curr_dir.files[filename]
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
