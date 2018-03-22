import cv2 as editor

def printPixelValue(image1, final_row, final_column, final_value):
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

def getvalue(image,i,j,rgb):
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

def divideImages(image1,image2):
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

def divideImagesByScalar(image1,scalar):
    image3 = image1
    i = 0
    while i < len(image1):
        j = 0
        while j < len(image1):
            rgb = 0
            while rgb < 3:
                image3[i][j][rgb] = int(image1[i][j][rgb]) / int(scalar)
                rgb = rgb + 1
            j = j + 1
        i = i + 1
    return image3

def multiplyImagesByScalar(image1,scalar):
    image3 = image1
    i = 0
    while i < len(image1):
        j = 0
        while j < len(image1):
            rgb = 0
            while rgb < 3:
                image3[i][j][rgb] = int(image1[i][j][rgb]) * int(scalar)
                rgb = rgb + 1
            j = j + 1
        i = i + 1
    return image3

def multiplyImages(image1,image2):
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


def subtractImages(image1,image2):
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


def sumImages(image1,image2):
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


def main():
    imagem1 = editor.imread('imagens/sapo.png')
    imagem3 = multiplyImagesByScalar(imagem1,2)
    editor.imshow('imagem',imagem3)
    editor.waitKey(0)
main()
