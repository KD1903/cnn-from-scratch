from PIL import Image
from numpy import array, asarray, zeros

image = Image.open("data/Porsche_072.jpg").convert('L')
img_array = asarray(image)

# img_array = asarray([[0, 0, 0, 1, 1, 0, 0, 0],
#                      [0, 0, 0, 1, 1, 0, 0, 0],
#                      [0, 0, 0, 1, 1, 0, 0, 0],
#                      [0, 0, 0, 1, 1, 0, 0, 0],
#                      [0, 0, 0, 1, 1, 0, 0, 0],
#                      [0, 0, 0, 1, 1, 0, 0, 0],
#                      [0, 0, 0, 1, 1, 0, 0, 0],
#                      [0, 0, 0, 1, 1, 0, 0, 0]])

img_array_shape = img_array.shape

filter = array([[0, 1, 0],
                [0, 1, 0],
                [0, 1, 0]])
filter_shape = filter.shape
stride = 1

new_img_arr = zeros(shape=(img_array_shape[0]-filter_shape[0]+1, img_array_shape[1]-filter_shape[1]+1))

for i in range(img_array.shape[0]-filter_shape[0]+1):
    for j in range(img_array.shape[1]-filter_shape[1]+1):
        temp_img_arr = []
        for temp in range(filter_shape[0]):
            temp_img_arr.append(img_array[i+temp][j:j+filter_shape[1]])

        tmp = 0
        for k in range(filter_shape[0]):
            for l in range(filter_shape[1]):
                tmp += filter[k][l] * temp_img_arr[k][l]

        new_img_arr[i][j] = tmp

# print(new_img_arr)

new_img = Image.fromarray(new_img_arr)
new_img.show()