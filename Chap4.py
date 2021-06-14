import time
start = time.time()
# 描述各节点、时间开销、父节点信息
# 创建节点信息，start起点，fin终点
graph = {
'1': {'2': 8, '3': 7, '6': 8}, 
'2': {'4': 5},
'3': {'5': 2, '7': 3}, 
'4': {'5': 1, '9': 12}, 
'5': {'9': 10, '3': 2},
'6': {'1': 8, '7': 9}, 
'7': {'5': 5, '8': 2, '6': 9}, 
'8': {'7': 2, '9': 2}, 
'9': {'5': 10}}

# 创建开销/时间表
infinity = float("inf") #无穷大
costs={'2':8,'3':7,'6':8,'9':infinity}
 # 路径中父节点信息
parents= {}
parents['2']='1'
parents['3']='1'
parents['6']='1'
parents['9']='5'
 
# 记录处理过的节点的数组
processed = []
 
# 定义寻找最小节点的函数
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:  # 遍历所有节点
        cost = costs[node]
        if cost < lowest_cost and node not in processed: # 如果当前节点的开销更低且未处理过
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
 
# 寻找最短路径
def find_shortest_path():
    node = '9'
    shortest_path = ['9']
    while parents[node] != '1':
        shortest_path.append(parents[node])
        node = parents[node]
    shortest_path.append('1')
    shortest_path.reverse()  # 将从终点到起点的路径反序表示
    return shortest_path
 
# 狄克斯特拉算法寻找最短路径
def dijkstra():
    node = find_lowest_cost_node(costs)  #在未处理的节点中找到开销最小的节点
    while node is not None:   # 所有节点都被处理过，node为None，循环结束
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():  # 遍历当前节点的所有邻居
            new_cost = cost + neighbors[n]
            try:
                if costs[n] > new_cost:  # 如果经当前节点前往该邻居更近
                    costs[n] = new_cost  # 就更新该邻居的开销
                    parents[n] = node  # 同时将该邻居的父节点设置为当前节点
            except:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)  # 将当前节点标记为处理过
        node = find_lowest_cost_node(costs)  # 找出接下来要处理的节点，并循环
    shortest_path = find_shortest_path()
    print('->'.join(shortest_path))
 
# 运行
dijkstra()
print(costs['9'])

end = time.time()
print("用时%ss"%(end-start))
