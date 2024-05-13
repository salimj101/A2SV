# Read input
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Initialize a set to store non-zero elements
non_zero_elements = set()

# Add all non-zero elements to the set
for ai in a:
    if ai != 0:
        non_zero_elements.add(ai)

# Sort the set to get the minimum non-zero element
sorted_elements = sorted(non_zero_elements)

# Perform k operations
for _ in range(k):
    if sorted_elements:
        # Print the minimum non-zero element
        print(sorted_elements[0])
        # Subtract the minimum non-zero element from all non-zero elements
        sorted_elements = [max(0, ai - sorted_elements[0]) for ai in sorted_elements]
    else:
        # All elements are zeros, so print 0
        print(0)
