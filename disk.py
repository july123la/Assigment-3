import random
import sys
import matplotlib.pyplot as plt

MAX_CYLINDERS = 5000
REQUEST_COUNT = 1000


def fcfs(requests, head):
    movement = 0
    current = head
    trace = [current]
    
    for r in requests:
        movement += abs(current - r)
        current = r
        trace.append(current)

    return movement, trace


def scan(requests, head):
    movement = 0
    current = head
    trace = [current]
    left = []
    right = []

    for r in requests:
        if r < head:
            left.append(r)
        else:
            right.append(r)

    left.sort()
    right.sort()

    for r in right:
        movement += abs(current - r)
        current = r
        trace.append(current)

    if len(right) > 0:
        movement += abs(current - (MAX_CYLINDERS - 1))
        current = MAX_CYLINDERS - 1
        i = len(left) - 1
        trace.append(current)

        while(i >= 0):
            movement += abs(current - left[i])
            current = left[i]
            trace.append(current)
            i -= 1

    return movement, trace


def cscan(requests, head):
    movement = 0
    current = head
    trace = [current]

    left = []
    right = []

    for r in requests:
        if r < head:
            left.append(r)
        else:
            right.append(r)

    left.sort()
    right.sort()

    for r in right:
        movement += abs(current - r)
        current = r
        trace.append(current)

    if len(left) > 0:
        movement += abs(current - (MAX_CYLINDERS - 1))
        movement += (MAX_CYLINDERS - 1)  
        current = 0
        trace.append(current)

        for r in left:
            movement += abs(current - r)
            current = r
            trace.append(current)

    return movement, trace


def visualize(head):

    random.seed()
    requests = [random.randint(0, MAX_CYLINDERS - 1) for _ in range(REQUEST_COUNT)]

    fcfs_cost, fcfs_path = fcfs(requests, head)
    scan_cost, scan_path = scan(requests, head)
    cscan_cost, cscan_path = cscan(requests, head)

    plt.figure(figsize=(12, 6))
    plt.plot(fcfs_path, label="FCFS")
    plt.plot(scan_path, label="SCAN")
    plt.plot(cscan_path, label="C-SCAN")
    plt.title("Movimiento del Cabezal por Algoritmo")
    plt.xlabel("Número de solicitud")
    plt.ylabel("Cilindro visitado")
    plt.legend()
    plt.grid(True)
    plt.show()


    plt.figure(figsize=(10, 5))
    algorithms = ["FCFS", "SCAN", "C-SCAN"]
    values = [fcfs_cost, scan_cost, cscan_cost]
    plt.bar(algorithms, values)
    plt.title("Comparación de Movimiento Total del Cabezal")
    plt.ylabel("Movimiento total (cilindros)")
    plt.grid(axis="y")
    plt.show()

    responsiveness = [
        1 / fcfs_cost,
        1 / scan_cost,
        1 / cscan_cost
    ]

    plt.figure(figsize=(10, 5))
    plt.bar(algorithms, responsiveness)
    plt.title("Simulación de Responsiveness del Sistema")
    plt.ylabel("Valor relativo (1 / movimiento total)")
    plt.grid(axis="y")
    plt.show()

    print("\n--- MÉTRICAS ---")
    print(f"FCFS   movement: {fcfs_cost}")
    print(f"SCAN   movement: {scan_cost}")
    print(f"C-SCAN movement: {cscan_cost}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 disk.py <initial_head_position>")
        return

    head = int(sys.argv[1])

    if head < 0 or head >= MAX_CYLINDERS:
        print(f"Head position must be between 0 and {MAX_CYLINDERS - 1}")
        return
    
    visualize(head)


main()
