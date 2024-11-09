import math

def generate_codes(sf):
    level = int(math.log2(sf))
    dp = [[1]]
    for _ in range(level):
        codes = []
        for code in dp:
            c1 = code + code
            c2 = code + [0 if x == 1 else 1 for x in code]
            codes.append(c1)
            codes.append(c2)
        dp = codes
    return dp


def encode_data(num_users, data, codes):
    if num_users > len(codes):
        return None
    combinated_signal = [0]*len(codes[0])*len(data[0])

    midpoint = len(codes) // 2

    for i in range(num_users):
        user_data = data[i]
        spreading_message = []

        if i % 2 == 0:
            code_index = midpoint + (i // 2)
        else:
            code_index = midpoint - ((i + 1) // 2)

        code = codes[code_index]

        for j in range(len(user_data)):
            spreading_message.extend([a ^ b for a, b in zip(code, [user_data[j]]*len(codes[0]))])

        spreading_message_voltage = [1 if x == 0 else -1 for x in spreading_message]
        
        for j in range(len(spreading_message_voltage)):
            combinated_signal[j] += spreading_message_voltage[j]
    return combinated_signal
            

def decode_data(num_users, combinated_signal, codes):
    decoded_data = []
    midpoint = len(codes) // 2

    for i in range(num_users):
        users_data_decoded = []

        if i % 2 == 0:
            code_index = midpoint + (i // 2)
        else:
            code_index = midpoint - ((i + 1) // 2)

        code = codes[code_index]
        code_voltage = [1 if x == 0 else -1 for x in code]
        
        for j in range(len(combinated_signal)//len(codes[0])):
            bit_v = combinated_signal[j*len(codes[0]):(j+1)*len(codes[0])]
            prod = [a*b for a, b in zip(bit_v, code_voltage)]
            p = sum(prod)/len(codes[0])
            users_data_decoded.append(0 if p > 0 else 1)
        decoded_data.append(users_data_decoded)
    
    return decoded_data