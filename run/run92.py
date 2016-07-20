import collections
import generic_run

LABEL = 'June-27-05-semiedged2'

param_sets = [[('random_seed', seed),
               ('max_length', 41),
               ('forward_max', 401),
               ('input_height', 2),
               ('nmaps', nm),
               ('task', task),
               ('do_binarization', binarization),
               ]
              for seed in range(8)
              for task in ['baddet,badde']
              for nm in [24]
              for binarization in
              [1e-1, 0.0]
              ]


param_sets = map(collections.OrderedDict, param_sets)
generic_run.parser.set_defaults(label=LABEL)

generic_run.main(param_sets)
