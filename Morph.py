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
        self.t= 1/(N+1)# morph step t
        (s_l,d_l)= self.process_input_file()

        self.src_image= Image(img1,s_l)
        self.dest_image= Image(img2, d_l)

        self.resize()
        self.src_image.draw_lines()
        self.dest_image.draw_lines()
        #self.morph()

    def process_input_file(self):
        src_lines= []
        dest_lines = []
        input = open(self.lines, 'r')
        for line in input:
            s=line.split(',')
            src_lines.append(np.array(s[:4]).astype(int))
            dest_lines.append(np.array(s[4:]).astype(int))
        return (src_lines, dest_lines)

    def resize(self):
        '''
        :return: reesclaed image into dimxdim pixels
        '''
        self.src_image.resize(self.dim)
        self.dest_image.resize(self.dim)

    def display(self):
        fig, axes = plt.subplots(nrows=1, ncols=2)
        ax = axes.ravel()
        ax[0].imshow(self.src_image.image, cmap='gray')
        ax[1].imshow(self.dest_image.image, cmap='gray')
        plt.show()

    def morph(self):
        '''

        :return: warped and blends image from
        source to dest
        '''
        step=self.t
        for i in range(self.N):
            im1= self.warp(self.src_image, self.dest_image, self.t)
            im2= self.warp(self.dest_image, self.src_image, self.t)
            im_t=self.blend(im1, im2, self.t)
            plt.imsave("results/image_step_" + str(i) + ".jpg", im_t)
            self.t+=step


        '''
        plt.axis('off')
        fig, xs = plt.subplots(1, 3)
        xs[0].imshow(im1, cmap="gray")
        xs[0].set_title("Warping source")
        xs[0].axis('off')
        xs[1].imshow(im2, cmap="gray")
        xs[1].set_title("Warping dest")
        xs[1].axis('off')
        xs[2].imshow(im_t, cmap="gray")
        xs[2].set_title("Blending")
        xs[2].axis('off')
        plt.show()
        '''

    def warp(self, src_image, dest_image, t):
        t_image= np.zeros_like(src_image.image)
        alist=[]
        for i in range(self.dim):
            for j in range(self.dim):
                alist.append(np.array([i,j]))
        for x in alist: # for each pixel in intermediary image
            DSUM= np.array([0.0,0.0])
            weightsum= 0
            it=0
            for line in dest_image.lines:
                line2= src_image.lines[it]
                line_t= Line(t*line.vec+(1-t)*line2.vec)
                (u,v) = line_t.find_u_v(x)
                x_i=line2.calculate_x_i(u,v)
                D_i=x_i-x # displacement
                length= np.linalg.norm(line_t.Q_P)# line length
                distance= line_t.shortest_distance(x,u,v)
                weight= math.pow(math.pow(length,p)/(distance + a), b)
                DSUM+=D_i*weight
                weightsum+=weight
                it+=1
            x_i=x +DSUM/weightsum
            if x_i[0]>self.dim-1:
                x_i[0]=self.dim-1
            if x_i[1]>self.dim-1:
                x_i[1]=self.dim-1
            self.interpolation(x, x_i, t_image, src_image)
        return t_image


    def interpolation(self,x,xi, t_image, src_image):
        '''
        :param int_image intermediary image
        :param src_image source image
        if x is a float, returns the interpolation of pixels
        '''
        rx= xi[0]%1 #col
        ry= xi[1]%1 #row
        xi= xi.astype(int)
        if(rx==0 and ry==0):
            t_image[x[1],x[0]]=src_image.image[xi[1],xi[0]]

        elif(rx==0):
            term1=(1-ry)*src_image.image[xi[1],xi[0]] 
            term2=ry*src_image.image[xi[1]+1,xi[0]]
            t_image[x[1],x[0]]=term1 + term2

        elif(ry==0):
            term1=(1-rx)*src_image.image[xi[1], xi[0]]
            term2=rx*src_image.image[xi[1], xi[0]+1]
            t_image[x[1],x[0]]= term1 +term2

        else:
            
            term1= rx*ry*src_image.image[xi[1]+1, xi[0]+1]
            term2= rx*(1-ry)*src_image.image[xi[1], xi[0]+1]
            term3= ry*(1-rx)*src_image.image[xi[1]+1, xi[0]]
            term4= (1-ry)*(1-rx)*src_image.image[xi[1], xi[0]]
            t_image[x[1],x[0]]=term1+ term2 +term3 +term4

    def blend(self, src_im, dest_im , t):
        return src_im*(1-t) +dest_im*t


        


        

