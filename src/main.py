# Problème 1
def img2ascii(img_data: list[list[int]], black:str = '#', white:str = '.' ) -> str:
    return '\n'.join(
        ''.join(black if pixel else white for pixel in row)
        for row in img_data
    )

img = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# Problème 2


def load_pbm(filename: str) -> list[list[int]]:
    with open(filename, 'r') as file:
        lines = file.readlines()
    lines = [line for line in lines if not line.startswith('#')]
    format_code = lines[0].strip()
    width, height = map(int, lines[1].split())
    data = ''.join(lines[2:]).replace('\n', '')
    pixels = [[int(data[y*width + x]) for x in range(width)] for y in range(height)]
    return format_code, width, height, pixels

ascii = img2ascii(img)
print(repr(ascii))
print(ascii)