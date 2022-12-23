per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
revenue = []
deposit = int(input('Enter your deposit: '))

for value in per_cent.values():
    value = deposit / 100 * value
    revenue.append(int(value))
print(f'An annual income is {revenue}')

max_revenue = max(revenue)
print(f'Your maximal revenue is {max_revenue}')


