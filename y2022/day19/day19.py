import sys
import re
import heapq
from concurrent.futures import ProcessPoolExecutor
from collections import namedtuple

Blueprint = namedtuple('Blueprint',
                       'id ore_robot_ore clay_robot_ore obsidian_robot_ore obsidian_robot_clay geode_robot_ore geode_robot_obsidian')
State = namedtuple('State', 'ore clay obsidian geode ore_robots clay_robots obsidian_robots geode_robots')
INF = float('INF')


def step1(blueprints):
    result = 0
    with ProcessPoolExecutor(max_workers=16) as executor:
        futures = {}
        for blueprint in blueprints:
            futures[blueprint.id] = executor.submit(evaluate_blueprint, blueprint, 24)
        for blueprint in blueprints:
            result += blueprint.id * futures[blueprint.id].result()
    return result


def step2(blueprints):
    result = 1
    with ProcessPoolExecutor(max_workers=3) as executor:
        futures = []
        for blueprint in blueprints[0:3]:
            futures.append(executor.submit(evaluate_blueprint, blueprint, 32))
        for future in futures:
            result *= future.result()
    return result


def evaluate_blueprint(blueprint, time):
    pq = []
    heapq.heappush(pq, (0, 0, State(0, 0, 0, 0, 1, 0, 0, 0)))
    cache = {}
    result = 0
    while pq:
        _, minute, state = heapq.heappop(pq)
        new_ore = state.ore + state.ore_robots
        new_clay = state.clay + state.clay_robots
        new_obsidian = state.obsidian + state.obsidian_robots
        new_geode = state.geode + state.geode_robots
        prev = cache.get(state, INF)
        if prev <= minute:
            continue
        cache[state] = minute
        if minute == time:
            result = max(result, state.geode)
            continue
        if approximate_max(state, time - minute) <= result:
            continue

        if state.ore >= blueprint.ore_robot_ore and most_expensive_ore(blueprint) > state.ore_robots:
            new_state = State(new_ore - blueprint.ore_robot_ore,
                              new_clay,
                              new_obsidian,
                              new_geode,
                              state.ore_robots + 1,
                              state.clay_robots,
                              state.obsidian_robots,
                              state.geode_robots)
            heapq.heappush(pq, (rank_state(new_state), minute + 1, new_state))
        if state.ore >= blueprint.clay_robot_ore and most_expensive_clay(blueprint) > state.clay_robots:
            new_state = State(new_ore - blueprint.clay_robot_ore,
                              new_clay,
                              new_obsidian,
                              new_geode,
                              state.ore_robots,
                              state.clay_robots + 1,
                              state.obsidian_robots,
                              state.geode_robots)
            heapq.heappush(pq, (rank_state(new_state), minute + 1, new_state))
        if state.ore >= blueprint.obsidian_robot_ore \
                and state.clay >= blueprint.obsidian_robot_clay \
                and most_expensive_obsidian(blueprint) > state.obsidian_robots:
            new_state = State(new_ore - blueprint.obsidian_robot_ore,
                              new_clay - blueprint.obsidian_robot_clay,
                              new_obsidian,
                              new_geode,
                              state.ore_robots,
                              state.clay_robots,
                              state.obsidian_robots + 1,
                              state.geode_robots)
            heapq.heappush(pq, (rank_state(new_state), minute + 1, new_state))
        if state.ore >= blueprint.geode_robot_ore and state.obsidian >= blueprint.geode_robot_obsidian:
            new_state = State(new_ore - blueprint.geode_robot_ore,
                              new_clay,
                              new_obsidian - blueprint.geode_robot_obsidian,
                              new_geode,
                              state.ore_robots,
                              state.clay_robots,
                              state.obsidian_robots,
                              state.geode_robots + 1)
            heapq.heappush(pq, (rank_state(new_state), minute + 1, new_state))

        # new state when we build no new robots and just let existing robots accumulate
        new_state = State(new_ore,
                          new_clay,
                          new_obsidian,
                          new_geode,
                          state.ore_robots,
                          state.clay_robots,
                          state.obsidian_robots,
                          state.geode_robots)
        heapq.heappush(pq, (rank_state(new_state), minute + 1, new_state))
    return result


def approximate_max(state, rem_minutes):
    """
    Calculates and upper limit on best possible outcome from this state
    """
    upper_limit = state.geode
    geode_robots = state.geode_robots
    for i in range(0, rem_minutes):
        upper_limit += geode_robots
        geode_robots += 1
    return upper_limit


def rank_state(state):
    rank = 0
    rank += 10 * state.geode_robots
    rank += 5 * state.obsidian_robots
    rank += state.ore_robots
    rank += state.clay_robots
    return -rank


def most_expensive_clay(blueprint):
    return blueprint.obsidian_robot_clay


def most_expensive_ore(blueprint):
    return max(blueprint.ore_robot_ore,
               blueprint.clay_robot_ore,
               blueprint.obsidian_robot_ore,
               blueprint.geode_robot_ore)


def most_expensive_obsidian(blueprint):
    return blueprint.geode_robot_obsidian


def read_input():
    result = []
    for line in sys.stdin:
        expr = re.sub('\\s+', ' ', '''Blueprint (\\d+): 
                        Each ore robot costs (\\d+) ore. 
                        Each clay robot costs (\\d+) ore. 
                        Each obsidian robot costs (\\d+) ore and (\\d+) clay. 
                        Each geode robot costs (\\d+) ore and (\\d+) obsidian.''')
        [_id, ore, clay, obsidian_ore, obsidian_clay, geode_ore, geode_clay] = list(
            map(int, re.match(expr, line).groups()))
        result.append(Blueprint(_id, ore, clay, obsidian_ore, obsidian_clay, geode_ore, geode_clay))
    return result


if __name__ == '__main__':
    blueprints = read_input()
    print('This one is slow. Wait for it...', file=sys.stderr)
    print(step1(blueprints))
    print(step2(blueprints))
