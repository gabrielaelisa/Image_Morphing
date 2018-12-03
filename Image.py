from headers import *
class Image:
    def __init__(self, img, lines):
        self.image= img
        self.lines= lines

    def draw_lines(self):
        '''

        :return: draws reference lines on
        top of the image
        '''
        for line in self.lines:
            red = self.image[:, :, 0]
            green = self.image[:, :, 1]
            blue = self.image[:, :, 2]
            x0= int(line[0])
            y0=int(line[1])
            x1=int(line[2])
            y1=int(line[3])
            rr,cc= s_line(x0,y0,x1,y1)
            red[cc,rr]=0
            green[cc,rr]=0
            blue[cc,rr]=255

    def resize(self):
        self.image= resize(self.image, (256, 256), anti_aliasing=True)