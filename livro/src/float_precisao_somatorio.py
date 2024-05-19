for x in (1, 3, 10, 100):
    print(f'$\\sum\\limits_{{i=1}}^{{{x}}}0.1 = {sum(0.1 for _ in range(x)):.28f}$\n')
