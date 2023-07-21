# https://www.codewars.com/kata/565f1bd8f97d3e59c400014a

fingers = ['Pinkie','Ring','Middle','Index','Thumb'][::-1]
def binary_fingers(bin_string):
    return [name for finger, name in zip(bin_string[::-1], fingers) if finger == '1'][::-1]
