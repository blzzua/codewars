# https://www.codewars.com/kata/64b6698c94167906c3fbd6c4

def max_overlap(img1, img2):
    sizes = len(img1), len(img1[0])
    max_comp = 0
    cur_comp = 0

    for shift1 in range(sizes[0]):
        for shift2 in range(sizes[1]):
            cur_comp = 0
            for line1, line2 in zip(img1,img2[shift1:]):
                for c1, c2 in zip(line1, line2[shift2:]):
                    if 1 == c1 == c2:
                        cur_comp += 1
            max_comp = max(max_comp, cur_comp)

            cur_comp = 0
            for line1, line2 in zip(img1[shift1:],img2):
                for c1, c2 in zip(line1, line2[shift2:]):
                    if 1 == c1 == c2:
                        cur_comp += 1
            max_comp = max(max_comp, cur_comp)

            cur_comp = 0
            for line1, line2 in zip(img1[shift1:],img2):
                for c1, c2 in zip(line1[shift2:], line2):
                    if 1 == c1 == c2:
                        cur_comp += 1
            max_comp = max(max_comp, cur_comp)

            cur_comp = 0
            for line1, line2 in zip(img1,img2[shift1:]):
                for c1, c2 in zip(line1[shift2:], line2):
                    if 1 == c1 == c2:
                        cur_comp += 1
            max_comp = max(max_comp, cur_comp)
    return max_comp


# clever lib function:
# from scipy.signal import correlate2d
# correlate2d(img1, img2).max()
