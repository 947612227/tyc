from deepdiff import DeepDiff

json_1 = {
  "repetition_change": {
    "root[0]": {
      "old_repeat": 2,
      "new_repeat": 1,
      "old_indexes": [
        0,
        3
      ],
      "new_indexes": [
        0
      ],
      "value": 1
    },
    "root[1]": {
      "old_repeat": 1,
      "new_repeat": 2,
      "old_indexes": [
        1
      ],
      "new_indexes": [
        1,
        3
      ],
      "value": 2
    }
  }
}
json_2 = {
  "repetition_change": {
    "root[0]": {
      "old_repeat": 2,
      "new_repeat": 1,
      "old_indexes": [
        0,
        3
      ],
      "new_indexes": [
        0
      ],
      "value": 1
    },
    "root[1]": {
      "old_repeat": 1,
      "new_repeat": 20,
      "old_indexes": [
        199
      ],
      "new_indexes": [
        1,
        3
      ],
      "value": 2
    }
  }
}

# exclude_paths = {忽略字段的地址}
# exclude_paths = [
#                     "root['repetition_change']['root[1]']['new_repeat']",
#                     "root['repetition_change']['root[1]']['old_indexes']"
#                  ]

res = DeepDiff(json_1, json_2, exclude_regex_paths=
["\['new_repeat'\]",        #第一个忽略的字段
 "\['old_indexes'\]"])      #第二个忽略的字段
print(res)
