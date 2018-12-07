from Morph import *
if __name__ == '__main__':
    # parámetros de entrada
    path_img1= sys.argv[1]
    path_img2= sys.argv[2]
    file= sys.argv[3]
    N = int(sys.argv[4])

    img1 = io.imread(path_img1)
    img2 = io.imread(path_img2)
    m = Morph(img1, img2, file, N)
    m.display()
    '''
    img1= resize(img1, (256, 256), anti_aliasing=True)
    img2= resize(img2, (256, 256), anti_aliasing=True)
    fig, xs = plt.subplots(1, 2)
    xs[0].imshow(img1, cmap="gray")
    xs[1].imshow(img2, cmap="gray")
    plt.show()
    #m = Morph(img1, img2, file, N)
    #m.display()
    '''