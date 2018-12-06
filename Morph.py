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
        self.dim= 256
        self.lines = lines
        self.N = N
        (s_l,d_l)= self.process_input_file()

        self.src_image= Image(img1,s_l)
        self.dest_image= Image(img2, d_l)

        self.resize()
        #self.src_image.draw_lines()
        #self.dest_image.draw_lines()
        self.warp(self.src_image)

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
        self.src_image.resize(self.dim)
        self.dest_image.resize(self.dim)

    def display(self):
        fig, axes = plt.subplots(nrows=2, ncols=2)
        ax = axes.ravel()
        ax[0].imshow(self.src_image.image, cmap='gray')
        ax[1].imshow(self.dest_image.image, cmap='gray')
        plt.show()

    def warp(self, src_image):
        int_image= np.zeros_like(src_image.image)
        alist=[]
        for i in range(self.dim):
            for j in range(self.dim):
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
                distance= line.shortest_distance(x,u,v)
                weight= math.pow(math.pow(length,p)/(distance + a), b)
                DSUM+=D_i*weight
                weightsum+=weight
                it+=1
            x_i=x +DSUM/weightsum
            #x_i= x_i.astype(int)
            if x_i[0]>255:
                x_i[0]=255
            if x_i[1]>255:
                x_i[1]=255
            self.interpolation(x, x_i, int_image, src_image)

            #int_image[x[1],x[0]]=src_image.image[x_i[1],x_i[0]]

        plt.imshow(int_image,vmin=0, vmax=1)
        plt.show()

    def interpolation(self,x,xi, int_image, src_image):
        '''
        :param int_image intermediary image
        :param src_image source image
        if x is a float, returns the interpolation of pixels
        '''
        rx= xi[0]%1 #col
        ry= xi[1]%1 #row
        xi= xi.astype(int)
        if(rx==0 and ry==0):
            int_image[x[1],x[0]]=src_image.image[xi[1],xi[0]]

        elif(rx==0):
            term1=(1-ry)*src_image.image[xi[1],xi[0]] 
            term2=ry*src_image.image[xi[1]+1,xi[0]]
            int_image[x[1],x[0]]=term1 + term2

        elif(ry==0):
            term1=(1-rx)*src_image.image[xi[1], xi[0]]
            term2=rx*src_image.image[xi[1], xi[0]+1]
            int_image[x[1],x[0]]= term1 +term2

        else:
            
            term1= rx*ry*src_image.image[xi[1]+1, xi[0]+1]
            term2= rx*(1-ry)*src_image.image[xi[1], xi[0]+1]
            term3= ry*(1-rx)*src_image.image[xi[1]+1, xi[0]]
            term4= (1-ry)*(1-rx)*src_image.image[xi[1], xi[0]]
            
            int_image[x[1],x[0]]=term1+ term2 +term3 +term4


        

