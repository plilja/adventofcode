from collections import namedtuple

Packet = namedtuple('Packet', 'version type payload')
Operator = namedtuple('Operator', 'sub_packets')
Literal = namedtuple('Literal', 'value')


def step1(inp):
    packet, rem = parse(inp)
    return sum_versions(packet)


def step2(inp):
    packet, rem = parse(inp)
    return calculate_value(packet)


def sum_versions(packet):
    result = packet.version
    if isinstance(packet.payload, Operator):
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
    version = int(inp[:3], 2)
    type_id = int(inp[3:6], 2)
    if type_id == 4:
        packet, rem = parse_literal(inp[6:])
    else:
        packet, rem = parse_operator(inp[6:])
    return Packet(version, type_id, packet), rem


def parse_literal(inp):
    def helper(s):
        if s[0] == '0':
            return s[1:5], s[5:]
        else:
            s2, rem = helper(s[5:])
            return s[1:5] + s2, rem
    s, rem = helper(inp)
    return Literal(int(s, 2)), rem


def parse_operator(inp):
    length_type_id = inp[0]
    if length_type_id == '0':
        n = int(inp[1:16], 2)
        rem = inp[16:16+n]
        sub_packets = []
        while '1' in rem:
            sub_packet, rem = parse(rem)
            sub_packets.append(sub_packet)
        return Operator(sub_packets), inp[16 + n:]
    else:
        assert length_type_id == '1'
        n = int(inp[1:12], 2)
        rem = inp[12:]
        sub_packets = []
        for i in range(0, n):
            sub_packet, rem = parse(rem)
            sub_packets.append(sub_packet)
        return Operator(sub_packets), rem


def to_bin(hex_val):
    return ''.join([('0000' + bin(int(s, 16))[2:])[-4:] for s in hex_val.strip()])


decoded = to_bin(input())
print(step1(decoded))
print(step2(decoded))
