class Solution(object):
    def flipAndInvertImage(self, image):
        for i in range(len(image)):
            line = []
            for j in reversed(range(len(image))):
                line += [0 if image[i][j] == 1 else 1]
            image[i] = line
        return image
        