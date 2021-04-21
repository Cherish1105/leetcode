#Here is the version which cause time exceed
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        visited = set()
        relations = defaultdict(set)
        for k, v in enumerate(routes):
            for stop in v:
                relations[stop].add(k)
        if source not in relations or target not in relations:
            return -1
        q = collections.deque()
        q.append(source)
        #buses = set()
        count = 0
        if source == target:
            return 0
        while q:
            count += 1
            for _ in range(len(q)):
                curr = q.popleft()
                #visited.add(curr)
                for bus in relations[curr]:
                    #buses.add(bus)
                    #把所有链接的bus 都加进来然后算个数应该不是最短路径
                    for i in routes[bus]:
                        if i == target:
                            return count
                        elif i not in visited:
                            q.append(i)
                            visited.add(curr)
        return -1
 #revised version by myself
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        visited = set()
        relations = defaultdict(set)
        for k, v in enumerate(routes):
            for stop in v:
                relations[stop].add(k)
        if source not in relations or target not in relations:
            return -1
        q = collections.deque()
        q.append(source)
        buses = set()
        count = 0
        if source == target:
            return 0
        while q:
            count += 1
            for _ in range(len(q)):
                curr = q.popleft()
                #visited.add(curr)
                for bus in relations[curr]:
                    if bus not in buses:
                        buses.add(bus)
                    #把所有链接的bus 都加进来然后算个数应该不是最短路径
                        for i in routes[bus]:
                            if i == target:
                                return count
                            elif i not in visited:
                                q.append(i)
                                visited.add(curr)
        return -1
 #Better solution by Lee
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        to_routes = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for j in route:
                to_routes[j].add(i)
        bfs = [(source, 0)]
        seen = set([S])
        for stop, bus in bfs:
            if stop == target: return bus
            for i in to_routes[stop]:
                for j in routes[i]:
                    if j not in seen:
                        bfs.append((j, bus + 1))
                        seen.add(j)
                routes[i] = []  # 这里避免里重复加入相同的bus,很巧妙
        return -1
