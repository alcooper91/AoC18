import re
from collections import defaultdict
claims = open("Input.txt", "r").read().splitlines()
# #1 @ 16,576: 17x14
reg = re.compile(r"#(?P<claim>\d*) @ (?P<x_val>\d*),(?P<y_val>\d*): (?P<x_width>\d*)x(?P<y_width>\d*)")

fabric = defaultdict(int)

for claim in claims:
    details = reg.search(claim).groupdict()
    x_val, y_val, x_width, y_width = int(details['x_val']), int(details['y_val']), int(details['x_width']), int(details['y_width'])
    for x in range(x_val, x_val + x_width):
        for y in range(y_val, y_val + y_width):
            fabric[(x, y)] += 1

ans = 0
for (x,y),v in fabric.items():
    if v > 1:
        ans += 1

print(ans)

for claim in claims:
    details = reg.search(claim).groupdict()
    x_val, y_val, x_width, y_width = int(details['x_val']), int(details['y_val']), int(details['x_width']), int(details['y_width'])
    safe_claim = True
    for x in range(x_val, x_val + x_width):
        for y in range(y_val, y_val + y_width):
            if fabric[(x, y)] != 1:
                safe_claim = False
                break
        if not safe_claim:
            break
    
    if safe_claim:
        print(details['claim'])