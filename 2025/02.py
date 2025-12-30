def solve_gift_shop():
    puzzle_input = """5529687-5587329,50-82,374-560,83-113,226375-287485,293169-368713,2034-2634,9945560-9993116,4872472-4904227,3218-5121,1074-1357,15451-26093,483468003-483498602,51513-85385,1466-1992,7600-13034,710570-789399,407363-480868,3996614725-3996662113,3-17,5414907798-5414992881,86274-120443,828669-909588,607353-700604,4242340614-4242556443,28750-44009,935177-1004747,20-41,74678832-74818251,8484825082-8484860878,2784096938-2784156610,5477-7589,621-952,2424167145-2424278200,147085-217900,93043740-93241586"""

    ranges = puzzle_input.replace('\n', '').strip().split(',')
    
    total_sum = 0
    
    for r in ranges:
        start_str, end_str = r.split('-')
        start = int(start_str)
        end = int(end_str)
        
        for num in range(start, end + 1):
            s_num = str(num)
            length = len(s_num)
            
            if length % 2 == 0:
                mid = length // 2
                first_half = s_num[:mid]
                second_half = s_num[mid:]
                
                if first_half == second_half:
                    total_sum += num

    return total_sum

def solve_gift_shop_pt2():
    puzzle_input = """5529687-5587329,50-82,374-560,83-113,226375-287485,293169-368713,2034-2634,9945560-9993116,4872472-4904227,3218-5121,1074-1357,15451-26093,483468003-483498602,51513-85385,1466-1992,7600-13034,710570-789399,407363-480868,3996614725-3996662113,3-17,5414907798-5414992881,86274-120443,828669-909588,607353-700604,4242340614-4242556443,28750-44009,935177-1004747,20-41,74678832-74818251,8484825082-8484860878,2784096938-2784156610,5477-7589,621-952,2424167145-2424278200,147085-217900,93043740-93241586"""
    #test_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""
    ranges = puzzle_input.replace('\n', '').strip().split(',')
    
    total_sum = 0
    
    for r in ranges:
        start_str, end_str = r.split('-')
        start = int(start_str)
        end = int(end_str)
        
        for num in range(start, end + 1):
            s_num = str(num)
            result, pattern = rfun(s_num)
            if result and pattern is not None:
                repeated = pattern * (len(s_num) // len(pattern))
                if repeated == s_num:
                    total_sum += num                

    return total_sum


def rfun(s_num):
    length = len(s_num)
    if length == 0:
        return False, None
    if length % 2 != 0:
        return rfun(s_num[:length - 1])

    mid = length // 2
    first_half = s_num[:mid]
    second_half = s_num[mid:]

    if first_half != second_half:
        return rfun(s_num[:length - 1])
    else:
        for d in range(1, len(first_half) + 1):
            if len(first_half) % d == 0:
                unit = first_half[:d]
                if unit * (len(first_half) // d) == first_half:
                    return True, unit


if __name__ == "__main__":
    result = solve_gift_shop()
    print(f"La somma di tutti gli ID non validi è: {result}")
    result_pt2 = solve_gift_shop_pt2()
    print(f"La somma di tutti gli ID non validi (parte 2) è: {result_pt2}")
