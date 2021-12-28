from collections import namedtuple

Packet = namedtuple('Packet', 'version type payload')
Operator = namedtuple('Operator', 'sub_packets')
Literal = namedtuple('Literal', 'value')


def step1(inp):
    packet, rem = parse(inp)
    return sum_versions(packet)


def sum_versions(packet):
    result = packet.version
    if isinstance(packet.payload, Operator):
        for sub_packet in packet.payload.sub_packets:
            result += sum_versions(sub_packet)
    return result


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


inp = ''.join([('0000' + bin(int(s, 16))[2:])[-4:] for s in input().strip()])
print(step1(inp))
