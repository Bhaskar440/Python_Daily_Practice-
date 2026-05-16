def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase
    lines = []
    for i in range(size):
        s = alphabet[i:size]
        row_letters = s[::-1] + s[1:]
        row_str = "-".join(row_letters)
        if i == 0:
            total_width = (size * 4) - 3
        lines.append(row_str.center(total_width, "-"))
    rangoli_pattern = lines[::-1] + lines[1:]
    print('\n'.join(rangoli_pattern))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)