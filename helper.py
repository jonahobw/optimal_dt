from classes import road_sign, classifier, final_classifier, tree

def signs():
    signs = []
    for i in range(43):
        signs.append([])
    signs[0] = {"color": "red", "shape": "circle", "car": False, "numbers": True, "straight_arrows": False,
                "curved_arrows": False, "road": False}
    signs[1] = {"color": "red", "shape": "circle", "car": False, "numbers": True, "straight_arrows": False,
                "curved_arrows": False, "road": False}
    signs[2] = {"color": "red", "shape": "circle", "car": False, "numbers": True, "straight_arrows": False,
                "curved_arrows": False, "road": False}
    signs[3] = {"color": "red", "shape": "circle", "car": False, "numbers": True, "straight_arrows": False,
                "curved_arrows": False, "road": False}
    signs[4] = {"color": "red", "shape": "circle", "car": False, "numbers": True, "straight_arrows": False,
                "curved_arrows": False, "road": False}
    signs[5] = {"color": "red", "shape": "circle", "car": False, "numbers": True, "straight_arrows": False,
                "curved_arrows": False, "road": False}
    signs[6] = {"color": "white", "shape": "circle", "car": False, "numbers": True, "straight_arrows": False,
                "curved_arrows": False, "road": False}
    signs[7] = {"color": "red", "shape": "circle", "car": False, "numbers": True, "straight_arrows": False,
                "curved_arrows": False, "road": False}
    signs[8] = {"color": "red", "shape": "circle", "car": False, "numbers": True, "straight_arrows": False,
                "curved_arrows": False, "road": False}
    signs[9] = {"color": "red", "shape": "circle", "car": True, "numbers": False, "straight_arrows": False,
                "curved_arrows": False, "road": False}
    signs[10] = {"color": "red", "shape": "circle", "car": True, "numbers": False, "straight_arrows": False,
                "curved_arrows": False, "road": False}
    signs[11] = {"color": "red", "shape": "triangle", "car": False, "numbers": False, "straight_arrows": False,
                "curved_arrows": False, "road": True}
    signs[12] = {"color": "yellow", "shape": "diamond", "car": False, "numbers": False, "straight_arrows": False,
                "curved_arrows": False, "road": False}
    signs[13] = {"color": "red", "shape": "inverted_triangle", "car": False, "numbers": False, "straight_arrows": False,
                "curved_arrows": False, "road": False}
    signs[14] = {"color": "red", "shape": "octagon", "car": False, "numbers": False, "straight_arrows": False,
                "curved_arrows": False, "road": False}
    signs[15] = {"color": "red", "shape": "circle", "car": False, "numbers": False, "straight_arrows": False,
                "curved_arrows": False, "road": False}
    signs[16] = {"color": "red", "shape": "circle", "car": False, "numbers": False, "straight_arrows": False,
                "curved_arrows": False, "road": False}
    signs[17] = {"color": "red", "shape": "circle", "car": False, "numbers": False, "straight_arrows": False,
                "curved_arrows": False, "road": False}
    signs[18] = {"color": "red", "shape": "triangle", "car": False, "numbers": False, "straight_arrows": False,
                "curved_arrows": False, "road": False}
    signs[19] = {"color": "red", "shape": "triangle", "car": False, "numbers": False, "straight_arrows": False,
                "curved_arrows": False, "road": True}
    signs[20] = {"color": "red", "shape": "triangle", "car": False, "numbers": False, "straight_arrows": False,
                "curved_arrows": False, "road": True}
    signs[21] = {"color": "red", "shape": "triangle", "car": False, "numbers": False, "straight_arrows": False,
                 "curved_arrows": False, "road": True}
    signs[22] = {"color": "yellow", "shape": "triangle", "car": False, "numbers": False, "straight_arrows": False,
                 "curved_arrows": False, "road": False}
    signs[23] = {"color": "red", "shape": "triangle", "car": True, "numbers": False, "straight_arrows": False,
                 "curved_arrows": False, "road": False}
    signs[24] = {"color": "red", "shape": "triangle", "car": False, "numbers": False, "straight_arrows": False,
                 "curved_arrows": False, "road": True}
    signs[25] = {"color": "yellow", "shape": "triangle", "car": False, "numbers": False, "straight_arrows": False,
                 "curved_arrows": False, "road": False}
    signs[26] = {"color": "red", "shape": "triangle", "car": False, "numbers": False, "straight_arrows": False,
                 "curved_arrows": False, "road": False}
    signs[27] = {"color": "red", "shape": "triangle", "car": False, "numbers": False, "straight_arrows": False,
                 "curved_arrows": False, "road": False}
    signs[28] = {"color": "red", "shape": "triangle", "car": False, "numbers": False, "straight_arrows": False,
                 "curved_arrows": False, "road": False}
    signs[29] = {"color": "red", "shape": "triangle", "car": False, "numbers": False, "straight_arrows": False,
                 "curved_arrows": False, "road": False}
    signs[30] = {"color": "red", "shape": "triangle", "car": False, "numbers": False, "straight_arrows": False,
                 "curved_arrows": False, "road": False}
    signs[31] = {"color": "red", "shape": "triangle", "car": False, "numbers": False, "straight_arrows": False,
                 "curved_arrows": False, "road": False}
    signs[32] = {"color": "white", "shape": "circle", "car": False, "numbers": False, "straight_arrows": False,
                 "curved_arrows": False, "road": False}
    signs[33] = {"color": "blue", "shape": "circle", "car": False, "numbers": False, "straight_arrows": False,
                 "curved_arrows": True, "road": False}
    signs[34] = {"color": "blue", "shape": "circle", "car": False, "numbers": False, "straight_arrows": False,
                 "curved_arrows": True, "road": False}
    signs[35] = {"color": "blue", "shape": "circle", "car": False, "numbers": False, "straight_arrows": True,
                 "curved_arrows": False, "road": False}
    signs[36] = {"color": "blue", "shape": "circle", "car": False, "numbers": False, "straight_arrows": True,
                 "curved_arrows": True, "road": False}
    signs[37] = {"color": "blue", "shape": "circle", "car": False, "numbers": False, "straight_arrows": True,
                 "curved_arrows": True, "road": False}
    signs[38] = {"color": "blue", "shape": "circle", "car": False, "numbers": False, "straight_arrows": True,
                 "curved_arrows": False, "road": False}
    signs[39] = {"color": "blue", "shape": "circle", "car": False, "numbers": False, "straight_arrows": True,
                 "curved_arrows": False, "road": False}
    signs[40] = {"color": "blue", "shape": "circle", "car": False, "numbers": False, "straight_arrows": False,
                 "curved_arrows": True, "road": False}
    signs[41] = {"color": "white", "shape": "circle", "car": True, "numbers": False, "straight_arrows": False,
                 "curved_arrows": False, "road": False}
    signs[42] = {"color": "white", "shape": "circle", "car": True, "numbers": False, "straight_arrows": False,
                 "curved_arrows": False, "road": False}

    road_sign_objects = []
    i = 0
    for sign in signs:
        road_sign_objects.append(road_sign(str(i), sign))
        i+=1
    return road_sign_objects


def attack_danger_weights(startsign_name, targetsign_name):

    '''

    for future use: the code to print out the weights:
    a = []
    for i in range(43):
        array = []
        for j in range(43):
            if(i==j):
                array.append(0)
            else:
                array.append(j)
        a.append(array)

    for arr in a:
        print(str(arr) + ",")
    '''

    weights = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 0, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 0, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 0, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 0, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 0, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 0, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 0, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 0, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 0, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 0, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 0, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 0, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 0,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         0, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 0, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 0, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 0, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 0, 35, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 0, 36, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 0, 37, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 0, 38, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 0, 39, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 0, 40, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 0, 41, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 0, 42],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 0]
    ]

    return weights[startsign_name][targetsign_name]


def split_signs(sign_array, attribute_name):

    # splits the signs in signarray based on the attribute_name
    # return values:
    # values (array) - unique values of attribute name
    # split (2d array) - the split up signs in sets, with the indexes
    #                   corresponding to the values array

    split = []
    values = []
    for sign in sign_array:
        if(sign.properties[attribute_name] not in values):
            values.append(sign.properties[attribute_name])
            split.append([sign])
        else:
            a = values.index(sign.properties[attribute_name])
            split[a].append(sign)
    return values, split


def find_child_classifiers(root, classifiers, signs):
    attribute = root.attribute_name
    values, split = split_signs(signs, attribute)
    possible_classifiers = []
    for i in range(len(split)):
        if (len(split[i]) == 1):
            # there is only 1 sign in this group
            # [0] indicates that there is only 1 sign
            # this sign will need to be a direct child of this root node
            possible_classifiers.append([0])
        elif(len(split[i]) == 2):
            #there are only 2 signs in this group
            #even if there is a classifier that distinguishes them, the next level down will be the road signs
            #themselves, so it makes sense to have a final classifier here
            possible_classifiers.append([1])
        else:
            # if the length of split[i] is more than 2, figure out which of the remaining
            # classifiers will split the group into 2 or more groups
            current_set_possible_classifiers = []
            for classifier in classifiers:
                child_values, child_split = split_signs(split[i], classifier)
                if (len(child_split) > 1):
                    current_set_possible_classifiers.append(classifier)
            if (len(current_set_possible_classifiers) == 0):
                # there are no classifiers that split the group of signs into 2 or more groups
                # [1] indicates that there are multiple signs, but no classifiers to differentiate between them
                # a final classifier will be needed
                possible_classifiers.append([1])
            else:
                possible_classifiers.append(current_set_possible_classifiers)
    return possible_classifiers


def find_child_classifiers2(root, classifiers, signs, classifier_budget):
    attribute = root.attribute_name
    values, split = split_signs(signs, attribute)
    possible_classifiers = []
    for i in range(len(split)):
        if (len(split[i]) == 1):
            # there is only 1 sign in this group
            # [0] indicates that there is only 1 sign
            # this sign will need to be a direct child of this root node
            possible_classifiers.append([0])
        elif(len(split[i]) == 2):
            #there are only 2 signs in this group
            #even if there is a classifier that distinguishes them, the next level down will be the road signs
            #themselves, so it makes sense to have a final classifier here
            possible_classifiers.append([1])
        else:
            # if the length of split[i] is more than 2, figure out which of the remaining
            # classifiers will split the group into 2 or more groups
            current_set_possible_classifiers = []
            for classifier in classifiers:
                child_values, child_split = split_signs(split[i], classifier)
                if (len(child_split) > 1):
                    current_set_possible_classifiers.append(classifier)
            if (len(current_set_possible_classifiers) == 0):
                # there are no classifiers that split the group of signs into 2 or more groups
                # [1] indicates that there are multiple signs, but no classifiers to differentiate between them
                # a final classifier will be needed
                possible_classifiers.append([1])
            else:
                possible_classifiers.append(current_set_possible_classifiers)
    return possible_classifiers


def print_tree(tree):

    # prints a 2D array where the 1st dimension is the depth of the nodes
    # and the second dimension are the nodes at that depth
    # nodes are printed in tuples (name of the node, name of the parent node)

    nodes = []
    nodenames = []
    root = tree.root
    nodenames.append([(root.name, root.parent)])
    nodes.append([root])

    children = root.children
    while(len(children)>0):
        grandchildren = []
        nodes.append(children)
        add_names = []
        for node in children:
            if(isinstance(node, classifier)):
                add_names.append((type(node), node.name, node.attribute_name, node.parent.name))
            else:
                add_names.append((type(node), node.name, node.parent.name))
            if(len(node.children)>1):
                for grandchild in node.children:
                    grandchildren.append(grandchild)
        nodenames.append(add_names)
        children = grandchildren
    return nodenames


def count_road_signs(Tree):
    # counts the number of road sign objects in a tree
    root = Tree.root
    unexplored = [root]
    count = 0
    while(len(unexplored)>0):
        node = unexplored.pop()
        if(isinstance(node, road_sign)):
            count +=1
        unexplored += node.children
    return count


def count_leaf_nodes(Tree):
    # counts the number of road sign objects in a tree
    root = Tree.root
    unexplored = [root]
    count = 0
    while(len(unexplored)>0):
        node = unexplored.pop()
        if(len(node.children)<1):
            count +=1
            continue
        unexplored += node.children
    return count


def count_all_classifiers(Tree):
    return len(Tree.nodes)- count_leaf_nodes(Tree)


def copy_tree(Tree):
    root = Tree.root
    if(isinstance(root, road_sign)):
        copy_root = road_sign(root.name, root.properties)
    elif(isinstance(root, classifier)):
        copy_root = classifier(root.name, root.attribute_name)
    elif(isinstance(root, final_classifier)):
        copy_root = final_classifier(root.name)
    copied_tree = tree(copy_root)
    copy_children(copy_root, root.children, copied_tree)
    return copied_tree


def copy_children(copy_parent, real_children, copy_tree):
    if(len(real_children)<1):
        return
    else:
        for real_child in real_children:
            if (isinstance(real_child, classifier)):
                newclassifier = classifier(real_child.name, real_child.attribute_name, copy_parent)
                copy_tree.add_node(newclassifier)
                copy_parent.children.append(newclassifier)
                copy_children(newclassifier, real_child.children, copy_tree)
            if (isinstance(real_child, final_classifier)):
                newfinalclassifier = final_classifier(real_child.name, copy_parent)
                copy_tree.add_node(newfinalclassifier)
                copy_parent.children.append(newfinalclassifier)
                copy_children(newfinalclassifier, real_child.children, copy_tree)
            if (isinstance(real_child, road_sign)):
                newroadsign = road_sign(real_child.name, real_child.properties, copy_parent)
                copy_tree.add_node(newroadsign)
                copy_parent.children.append(newroadsign)


def find_road_sign_path(root, sign):
    path = []
    current = root
    road_sign_numbers = []
    target = sign.name
    for child in current.children:
        if(isinstance(child, road_sign)):
            road_sign_numbers.append(child.name)
    bool = target in road_sign_numbers
    while(not bool):
        path.append(current)
        # figure out which child node to go to

        # if current node is a classifier, figure out which child
        # is the right attribute
        if(isinstance(current, classifier)):
            attribute = sign.properties[current.attribute_name]
            for node in current.children:
                if(node.name == attribute):
                    current = node
                    break
                if(isinstance(node, final_classifier)):
                    if(node.name.find(str(attribute))>0):
                        current = node
                        break
        road_sign_numbers = []
        for child in current.children:
            if (isinstance(child, road_sign)):
                road_sign_numbers.append(child.name)
        bool = target in road_sign_numbers
    path.append(current)
    path.append(sign)
    return path


def attack_distance(root, startsign, endsign):
    path1 = find_road_sign_path(root, startsign)
    path2 = find_road_sign_path(root, endsign)
    while(path1[0] == path2[0]):
        path1 = path1[1:]
        path2 = path2[1:]
    return len(path2)


def avg_attack_distance(tree, road_signs):
    # it is a directed attack so we want the data going from 0 -> 1 and 1 -> 0
    root = tree.root
    total_distance = 0
    count = 0
    signs = road_signs.copy()
    for startnode in signs:
        for endnode in signs:
            if (startnode.name == endnode.name):
                continue
            a = attack_distance(root, startnode, endnode)
            total_distance += a
            #print("", startnode.name, endnode.name, a)
            count +=1
    if(count != 1806):
        a = "Error, count = " + str(count)
        return a
    return total_distance/count


def weighted_avg_attack_distance(tree, road_signs):
    # it is a directed attack so we want the data going from 0 -> 1 and 1 -> 0
    #TODO implement weights in attack_danger_weights
    root = tree.root
    total_distance = 0
    count = 0
    signs = road_signs.copy()
    for startnode in signs:
        for endnode in signs:
            if (startnode.name == endnode.name):
                continue
            a = attack_distance(root, startnode, endnode)
            total_distance += a*attack_danger_weights(startnode.name, endnode.name)
            #print("", startnode.name, endnode.name, a)
            count +=1
    if(count != 1806):
        a = "Error, count = " + str(count)
        return a
    return total_distance/count


def get_permutations(array, permutations = [], current = []):
    #takes a 2d array and finds all permutations of it, taking one element from each array

    #base case
    if len(array) == 1:
        if(array[0] == []):
            new = current.copy()
            new.append([])
            permutations.append(new)
            return
        for item in array[0]:
            new = current.copy()
            new.append(item)
            permutations.append(new)
        return
    else:
    #len(2d_array is greater than 1)
        if(array[0] == []):
            new = current.copy()
            new.append([])
            get_permutations(array[1:], permutations, new)
        else:
            for item in array[0]:
                new = current.copy()
                new.append(item)
                get_permutations(array[1:], permutations, new)


def Tree_stats(Tree):
    signsarray = signs()
    print("\n\n\nThe tree is:")
    print(print_tree(Tree))
    print("\naverage attack distance:")
    print(avg_attack_distance(Tree, signsarray))
    print("number of road signs:")
    print(count_road_signs(Tree))
    print("number of leaf nodes:")
    print(count_leaf_nodes(Tree))
    print("total number of nodes")
    print(len(Tree.nodes))
    print("total number of classifiers")
    print(count_all_classifiers(Tree))
