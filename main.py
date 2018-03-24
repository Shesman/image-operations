from image_operations import *

image_default1 = 'imagens/sapo.png'
image_default2 = 'imagens/world.png'


def image_to_use(quantity):
    if quantity is 1:
        choice = input('WHAT IMAGES DO YOU WILL USE?\n '
                       'press enter to defaults')
        if str(choice) is '':
            return image_default1
        else:
            return str(choice)
    elif quantity is 2:
        choice = input('WHAT IS THE FIRST IMAGE DO YOU WILL USE\n? '
                       'press enter to defaults')
        if choice is not '':
            choice2 = input('WHAT IS THE SECOND IMAGE DO YOU WILL USE?\n')
        if str(choice) is '':
            return image_default1, image_default2
        else:
            return str(choice), str(choice2)


def main():
    menu = input('What operation do you want perform?'
                 '\n1-  Divide images'
                 '\n2-  Divide image by a scalar number'
                 '\n3-  Multiply image by image'
                 '\n4-  Multiply image by scalar number'
                 '\n5-  Sum of two images'
                 '\n6-  Subtraction of two images'
                 '\n7-  Logic \"AND\" of two images'
                 '\n8-  Logic \"OR\" of two images'
                 '\n9-  Logic \"NOT\" of two images'
                 '\n10- Logic \"NAND\" of two images'
                 '\n11- Logic \"NOR\" of two images'
                 '\n12- Logic \"XOR\" of two images\n\n')

    if int(menu) is 1:
        images = image_to_use(2)
        imagem3 = divideImages(images[0], images[1])
        show(imagem3)

    elif int(menu) is 2:
        images = image_to_use(1)
        scalar = int(input('Type the scalar number:\n'))
        imagem3 = divideImagesByScalar(images, scalar)
        show(imagem3)

    elif int(menu) is 3:
        images = image_to_use(2)
        imagem3 = multiplyImages(images[0], images[1])
        show(imagem3)

    elif int(menu) is 4:
        images = image_to_use(1)
        scalar = int(input('Type the scalar number:\n'))
        imagem3 = multiplyImagesByScalar(images, scalar)
        show(imagem3)

    elif int(menu) is 5:
        images = image_to_use(2)
        imagem3 = sumImages(images[0], images[1])
        show(imagem3)

    elif int(menu) is 6:
        images = image_to_use(2)
        imagem3 = subtractImages(images[0], images[1])
        show(imagem3)

    elif int(menu) is 7:
        images = image_to_use(2)
        imagem3 = logic_AND(images[0], images[1])
        show(imagem3)

    elif int(menu) is 8:
        images = image_to_use(2)
        imagem3 = logic_OR(images[0], images[1])
        show(imagem3)

    elif int(menu) is 9:
        images = image_to_use(2)
        imagem3 = logic_NOT(images[0], images[1])
        show(imagem3)

    elif int(menu) is 10:
        images = image_to_use(2)
        imagem3 = logic_NAND(images[0], images[1])
        show(imagem3)

    elif int(menu) is 11:
        images = image_to_use(2)
        imagem3 = logic_NOR(images[0], images[1])
        show(imagem3)

    elif int(menu) is 12:
        images = image_to_use(2)
        imagem3 = logic_XOR(images[0], images[1])
        show(imagem3)
    else:
        print('Invalid choice\n')

    exit(0)


# imagem3 = logic_NOR(imagem1,imagem2)
# show(imagem3)
# choices = image_to_use(2)
# print(choices)

if __name__ == '__main__':
    main()
