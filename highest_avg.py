# -*- coding: utf-8 -*-

country_list = {}
final_result = {}
def highest_avg(str):
    for list1 in str:
        if country_list.keys():
            if list1[0] in country_list.keys():
                country_list[list1[0]].append(list1[1])
            else:
                country_list.update({list1[0]: [list1[1]]})
        else:
            country_list.update({list1[0]: [list1[1]]})
    for key, value in country_list.iteritems():
        final_result.update({key: sum(value)})
    d3 = max(final_result, key=lambda key : final_result[key])
    return d3

highest_avg([
    ["P", 81],
    ["P", 57],
    ["I", 53],
    ["I", 7],
    ["A", 31],
    ["I", 22],
    ["P", 125],
])