from headers import *
from Image import *
p=1
b= 2
a= 0.01
class Morph:

    def __init__(self, img1, img2, lines, N):
        '''

        :param img1: source image for morphing
        :param img2:  destination image for morphing
        :param lines: lines of correspondance, .txt file
        :param N: number of inter-¡mediary images
        '''
        self.lines = lines
        self.N = N
        (s_l,d_l)= self.process_input_file()

        self.src_image= Image(img1,s_l)
        self.dest_image= Image(img2, d_l)

        self.resize()
        self.src_image.draw_lines()
        self.dest_image.draw_lines()
        #self.warp(self.src_image)

    def process_input_file(self):
        src_lines= []
        dest_lines = []
        input = open(self.lines, 'r')
        for line in input:
            s=line.split(',')
            src_lines.append(s[:4])
            dest_lines.append(s[4:])
        return (src_lines, dest_lines)

    def resize(self):
        '''

        :return: reesclaed image into 256x256 pixels
        '''
        self.src_image.resize()
        self.dest_image.resize()

    def display(self):
        fig, axes = plt.subplots(nrows=2, ncols=2)
        ax = axes.ravel()
        ax[0].imshow(self.src_image.image, cmap='gray')
        ax[1].imshow(self.dest_image.image, cmap='gray')
        plt.show()

    def warp(self, src_image):
        int_image= np.zeros_like(src_image.image)
        alist=[]
        for i in range(225):
            for j in range(225):
                alist.append(np.array([i,j]))
        for x in alist: # for each pixel in intermediary image
            DSUM= np.array([0.0,0.0])
            weightsum= 0
            it=0
            for line in self.dest_image.lines:
                (u,v) = line.find_u_v(x)
                line2= src_image.lines[it]
                x_i=line2.calculate_x_i(u,v)
                D_i=x_i-x # displacement
                length= np.linalg.norm(line.Q_P)# line length
                distance= line.shortest_distance(x)
                weight= math.pow(math.pow(length,p)/(distance + a), b)
                DSUM+=D_i*weight
                weightsum+=weight
                it+=1
            x_i=x +DSUM/weightsum
            x_i= x_i.astype(int)
            if x_i[0]>255:
                x_i[0]=255
            if x_i[1]>255:
                x_i[1]=255
            int_image[x[0],x[1], 0]=src_image.image[x_i[0],x_i[1], 0]
            int_image[x[0],x[1], 1]=src_image.image[:, :, 1][x_i[0],x_i[1]]
            int_image[x[0],x[1], 2]=src_image.image[:, :, 2][x_i[0],x_i[1]]

        plt.imshow(int_image,vmin=0, vmax=1)
        plt.show()                

