roadmap = {1: {2:8, 3:7,6:8}, 2: {4:5}, 3: {5:2,7:3},
4:{5:1,9:12},5:{3:2,9:10},6:{1:8,7:9},7:{6:9,5:7,8:2},8:{7:2,9:2}}
dis = {2: 8, 3: 7, 4: 666, 5: 666, 6: 8,7:666,8:666,9:666}
parents_node = {3:1 }
passed = []

min_dis = None
min_dis_point = None
for i in range(len(dis)):
    sort_dis = sorted(dis.items(), key=lambda item: item[1])
    # 找到dis中距离起始点距离最小的点
    for p, d in sort_dis:
        if p not in passed:
            min_dis_point = p
            min_dis = d
            passed.append(p)
            break
    try:
        # 更新相邻点的开销
        for n in roadmap[min_dis_point].keys():
            update = min_dis+roadmap[min_dis_point][n]
            if dis[n] > update:
                dis[n] = update
                parents_node[n] = min_dis_point
    except:  # 最后一个点有进没出
        pass

travel = ''
for node, parents in parents_node.items():
    travel += str(parents)+'->'+str(node)+'->'+'\n'
print(dis)
print(travel)

# {节点：{相邻点：权重}}

