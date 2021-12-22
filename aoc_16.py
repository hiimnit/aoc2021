from math import prod


input = '620D49005AD2245800D0C9E72BD279CAFB0016B1FA2B1802DC00D0CC611A47FCE2A4ACE1DD144BFABBFACA002FB2C6F33DFF4A0C0119B169B013005F003720004263644384800087C3B8B51C26B449130802D1A0068A5BD7D49DE793A48B5400D8293B1F95C5A3005257B880F5802A00084C788AD0440010F8490F608CACE034401AB4D0F5802726B3392EE2199628CEA007001884005C92015CC8051800130EC0468A01042803B8300D8E200788018C027890088CE0049006028012AB00342A0060801B2EBE400424933980453EFB2ABB36032274C026E4976001237D964FF736AFB56F254CB84CDF136C1007E7EB42298FE713749F973F7283005656F902A004067CD27CC1C00D9CB5FDD4D0014348010C8331C21710021304638C513006E234308B060094BEB76CE3966AA007C6588A5670DC3754395485007A718A7F149CA2DD3B6E7B777800118E7B59C0ECF5AE5D3B6CB1496BAE53B7ADD78C013C00CD2629BF5371D1D4C537EA6E3A3E95A3E180592AC7246B34032CF92804001A1CCF9BA521782ECBD69A98648BC18025800F8C9C37C827CA7BEFB31EADF0AE801BA42B87935B8EF976194EEC426AAF640168CECAF84BC004AE7D1673A6A600B4AB65802D230D35CF81B803D3775683F3A3860087802132FB32F322C92A4C402524F2DE006E8000854378F710C0010D8F30FE224AE428C015E00D40401987F06E3600021D0CE3EC228DA000574E4C3080182931E936E953B200BF656E15400D3496E4A725B92998027C00A84EEEE6B347D30BE60094E537AA73A1D600B880371AA36C3200043235C4C866C018E4963B7E7AA2B379918C639F1550086064BB148BA499EC731004E1AC966BDBC7646600C080370822AC4C1007E38C428BE0008741689D0ECC01197CF216EA16802D3748FE91B25CAF6D5F11C463004E4FD08FAF381F6004D3232CC93E7715B463F780'


class Packet:
    def __init__(self, version: int, type_id: int) -> None:
        self.version = version
        self.type_id = type_id

    def sum_versions(self) -> int:
        raise NotImplementedError()

    def calc(self) -> int:
        raise NotImplementedError()

class Literal(Packet):
    def __init__(self, version: int, type_id: int, value: int) -> None:
        super().__init__(version, type_id)
        self.value = value

    def __repr__(self) -> str:
        return f'<Literal: v={self.version} t={self.type_id} value={self.value}>'

    def sum_versions(self) -> int:
        return self.version

    def calc(self) -> int:
        return self.value

class Operation(Packet):
    def __init__(self, version: int, type_id: int) -> None:
        super().__init__(version, type_id)
        self.subpackets: list[Packet] = []

    def __repr__(self) -> str:
        return f'<Operation: v={self.version} t={self.type_id} sp={len(self.subpackets)}>'

    def sum_versions(self) -> int:
        return self.version + sum(packet.sum_versions() for packet in self.subpackets)

    def calc(self) -> int:
        if self.type_id == 0:
            return sum(p.calc() for p in self.subpackets)
        if self.type_id == 1:
            return prod(p.calc() for p in self.subpackets)
        if self.type_id == 2:
            return min(p.calc() for p in self.subpackets)
        if self.type_id == 3:
            return max(p.calc() for p in self.subpackets)
        if self.type_id == 5:
            return 1 if self.subpackets[0].calc() > self.subpackets[1].calc() else 0
        if self.type_id == 6:
            return 1 if self.subpackets[0].calc() < self.subpackets[1].calc() else 0
        if self.type_id == 7:
            return 1 if self.subpackets[0].calc() == self.subpackets[1].calc() else 0
        raise NotImplementedError()
        

def bits_iterator(input: str):
    for c in input:
        yield int(c, base=16)

class Converter:
    def __init__(self, input: str) -> None:
        self.iterator = bits_iterator(input)
        self.buffered_bits = 0
        self.buffered_value = 0

    def get(self, n: int):
        while self.buffered_bits < n:
            i = next(self.iterator)
            if i is None:
                raise Exception('Unexpected EOS')

            self.buffered_value = (self.buffered_value << 4) + i
            self.buffered_bits += 4

        offset = self.buffered_bits - n
        mask = (pow(2, n) - 1) << offset
        value = self.buffered_value & mask 

        self.buffered_bits -= n 
        self.buffered_value -= value

        value = value >> offset
        return value

def parse_packet(converter: Converter) -> tuple[int, Packet]:
    version = converter.get(3)
    type_id = converter.get(3)
    if type_id == 4:
        return parse_literal(converter, version, type_id)
    else:
        return parse_operation(converter, version, type_id)

def parse_operation(converter: Converter, version: int, type_id: int) -> tuple[int, Packet]:
    op = Operation(version, type_id)
    total_bit_count = 0

    length_type = converter.get(1)
    total_bit_count += 1
    if length_type == 0:
        length = converter.get(15)
        total_bit_count += 15
        subpacket_bit_count = 0
        while subpacket_bit_count < length:
            bit_count, packet = parse_packet(converter)
            subpacket_bit_count += bit_count
            op.subpackets.append(packet)
        total_bit_count += subpacket_bit_count
    else:
        number_of_packets = converter.get(11)
        total_bit_count += 11
        for _ in range(number_of_packets):
            bit_count, packet = parse_packet(converter)
            total_bit_count += bit_count
            op.subpackets.append(packet)

    return 7 + total_bit_count, op

def parse_literal(converter: Converter, version: int, type_id: int) -> tuple[int, Packet]:
    value = 0
    bit_count = 0
    while True:
        bits = converter.get(5)
        bit_count += 5
        value = (value << 4) + (bits & 0b1111)
        if (bits & 0b10000) != 0b10000:
            break

    literal = Literal(version, type_id, value)
    return 6 + bit_count, literal

if __name__ == '__main__':
    # part 1
    converter = Converter(input)

    bit_count, packet = parse_packet(converter)

    print('result=', packet.sum_versions())

    # part 2
    print('result=', packet.calc())

