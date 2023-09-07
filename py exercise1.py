import re

def count_and_replace(filename):
    terrible_count = 0
    even_count = False  # 用于跟踪"terrible"出现的是偶数次还是奇数次
    new_lines = []

    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:

        matches = [(m.start(0), m.end(0)) for m in re.finditer(r'\bterrible\b', line, re.IGNORECASE)]

        if matches:
            terrible_count += len(matches)
        
        last_end = 0
        new_line = ''
        
        for start, end in matches:
            even_count = not even_count
            
            new_line += line[last_end:start]
            if even_count:
                new_line += 'pathetic'
            else:
                new_line += 'marvellous'
            
            last_end = end

        new_line += line[last_end:]
        new_lines.append(new_line)

    with open('result.txt', 'w') as result_file:
        for new_line in new_lines:
            result_file.write(new_line + '\n')
    
    return terrible_count

if __name__ == "__main__":
    filename = 'file_to_read.txt'
    terrible_count = count_and_replace(filename)
    print(f"The word 'terrible' appears {terrible_count} times in the file.")
