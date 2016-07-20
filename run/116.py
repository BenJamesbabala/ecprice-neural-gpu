import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import collections
from kube import run

LABEL = 'July-07-11-baseline'

param_sets = [[('random_seed', seed),
               ('nmaps', nm),
               ('task', task),
               ]
              for seed in range(3)
              for task in ['scopy', 'sdup', 'sbmul'] +
                          [x for y in ['sbadd', 'badd',
                                       'badde', 'sbadde',
                                       'baddz']
                           for x in ['%s,%st' % (y,y),
                                     '%st,%s' % (y,y)]]
              for nm in [24, 128]
              ]


param_sets = map(collections.OrderedDict, param_sets)
run.parser.set_defaults(label=LABEL)
#print len(param_sets)
run.main(param_sets)
