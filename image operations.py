import cv2 as editor

def printPixelValue(image_path1, final_row, final_column, final_value):
    image1 = editor.imread(image_path1)
    i = 0
    for row in image1:
        if i < final_row:
            i = i + 1
            print('ROW - ', i)
            j = 0
        for column in row:
            if j < final_column:
                j = j +1
                print('COLUMN -- ', j)
                k = 0
            for value in column:
                if k < final_value:
                    k = k + 1
                    print('value --- ', k)
                    return value

def getvalue(image_path,i,j,rgb):
    image = editor.imread(image_path)
    if rgb == 'r':
        color = 0
    elif rgb == 'g':
        color = 1
    elif rgb == 'b':
        color = 2
    else:
        print(' \'rgb\' need to be a Char!')
        return 'error'
    return image[int(i)][int(j)][color]

def divideImages(image_path1,image_path2):
    image1 = editor.imread(image_path1)
    image2 = editor.imread(image_path2)
    image3 = image2
    i = 0
    while i < len(image1):
        j = 0
        while j < len(image1):
            rgb = 0
            while rgb < 3:
                if (int(image1[i][j][rgb]) is not 0) and (int(image2[i][j][rgb]) is not 0) :
                    image3[i][j][rgb] = int(image1[i][j][rgb]) / int(image2[i][j][rgb])
                rgb = rgb + 1
            j = j + 1
        i = i + 1
    return image3

def divideImagesByScalar(image_path1,scalar):
    image1 = editor.imread(image_path1)
    image2 = image1
    i = 0
    while i < len(image1):
        j = 0
        while j < len(image1):
            rgb = 0
            while rgb < 3:
                image2[i][j][rgb] = int(image1[i][j][rgb]) / int(scalar)
                rgb = rgb + 1
            j = j + 1
        i = i + 1
    return image2

def multiplyImagesByScalar(image_path1,scalar):
    image1 = editor.imread(image_path1)
    image2 = image1
    i = 0
    while i < len(image1):
        j = 0
        while j < len(image1):
            rgb = 0
            while rgb < 3:
                image2[i][j][rgb] = int(image1[i][j][rgb]) * int(scalar)
                rgb = rgb + 1
            j = j + 1
        i = i + 1
    return image2

def multiplyImages(image_path1,image_path2):
    image1 = editor.imread(image_path1)
    image2 = editor.imread(image_path2)
    image3 = image2
    i = 0
    while i < len(image1):
        j = 0
        while j < len(image1):
            rgb = 0
            while rgb < 3:
                image3[i][j][rgb] = int(image1[i][j][rgb]) * int(image2[i][j][rgb])
                rgb = rgb + 1
            j = j + 1
        i = i + 1
    return image3

def subtractImages(image_path1,image_path2):
    image1 = editor.imread(image_path1)
    image2 = editor.imread(image_path2)
    image3 = image2
    i = 0
    while i < len(image1):
        j = 0
        while j < len(image1):
            rgb = 0
            while rgb < 3:
                image3[i][j][rgb] = int(image1[i][j][rgb]) - int(image2[i][j][rgb])
                rgb = rgb + 1
            j = j + 1
        i = i + 1
    return image3

def sumImages(image_path1,image_path2):
    image1 = editor.imread(image_path1)
    image2 = editor.imread(image_path2)
    image3 = image2
    i = 0
    while i < len(image1):
        j = 0
        while j < len(image1):
            rgb = 0
            while rgb < 3:
                image3[i][j][rgb] = int(image1[i][j][rgb]) + int(image2[i][j][rgb])
                rgb = rgb + 1
            j = j + 1
        i = i + 1
    return image3

def otimization(v_max,v_min,value):
    return (255/v_max)*(value - v_min)

def round(number):
    if number > 128:
        return True
    else:
        return False

def logic_AND(image_path1, image_path2):
    image1 = editor.imread(image_path1,0)
    image2 = editor.imread(image_path2,0)
    image3 = image2
    i = 0
    while i < len(image1):
        j = 0
        while j < len(image1):
            temp = round(image1[i][j]) and round(image2[i][j])
            if temp:
                image3[i][j] = 255
            else:
               image3[i][j] = 0
            j = j + 1
        i = i + 1
    return image3

def logic_OR(image_path1, image_path2):
    image1 = editor.imread(image_path1,0)
    image2 = editor.imread(image_path2,0)
    image3 = image2
    i = 0
    while i < len(image1):
        j = 0
        while j < len(image1):
            temp = round(image1[i][j]) or round(image2[i][j])
            if temp:
                image3[i][j] = 255
            else:
               image3[i][j] = 0
            j = j + 1
        i = i + 1
    return image3

def logic_XOR(image_path1, image_path2):
    image1 = editor.imread(image_path1,0)
    image2 = editor.imread(image_path2, 0)
    image3 = image2
    i = 0
    while i < len(image1):
        j = 0
        while j < len(image1):
            temp = round(image1[i][j]) is not round(image2[i][j])
            if temp:
                image3[i][j] = 255
            else:
               image3[i][j] = 0
            j = j + 1
        i = i + 1
    return image3

def logic_NAND(image_path1, image_path2):
    image1 = editor.imread(image_path1, 0)
    image2 = editor.imread(image_path2, 0)
    image3 = image2
    i = 0
    while i < len(image1):
        j = 0
        while j < len(image1):
            temp = round(image1[i][j]) and round(image2[i][j])
            if temp is not True:
                image3[i][j] = 255
            else:
               image3[i][j] = 0
            j = j + 1
        i = i + 1
    return image3

def logic_NOR(image_path1, image_path2):
    image1 = editor.imread(image_path1, 0)
    image2 = editor.imread(image_path2, 0)
    image3 = image2
    i = 0
    while i < len(image1):
        j = 0
        while j < len(image1):
            temp = round(image1[i][j]) or round(image2[i][j])
            if temp is not True:
                image3[i][j] = 255
            else:
               image3[i][j] = 0
            j = j + 1
        i = i + 1
    return image3

def logic_NOT(image_path1):
    image1 = editor.imread(image_path1, 0)
    image2 = image1
    i = 0
    while i < len(image1):
        j = 0
        while j < len(image1):
            temp = round(image1[i][j])
            if temp:
                image2[i][j] = 0
            else:
               image2[i][j] = 255
            j = j + 1
        i = i + 1
    return image2


def main():
    imagem1 = 'imagens/sapo.png'
    imagem2 = 'imagens/world.png'
    imagem3 = logic_NOR(imagem1,imagem2)
    editor.imshow('imagem',imagem3)
    editor.waitKey(0)
main()
