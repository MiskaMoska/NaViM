'''
Cast network routing path configuration
'''
W = 7 #cast network width
H = 8 #cast network height
RT_DEPTH = 16 #routing table depth
SID_WIDTH = 10 #data width of stream ID

PATH_DICT = dict()

# ----------------------------------------------------------------------------------------------------- example begin
# PATH_DICT['0,0'] = [(       2       ,       0       ,       0       ),(...),(...),...]
#             ^               ^               ^               ^                 ^
#       router position  input port      output port      stream ID        other paths
# ----------------------------------------------------------------------------------------------------- example end
# Note: A stream is a multicast tree, every multicast tree in the cast network has a unique stream ID.
# Port specification: 0-local, 1-west, 2-east, 3-vert0, 4-vert1.

# #test multicast
# PATH_DICT[(0,0)] = [(2,0,1)]
# PATH_DICT[(1,0)] = [(2,3,1),(2,1,1),(2,0,1)]
# PATH_DICT[(2,0)] = [(0,1,1),(0,3,1)]
# PATH_DICT[(0,1)] = [(2,0,1)]
# PATH_DICT[(1,1)] = [(3,1,1),(3,3,1)]
# PATH_DICT[(2,1)] = [(3,0,1)]
# PATH_DICT[(0,2)] = [(2,0,1)]
# PATH_DICT[(1,2)] = [(3,1,1),(3,0,1)]
# PATH_DICT[(2,2)] = []

# test dual-multicast
# PATH_DICT[(0,0)] = [(2,0,1)]
# PATH_DICT[(1,0)] = [(2,3,1),(2,1,1),(2,0,1),(0,2,2),(0,3,2)]
# PATH_DICT[(2,0)] = [(0,1,1),(0,3,1),(1,0,2)]
# PATH_DICT[(0,1)] = [(2,0,1)]
# PATH_DICT[(1,1)] = [(3,1,1),(3,3,1),(3,0,2),(3,3,2)]
# PATH_DICT[(2,1)] = [(3,0,1)]
# PATH_DICT[(0,2)] = [(2,0,1)]
# PATH_DICT[(1,2)] = [(3,1,1),(3,0,1),(3,2,2)]
# PATH_DICT[(2,2)] = [(1,0,2)]

# # test virtual vgg16
# PATH_DICT[(0,0)] = [(1,0,1023),(0,2,1)]
# PATH_DICT[(1,0)] = [(0,2,2),(1,0,1)]
# PATH_DICT[(2,0)] = [(0,2,3),(1,0,2)]
# PATH_DICT[(3,0)] = [(0,2,4),(1,0,3)]
# PATH_DICT[(4,0)] = [(0,2,5),(1,0,4)]
# PATH_DICT[(5,0)] = [(1,2,5),(1,0,5),(2,3,6)]
# PATH_DICT[(6,0)] = [(1,0,5),(0,1,6),(0,3,6)]
# PATH_DICT[(0,1)] = [(2,3,8),(2,0,8)]
# PATH_DICT[(1,1)] = [(2,3,9),(2,0,7),(0,1,8),(0,2,8)]
# PATH_DICT[(2,1)] = [(1,2,8),(2,1,7),(2,1,9),(2,3,9),(2,0,7)]
# PATH_DICT[(3,1)] = [(0,1,9),(0,2,9),(1,2,8),(1,4,8),(2,1,7),(2,0,7)]
# PATH_DICT[(4,1)] = [(1,2,9),(1,4,8),(2,1,7),(2,0,7)]
# PATH_DICT[(5,1)] = [(0,1,7),(1,2,9),(1,4,9),(3,0,6)]
# PATH_DICT[(6,1)] = [(1,4,9),(3,0,6)]
# PATH_DICT[(0,2)] = [(2,3,10),(3,0,8)]
# PATH_DICT[(1,2)] = [(0,1,10),(0,2,10),(2,3,11),(3,0,9)]
# PATH_DICT[(2,2)] = [(1,2,10),(2,1,11),(2,3,11),(3,0,9)]
# PATH_DICT[(3,2)] = [(1,2,10),(1,4,10),(2,1,11),(4,0,8)]
# PATH_DICT[(4,2)] = [(0,1,11),(0,2,11),(1,4,10),(4,0,8)]
# PATH_DICT[(5,2)] = [(1,2,11),(1,4,11),(4,0,9)]
# PATH_DICT[(6,2)] = [(1,4,11),(4,0,9)]
# PATH_DICT[(0,3)] = [(3,3,10),(3,0,10)]
# PATH_DICT[(1,3)] = [(2,3,12),(3,0,11)]
# PATH_DICT[(2,3)] = [(2,1,12),(2,3,12),(3,0,11)]
# PATH_DICT[(3,3)] = [(0,1,12),(0,2,12),(4,0,10)]
# PATH_DICT[(4,3)] = [(1,2,12),(4,0,10)]
# PATH_DICT[(5,3)] = [(1,2,12),(1,4,12),(4,0,11)]
# PATH_DICT[(6,3)] = [(1,4,12),(4,0,11)]
# PATH_DICT[(0,4)] = [(0,2,13),(2,3,14),(3,0,10)]
# PATH_DICT[(1,4)] = [(1,2,13),(2,1,14),(2,3,14),(3,0,12)]
# PATH_DICT[(2,4)] = [(0,1,14),(0,2,14),(1,2,13),(3,0,12)]
# PATH_DICT[(3,4)] = [(1,2,13),(1,2,14),(1,4,14),(1,0,13)]
# PATH_DICT[(4,4)] = [(1,2,13),(1,4,14),(1,0,13)]
# PATH_DICT[(5,4)] = [(1,2,13),(1,4,13),(4,0,12)]
# PATH_DICT[(6,4)] = [(1,4,13),(4,0,12)]
# PATH_DICT[(0,5)] = [(3,0,14)]
# PATH_DICT[(1,5)] = [(3,0,14)]
# PATH_DICT[(2,5)] = [(2,3,15),(2,0,15)]
# PATH_DICT[(3,5)] = [(2,1,15),(4,0,14)]
# PATH_DICT[(4,5)] = [(2,1,15),(4,0,14)]
# PATH_DICT[(5,5)] = [(0,1,15),(4,0,13)]
# PATH_DICT[(6,5)] = [(4,0,13)]
# PATH_DICT[(0,6)] = [(0,2,16),(2,0,15)]
# PATH_DICT[(1,6)] = [(2,1,15),(2,0,15),(1,2,16)]
# PATH_DICT[(2,6)] = [(0,2,17),(1,2,16),(3,1,15),(3,0,15)]
# PATH_DICT[(3,6)] = [(1,2,16),(1,0,16),(1,4,17)]
# PATH_DICT[(4,6)] = [(1,2,16),(1,0,16)]
# PATH_DICT[(5,6)] = [(1,2,16),(1,0,16)]
# PATH_DICT[(6,6)] = [(1,0,16)]
# PATH_DICT[(0,7)] = []
# PATH_DICT[(1,7)] = []
# PATH_DICT[(2,7)] = []
# PATH_DICT[(3,7)] = [(4,2,17),(4,0,17),(0,3,1022)]
# PATH_DICT[(4,7)] = [(1,2,17),(1,0,17)]
# PATH_DICT[(5,7)] = [(1,2,17),(1,0,17),(0,3,1022)]
# PATH_DICT[(6,7)] = [(1,0,17)]

# test virtual vgg16 v2
PATH_DICT[(0,0)] = [(1,0,1023),(0,2,1)]
PATH_DICT[(1,0)] = [(0,2,2),(1,0,1)]
PATH_DICT[(2,0)] = [(0,2,3),(1,0,2)]
PATH_DICT[(3,0)] = [(0,2,4),(1,0,3)]
PATH_DICT[(4,0)] = [(0,2,5),(1,0,4)]
PATH_DICT[(5,0)] = [(1,2,5),(1,0,5),(2,3,6)]
PATH_DICT[(6,0)] = [(1,0,5),(0,1,6),(0,3,6)]
PATH_DICT[(0,1)] = [(2,3,8),(2,0,8)]
PATH_DICT[(1,1)] = [(2,3,9),(2,0,7),(0,1,8),(0,2,8)]
PATH_DICT[(2,1)] = [(1,2,8),(2,1,7),(2,1,9),(2,3,9),(2,0,7)]
PATH_DICT[(3,1)] = [(0,1,9),(0,2,9),(1,2,8),(1,4,8),(2,1,7),(2,0,7)]
PATH_DICT[(4,1)] = [(1,2,9),(1,4,8),(2,1,7),(2,0,7)]
PATH_DICT[(5,1)] = [(0,1,7),(1,2,9),(1,4,9),(3,0,6)]
PATH_DICT[(6,1)] = [(1,4,9),(3,0,6)]
PATH_DICT[(0,2)] = [(2,3,10),(3,0,8)]
PATH_DICT[(1,2)] = [(0,1,10),(0,2,10),(2,3,11),(3,0,9)]
PATH_DICT[(2,2)] = [(1,2,10),(2,1,11),(2,3,11),(3,0,9)]
PATH_DICT[(3,2)] = [(1,2,10),(1,4,10),(2,1,11),(4,0,8)]
PATH_DICT[(4,2)] = [(0,1,11),(0,2,11),(1,4,10),(4,0,8)]
PATH_DICT[(5,2)] = [(1,2,11),(1,4,11),(4,0,9)]
PATH_DICT[(6,2)] = [(1,4,11),(4,0,9)]
PATH_DICT[(0,3)] = [(3,3,10),(3,0,10)]
PATH_DICT[(1,3)] = [(2,3,12),(3,0,11)]
PATH_DICT[(2,3)] = [(2,1,12),(2,3,12),(3,0,11)]
PATH_DICT[(3,3)] = [(0,1,12),(0,2,12),(4,0,10)]
PATH_DICT[(4,3)] = [(1,2,12),(4,0,10)]
PATH_DICT[(5,3)] = [(1,2,12),(1,4,12),(4,0,11)]
PATH_DICT[(6,3)] = [(1,4,12),(4,0,11)]
PATH_DICT[(0,4)] = [(0,2,13),(3,0,10)]
PATH_DICT[(1,4)] = [(1,2,13),(2,3,14),(3,0,12)]
PATH_DICT[(2,4)] = [(1,2,13),(3,0,12)]
PATH_DICT[(3,4)] = [(1,2,13),(1,0,13),(2,1,14),(2,3,14)]
PATH_DICT[(4,4)] = [(0,1,14),(0,3,14),(1,2,13),(1,0,13)]
PATH_DICT[(5,4)] = [(1,2,13),(1,4,13),(4,0,12)]
PATH_DICT[(6,4)] = [(1,4,13),(4,0,12)]
PATH_DICT[(0,5)] = [(2,0,14)]
PATH_DICT[(1,5)] = [(3,0,14),(3,1,14)]
PATH_DICT[(2,5)] = [(2,3,15),(2,0,15)]
PATH_DICT[(3,5)] = [(2,1,15),(3,0,14)]
PATH_DICT[(4,5)] = [(2,1,15),(3,0,14)]
PATH_DICT[(5,5)] = [(0,1,15),(4,0,13)]
PATH_DICT[(6,5)] = [(4,0,13)]
PATH_DICT[(0,6)] = [(0,2,16),(2,0,15)]
PATH_DICT[(1,6)] = [(2,1,15),(2,0,15),(1,2,16)]
PATH_DICT[(2,6)] = [(0,2,17),(1,2,16),(3,1,15),(3,0,15)]
PATH_DICT[(3,6)] = [(1,2,16),(1,0,16),(1,4,17)]
PATH_DICT[(4,6)] = [(1,2,16),(1,0,16)]
PATH_DICT[(5,6)] = [(1,2,16),(1,0,16)]
PATH_DICT[(6,6)] = [(1,0,16)]
PATH_DICT[(0,7)] = []
PATH_DICT[(1,7)] = []
PATH_DICT[(2,7)] = []
PATH_DICT[(3,7)] = [(4,2,17),(4,0,17),(0,3,1022)]
PATH_DICT[(4,7)] = [(1,2,17),(1,0,17)]
PATH_DICT[(5,7)] = [(1,2,17),(1,0,17),(0,3,1022)]
PATH_DICT[(6,7)] = [(1,0,17)]


