def print_result(func):
  def decorator(*args):
    print(func.__name__)
    result = func(*args)
    if (type(result) == list):
      print(*result, sep='\n')
    elif (type(result) == dict):
      for key in result.keys():
        print(key, '=', result[key])
    else:
      print(result)
    return result

  return decorator