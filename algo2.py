#!/usr/bin/env python3
'''For Project 3 - Algorithm 2'''

def max_appreciation(values):
    if not values or len(values) < 2:
        return 0
    
    min_price = values[0]
    best_profit = 0
    
    for price in values[1:]:
        profit = price - min_price
        if profit > best_profit:
            best_profit = profit
        if price < min_price:
            min_price = price
    
    return best_profit


def main():
    # Sample input #1
    print(f'Sample Output #1: {max_appreciation([7, 1, 5, 3, 6, 4])} expected: 5')

    # Sample input #2
    print(f'Sample Output #2: {max_appreciation([9, 8, 6, 3, 1])} expected: 0')


if __name__ == "__main__":
    main()