import json
import sys

from python_fp.print_result import print_result
from python_fp.cm_timer import cm_timer_1
from python_fp.sort import sort
from python_fp.random import gen_random
from python_fp.unique import Unique
from python_fp.field import field

path = r"./db.json"

with open(path, encoding='utf-8') as f:
  data = json.load(f)

@print_result
def f1(arg):
  return sorted(
    Unique(
      (x['job-name'] for x in list(field(arg, 'job-name'))[0]),
      ignore_case=True
    )
  )

@print_result
def f2(arg):
  return filter(lambda x: x.lower().startswith('программист'), arg)

@print_result
def f3(arg):
  return list(map(lambda x: x + ' с опытом Python', arg))

@print_result
def f4(arg):
  salary = list(gen_random(len(arg), 100000, 200000))
  work = list(zip(arg, salary))
  return list(map(lambda x: x[0] + ', зарплата ' + str(x[1]) + ' руб.', work))


def main():
    print('\tproccess_data.py')
    with cm_timer_1():
        print(f4(f3(f2(f1(data)))))

if __name__ == "__main__":
    main()