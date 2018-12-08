from headers import *
class Image:
    def __init__(self, img, lines):
        self.image= img
        self.lines= self.process_lines(lines)

    def process_lines(self, ls):
        lines=[]
        for item in ls:
            l= Line(item)
            lines.append(l)
        return lines


    def draw_lines(self):
        '''

        :return: draws reference lines on
        top of the image
        '''

        for line in self.lines:
            red = self.image[:, :, 0]
            green = self.image[:, :, 1]
            blue = self.image[:, :, 2]
            rr,cc= s_line(line.P[1],line.P[0],line.Q[1],line.Q[0])
            red[rr,cc]=0
            green[rr,cc]=0
            blue[rr,cc]=255
        self.image=resize(self.image, (256, 256), anti_aliasing=True)

    def resize(self, dim):
        self.image= resize(self.image, (dim, dim), anti_aliasing=True)

class Line:

    def __init__(self, vec):
        self.vec= vec
        # x0, y0
        self.P= np.array([vec[0], vec[1]])
        #x1, y1
        self.Q= np.array([vec[2], vec[3]])
        self.Q_P= np.subtract(self.Q, self.P)
    

    def shortest_distance(self,x, u, v):
        '''
        :param x is a numpy array (tuple)
        :returns shortest distance for point x to
        the line defined by P Q from object line
        '''
        if(u >0 and u <1):
            return abs(v)

        if(u<0):
            p= np.subtract(self.P, x)
            return np.linalg.norm(p)

        else:
            p= np.subtract(self.Q, x)
            return np.linalg.norm(p)


    def find_u_v(self, X):
        X_P= np.subtract(X, self.P)
        mag=np.linalg.norm(self.Q_P)
        Perp= np.array([self.Q_P[1], -1*self.Q_P[0]])
        u= np.dot(X_P, self.Q_P)/ math.pow(mag,2)
        v=np.dot(X_P, Perp)/mag
        return(u,v)

    def calculate_x_i(self,u,v):
        mag=np.linalg.norm(self.Q_P)
        Perp= np.array([self.Q_P[1], -1*self.Q_P[0]])
        return self.P+ np.dot(u, self.Q_P) + np.dot(v, Perp)/mag
