
class ObjLoader(object):
    def __init__(self, fileName):
        self.vertices = []
        self.faces = []
        ##
        try:
            f = open(fileName)
            for line in f:
                if line[:2] == "v ":
                    index1 = line.find(" ") + 1
                    index2 = line.find(" ", index1 + 1)
                    index3 = line.find(" ", index2 + 1)

                    vertex = (float(line[index1:index2]), float(line[index2:index3]), float(line[index3:-1]))
                    vertex = (round(vertex[0], 2), round(vertex[1], 2), round(vertex[2], 2))
                    self.vertices.append(vertex)

                elif line[0] == "f":
                    #string = line.replace("//", "/")
                    string = line
                    ##
                    i = string.find(" ") + 1
                    face = []
                    for item in range(string.count(" ")):
                        if string.find(" ", i) == -1:
                            face.append(int(string[i:-1].split('/')[0])-1)
                            break
                        face.append(int(string[i:string.find(" ", i)].split('/')[0])-1)
                        i = string.find(" ", i) + 1
                    ##
                    self.faces.append(tuple(face))

            f.close()
        except IOError:
            print(".obj file not found.")

class TargetLoader(object):
    def __init__(self, fileName):
        self.vertices = []
        self.indices = []
        ##
        try:
            f = open(fileName)
            for line in f:
                if line[:1] != "#":
                    index0 = 0
                    index1 = line.find(" ", index0 + 1)
                    index2 = line.find(" ", index1 + 1)
                    index3 = line.find(" ", index2 + 1)
                    #print(line[index0:index1],"|",line[index1:index2],"|",line[index2:index3],"|",line[index3:-1])
                    vertex = (float(line[index1:index2]), float(line[index2:index3]), float(line[index3:-1]))
                    vertex = (round(vertex[0], 2), round(vertex[1], 2), round(vertex[2], 2))
                    self.vertices.append(vertex)
                    self.indices.append(int(line[index0:index1]) - 1)



            f.close()
        except IOError:
            print(".obj file not found.")