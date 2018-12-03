from headers import *
from Image import *
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
        print(s_l)
        self.src_image= Image(img1,s_l)
        self.dest_image= Image(img2, d_l)
        self.resize()
        self.src_image.draw_lines()
        self.dest_image.draw_lines()

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