#!/usr/bin/env python3
#=======================================================================
#
# mem_scrambling_test.py
# ----------------------
# Simple test of mem scarmbling function used in Tillitis TK1.
#
#
#=======================================================================

INT_MAX = 2**32 - 1


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_bin_input(filename):
    l = []
    with open(filename,'rb') as f:
        return f.read()

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def display_w32(filename):
    my_bin_data = get_bin_input(filename)
    print("type:", type(my_bin_data))
    print("length:", len(my_bin_data))

    for i in range(int(len(my_bin_data) / 4)):
        w = (my_bin_data[i] << 0  + \
             my_bin_data[i] << 8  + \
             my_bin_data[i] << 16 + \
             my_bin_data[i] << 24) % INT_MAX
        print("%010u" % w)
    pass

#-------------------------------------------------------------------
#-------------------------------------------------------------------
print("mem_scrambling_test")
print("===================")
display_w32("app.bin")


#=======================================================================
#=======================================================================
