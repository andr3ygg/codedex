import imageio.v3 as iio


def create_gif (*argv):
  images = [ ]
  #ARGV are the imgaes
  for img in argv:
    images.append(iio.imread(img))
    iio.imwrite('chicklet.gif', images, duration = 500, loop = 0) 



def main():
  create_gif("collections/chicklet1.png", "collections/chicklet2.png", "collections/chicklet3.png", "collections/chicklet4.png")


if __name__ == "__main__":
  main()