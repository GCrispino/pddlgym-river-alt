import sys


def create_problem_description(location_string, connection_string,
                               is_river_string, is_waterfall_string,
                               is_bank_string, is_bridge_string, init_location_string,
                               goal_location):
    goal_string = f"(is-goal f{goal_location[0]}-{goal_location[1]}f)"

    return f"""
(define (problem river_alt) (:domain river_alt)
  (:objects
    {location_string}
    robot0 - robot
  )
  (:init
    {connection_string}

    {is_river_string}

    {is_waterfall_string}

    {is_bank_string}

    {is_bridge_string}

    (move down)
    (move left)
    (move right)
    (move up)

    {init_location_string}
    {goal_string}
  )
  (:goal (and
    (robot-at robot0 f{goal_location[0]}-{goal_location[1]}f)))
)
    """


def build_connection_string(nx, ny, river_locations, bank_locations,
                            bridge_locations):
    conns = []

    # river cells
    for x, y in river_locations:
        conns.append(f"(conn f{x}-{y}f f{x}-{y - 1}f up)")
        conns.append(f"(conn f{x}-{y}f f{x + 1}-{y}f right)")
        conns.append(f"(conn f{x}-{y}f f{x}-{y + 1}f down)")
        conns.append(f"(conn f{x}-{y}f f{x - 1}-{y}f left)")

    # bank cells
    for x, y in bank_locations:
        if x == 0:
            # left bank
            conns.append(f"(conn f{x}-{y}f f{x + 1}-{y}f right)")
        elif x == nx - 1:
            # right bank
            conns.append(f"(conn f{x}-{y}f f{x - 1}-{y}f left)")
        if y < ny - 1:
            conns.append(f"(conn f{x}-{y}f f{x}-{y + 1}f down)")
        if y > 0:
            conns.append(f"(conn f{x}-{y}f f{x}-{y - 1}f up)")
    # bridge cells
    for x, y in bridge_locations:
        conns.append(f"(conn f{x}-{y}f f{x}-{y + 1}f down)")
        if x < nx - 1:
            conns.append(f"(conn f{x}-{y}f f{x + 1}-{y}f right)")
        if x > 0:
            conns.append(f"(conn f{x}-{y}f f{x - 1}-{y}f left)")


    # bottom cells (y == ny - 1)
    for x in range(nx):
        conns.append(f"(conn f{x}-{ny - 1}f f{x}-{ny - 2}f up)")

    return "\n\t".join(conns)


if len(sys.argv) < 3:
    raise ValueError("Please pass x and y dimensions")

nx, ny = int(sys.argv[1]), int(sys.argv[2])
try:
    init_location = int(sys.argv[3])
except IndexError:
    #init_location = nx * (ny - 2) + 1
    init_location = (0, ny - 2)

# Define locations
river_locations = [(x, y) for x in range(1, nx - 1) for y in range(1, ny - 1)]
bridge_locations = [(x, 0) for x in range(1, nx - 1)]
waterfall_locations = [(x, ny - 1) for x in range(nx - 1)]
bank_locations = [(x, y) for x in (0, nx - 1)
                  for y in range(ny - 1)] + [(nx - 1, ny - 1)]

goal_location = (nx - 1, ny - 1)

# Build strings
river_string = "\n\t".join([f"(is-river f{x}-{y}f)" for (x, y) in river_locations])
waterfall_string = "\n\t".join([f"(is-waterfall f{x}-{y}f)" for (x, y) in waterfall_locations])
bank_string = "\n\t".join([f"(is-bank f{x}-{y}f)" for (x, y) in bank_locations])
bridge_string = "\n\t".join([f"(is-bridge f{x}-{y}f)" for (x, y) in bridge_locations])
init_location_string = f"(robot-at robot0 f{init_location[0]}-{init_location[1]}f)"

location_string = "\n\t".join([
    f"f{x}-{y}f - location"
    for (x, y) in sorted(river_locations + bridge_locations +
                         waterfall_locations + bank_locations)
])

connection_string = build_connection_string(nx, ny, river_locations,
                                            bank_locations, bridge_locations)

res_string = create_problem_description(location_string, connection_string,
                                        river_string, waterfall_string,
                                        bank_string, bridge_string,
                                        init_location_string, goal_location)

print(res_string)
