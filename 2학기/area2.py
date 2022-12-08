def tri_area(width, heigth):
    return width*heigth*1/2


def box_area(width, heigth):
    return width*heigth


def print_area(width, heigth):
    print("가로", width, " 세로", heigth, "인 삼각형의 넓이 :",
          tri_area(width, heigth))
    print("가로", width, " 세로", heigth, "인 사각형의 넓이 :",
          box_area(width, heigth))


if __name__ == "__main__":
    print_area(3, 5)
    print_area(6, 10)
print(__name__)
