from collections import deque

def find_nearest_provider(n, edges,availabilty,
    start_provider, target_eqipment):
    graph = {i: [] for i in range(1, n+1)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

        queue = deque([(start_provider, 0)])  
        visited = set([start_provider])

        while queue:
            provider,distance = queue.popleft()

            if target_eqipment in availabilty[provider]:
                return provider, distance

            for neighbor in graph.get[provider]:
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))
                    visited.add(neighbor)

                    return None, -1  # If no provider is found, return None and -1

      #  example 

        n= 5 
        edges = [(1, 2), (2, 3), (3, 4), (4, 5)]
        availabilty = {
            1: ['laptop', 'phone'],
            2: ['tablet'],
            3: ['laptop'],
            4: ['phone'],
            5: ['tablet']
        }

        start_provider = 1
        target_eqipment = 'phone'

        provider, distance = find_nearest_provider(n, edges, availabilty, start_provider, target_eqipment)
        print(f"The nearest provider that can repair {target_eqipment} is provider {provider} at a distance of {distance} units.")

