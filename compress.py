def compress(string: str) -> str:
    """
    Compress string to format {letter}{quantity}
    Example: string: aaabbccccdaa, result: a3b2c4d1a2
    
    """
    if not string:
        return ""
    result = string[0]
    n = 0
    for letter in string:

        if result[-1] == letter:
            n += 1
        else:
            result += str(n)
            result += letter
            n = 1
    
    result += str(n)
            
    return result


TEST_CASES = [
    {"string": "abcd", "result": "a1b1c1d1"},
    {"string": "aaa", "result": "a3"},
    {"string": "", "result": ""},
    {"string": "aaabbccccdaa", "result": "a3b2c4d1a2"}
    ]

def test_compress():
    for case in TEST_CASES:
        assert compress(case["string"]) == case["result"]
        print("PASS")

#print(compress("aabbcccc"))
test_compress()
