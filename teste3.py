import teste2

v1 = teste2.beam('5.C1',0.5,0.25,3)

# v1.add_pure_bending_moment(4,32)

v1.add_distributed_load([0, 0.9], [0, -4.38])
v1.add_distributed_load([0.9, 1.5], [-4.38, -4.38])
v1.add_distributed_load([1.5, 3], [-4.84, -4.84])

# v1.add_point_load(1, -10)
# v1.add_point_load(2.5, -15)

v1.add_point_support(0,5,2)
v1.add_point_support(3,7,1)

v1.info_beam()

v1.plot_load()
v1.plot_shear()
v1.plot_moment()