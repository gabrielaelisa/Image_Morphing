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
            rr,cc= s_line(line.y0,line.x0,line.y1,line.x1)
            red[rr,cc]=0
            green[rr,cc]=0
            blue[rr,cc]=255

    def resize(self):
        self.image= resize(self.image, (256, 256), anti_aliasing=True)

class Line:

    def __init__(self, vec):
        self.x0 = int(vec[0])
        self.y0 = int(vec[1])
        self.P= np.array([self.x0, self.y0])
        self.x1 = int(vec[2])
        self.y1 = int(vec[3])
        self.Q= np.array([self.x1, self.y1])

    def find_u_v(self, X):
        X_P= np.subtract(X, self.P)
        Q_P= np.subtract(self.Q, self.P)
        mag=np.linalgnorm(Q_P)
        Perp= np.array([Q_P[1], -1*Q_P[0]])
        u= np.dot(X_P, Q_P)/ math.pow(mag,2)
        v=np.dot(X_P, Perp)/mag
        return(u,v)

    def calculate_x_i(u,v):
        X_P= np.subtract(X, self.P)
        Q_P= np.subtract(self.Q, self.P)
        mag=np.linalgnorm(Q_P)
        Perp= np.array([Q_P[1], -1*Q_P[0]])
        return self.P+ np.dot(u, Q_P) + np.dot(v, Perp)/mag
    
