
def divide(data, poly):
    n = len(poly)
    data = list(data)

    for i in range(len(data) - n + 1):
        if data[i] == '1':
            for j in range(n):
                data[i + j] = '0' if data[i + j] == poly[j] else '1'

    return ''.join(data[-(n - 1):])


def CRC(msg, poly):
    data = ""

    for c in msg:
        data += format(ord(c), '08b')

    r = len(poly) - 1
    appended = data + '0' * r

    rem = divide(appended, poly)
    codeword = data + rem

    print("\nPolynomial :", poly)
    print("Data       :", data)
    print("CRC        :", rem)
    print("Codeword   :", codeword)


msg = input("Enter data: ")

# CRC-12
crc12 = "1100000001111"

# CRC-16
crc16 = "11000000000000101"

# CRC-CCITT
crcCCITT = "10001000000100001"

CRC(msg, crc12)
CRC(msg, crc16)
CRC(msg, crcCCITT)
