import collections
import generic_run

LABEL = 'June-16-01-current8'

param_sets = [[('random_seed', seed),
               ('max_length', 41),
               ('forward_max', 401),
               ('task', task),
               ]
              for seed in range(8)
              for task in ['badd']
              ]


param_sets = map(collections.OrderedDict, param_sets)
generic_run.parser.set_defaults(label=LABEL)

generic_run.main(param_sets)
