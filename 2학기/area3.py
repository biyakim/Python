import sys


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
    if len(sys.argv) == 3:
        print_area(int(sys.argv[1]), int(sys.argv[2]))
    else:
        print("사용법 : python area3 가로 세로")
