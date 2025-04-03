import heapq

def match_requests(requests, sellers):
    # Dictonary to store the best seller for each request
    equipment_heap={}

    #Populate the heap with the sellers
    for equipment, price in sellers:
        if equipment not in equipment_heap:
            equipment_heap[equipment] = []
        heapq.heappush(equipment_heap[equipment], price)

        #process buyers req 
        result=[]
        for equipment, max_price in requests:
            if equipment in equipment_heap:
                while equipment_heap[equipment]:
                    lowest_price = heapq.heappop(equipment_heap[equipment])
                    if lowest_price <= max_price:
                        result.append(lowest_price)
                        break
                    else:
                        result.append(None)
                    
        return result

        #example
        requests = [('laptop', 1000), ('phone', 500)]
        sellers = [('laptop', 800), ('phone', 400), ('laptop', 900), ('phone', 600)]
        print(match_requests(requests, sellers))
        
