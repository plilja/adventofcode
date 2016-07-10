import sys

class Boss:
    def __init__(self, hp, damage):
        self.hp = hp
        self.damage = damage

class Player:
    def __init__(self, hp, mana, armor):
        self.hp = hp
        self.mana = mana
        self.armor = armor

class Effect:
    def __init__(self, f, dur):
        self.f = f
        self.dur = dur

    def apply(self, player, boss):
        if self.dur > 0:
            player_, boss_ = self.f(player, boss)
        else:
            player_, boss_ = player, boss
        return (Effect(self.f, self.dur - 1), player_, boss_)

    def active(self):
        return self.dur > 0


class Shield:
    def __init__(self, dur):
        self.dur = dur

    def apply(self, p, b):
        if self.dur == 7:
            return (Shield(6), Player(p.hp, p.mana, p.armor + 7), b)
        elif self.dur == 1:
            return (Shield(0), Player(p.hp, p.mana, p.armor - 7), b)
        else:
            return (Shield(self.dur - 1), p, b)

    def active(self):
        return self.dur > 0


def inflict_damage(character, damage):
    if isinstance(character, Boss):
        return Boss(character.hp - damage, character.damage)
    else:
        assert isinstance(character, Player)
        return Player(character.hp - damage, character.mana, character.armor)


def magic_missile(player, boss):
    return (player, inflict_damage(boss, 4))


def drain(player, boss):
    return (Player(player.hp + 2, player.mana, player.armor), inflict_damage(boss, 2))


def poison(player, boss):
    return (player, inflict_damage(boss, 3))


def recharge(player, boss):
    return (Player(player.hp, player.mana + 101, player.armor), boss)


def spells():
    return [('magic_missile', 53, lambda: Effect(magic_missile, 1)), 
            ('drain', 73, lambda: Effect(drain, 1)),
            ('shield', 113, lambda: Shield(7)),
            ('poison', 173, lambda: Effect(poison, 6)),
            ('recharge', 229, lambda: Effect(recharge, 5))]


def solve(boss, turn_cost):
    def apply_spells(player, boss, avail_spells, act_spells):
        act_spells_ = {}
        for k, s in act_spells.items():
            s_, player, boss = s.apply(player, boss)
            if s_.active():
                act_spells_[k] = s_
        return (player, boss, act_spells_)


    def boss_turn(player, boss, avail_spells, act_spells, best):
        player, boss, act_spells = apply_spells(player, boss, avail_spells, act_spells)
        if boss.hp <= 0:
            return 0
        else:
            player = Player(player.hp - max(1, boss.damage - player.armor), player.mana, player.armor)
            if player.hp <= 0:
                return float('inf')
            else:
                return player_turn(player, boss, avail_spells, act_spells, best)


    def player_turn(player, boss, avail_spells, act_spells, best):
        player = inflict_damage(player, turn_cost)
        if player.hp <= 0:
            return float('inf')
        player, boss, act_spells = apply_spells(player, boss, avail_spells, act_spells)
        if boss.hp <= 0:
            return 0

        ans = best 
        for name, cost, factory in avail_spells:
            if cost <= player.mana and name not in act_spells and cost < best:
                p = Player(player.hp, player.mana - cost, player.armor)
                s = factory()
                act_spells[name] = s
                ans = min(ans, cost + boss_turn(p, boss, avail_spells, act_spells, ans - cost))
                act_spells.pop(name)

        return ans

    p = Player(50, 500, 0)
    return player_turn(p, boss, spells(), {}, float('inf'))


def read_boss():
    line = sys.stdin.readline
    [_, _, hp] = line().split()
    [_, damage] = line().split()
    return Boss(int(hp), int(damage))


boss = read_boss()
print('Step 1:', solve(boss, 0))
print('Step 2:', solve(boss, 1))
