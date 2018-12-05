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
        self.x1 = int(vec[2])
        self.y1 = int(vec[3])