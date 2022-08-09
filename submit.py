def check(files, func):
  for file in files:
    with open(file, 'r') as f:

      text = f.readlines()
      f.close()

    n = int(text[0].rstrip('\n').split(' ')[0])

    q = int(text[0].rstrip('\n').split(' ')[1])

    queries = []
    expected_result = int(text[-1].rstrip('\n').split(' ')[0])
    for i in range(1, len(text) -1 ):
        queries.append(list(map(int, text[i].rstrip().split())))

    result = func(n, queries)
    if result == expected_result:
      print(f'------- Test Case {file[-5]} Pass (✓)-------')
    else:
      print(f'------- Test Case {file[-5]} Failed (x) -------')