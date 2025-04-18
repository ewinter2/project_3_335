#!/usr/bin/env python3
'''For Project 3 - Algorithm 1'''

def max_total_charm(num_of_beads, braclet_weight, 
                    bead_weights, charm_values):
    '''
    Select any combination of beads such that:
      - The sum of their masses is less than or equal to W
      - The total charm of the bracelet is maximized
    '''
    # Initialize a DP array with size (braclet_weight + 1)
    dp = [0] * (braclet_weight + 1)

    # Fill the DP array
    for w in range(1, braclet_weight + 1):
        for i in range(num_of_beads):
            if bead_weights[i] <= w:
                dp[w] = max(dp[w], dp[w - bead_weights[i]] + charm_values[i])

    # The maximum charm value is stored in dp[braclet_weight]
    return dp[braclet_weight]

    
def main():
    '''Main function to run the algorithm'''
    
    #Sample input #1
    n = 3
    W = 10
    w = [2, 3, 5]
    v = [3.0, 4.0, 7.5]
    print(f'Sample output #1: {max_total_charm(n, W, w, v)} expected: 15.0')

    #Sample input #2
    n = 3
    W = 7
    w = [2, 3, 4]
    v = [3.0, 4.0, 5.0]
    print(f'Sample output #2: {max_total_charm(n, W, w, v)} expected: 12.0')

    #input #3 
    n = 3 
    W = 13
    w = [2, 3, 4]
    v = [1.0, 4.0, 5.0]
    print(f'Sample output #3: {max_total_charm(n, W, w, v)} expected: 17.0')


if __name__ == "__main__":
    main()