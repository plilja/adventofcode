from collections import namedtuple

Packet = namedtuple('Packet', 'version type payload')
Operator = namedtuple('Operator', 'sub_packets')
Literal = namedtuple('Literal', 'value')


def step1(inp):
    packet = parse(inp)
    return sum_versions(packet)


def step2(inp):
    packet = parse(inp)
    return calculate_value(packet)


def sum_versions(packet):
    result = packet.version
    if packet.type != 4:
        for sub_packet in packet.payload.sub_packets:
            result += sum_versions(sub_packet)
    return result


def calculate_value(packet):
    if packet.type == 4:
        return packet.payload.value
    elif packet.type == 0:
        return sum(map(calculate_value, packet.payload.sub_packets))
    elif packet.type == 1:
        result = 1
        for sub_packet in packet.payload.sub_packets:
            result *= calculate_value(sub_packet)
        return result
    elif packet.type == 2:
        return min(map(calculate_value, packet.payload.sub_packets))
    elif packet.type == 3:
        return max(map(calculate_value, packet.payload.sub_packets))
    else:
        assert packet.type in [5, 6, 7]
        assert len(packet.payload.sub_packets) == 2
        a = calculate_value(packet.payload.sub_packets[0])
        b = calculate_value(packet.payload.sub_packets[1])
        if packet.type == 5:
            return 1 if a > b else 0
        elif packet.type == 6:
            return 1 if a < b else 0
        elif packet.type == 7:
            return 1 if a == b else 0


def parse(inp):
    version = parse_integer(inp, 3)
    type_id = parse_integer(inp, 3)
    if type_id == 4:
        payload = parse_literal(inp)
    else:
        payload = parse_operator(inp)
    return Packet(version, type_id, payload)


def parse_literal(inp):
    s = ''
    while True:
        bit = parse_integer(inp, 1)
        s += pop(inp, 4)
        if bit == 0:
            break
    return Literal(int(s, 2))


def parse_operator(inp):
    length_type_id = pop(inp, 1)
    if length_type_id == '0':
        n = parse_integer(inp, 15)
        rem = list(pop(inp, n))
        sub_packets = []
        while '1' in rem:
            sub_packet = parse(rem)
            sub_packets.append(sub_packet)
        return Operator(sub_packets)
    else:
        assert length_type_id == '1'
        n = parse_integer(inp, 11)
        sub_packets = []
        for i in range(0, n):
            sub_packet = parse(inp)
            sub_packets.append(sub_packet)
        return Operator(sub_packets)


def parse_integer(inp, n):
    return int(pop(inp, n), 2)


def pop(inp, n):
    result = ''
    for i in range(0, n):
        result += inp.pop(0)
    return result


def to_bin(hex_val):
    return list(''.join([('0000' + bin(int(s, 16))[2:])[-4:] for s in hex_val.strip()]))


decoded = to_bin(input())
print(step1(decoded[::]))
print(step2(decoded[::]))
