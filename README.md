List
---

Sorting a multidimensional array
```python
sorted_array = sorted(array,key=lambda x: x[column_index_that_has_to_be_sorted])
```
Reversing a array using slicing
```python
array = array[::-1]
```
Removing an element from an array
```python
popped_number  = array.pop(index) # by default it will remove last element
```
Insert an element into an array
```python
array.insert(index, element) # index has to provided for insert function, Return None so dont assign it to anything
array.append(element) # appends at the end only, Return None so dont assign it to anything
```
Modifying an element in an array based on index
```python
array[i] = some_other_number
```

Dict
---

Initializing a defaultdict
```python
dict_created = defaultdict(int) # here I kept int as I want the values of dictionary to be integer 
```

String
---

Don't sort a String like this
```python
sorted_string = sorted(string_value) # it will return list of chars
```
Do this
```python
sorted_string = ''.join(sorted(string_value))
```

Check if char is alphabet or numeric or alphanumeric
```python
char.isalnum()
char.isalpha()
char.isnumeric()
```

Convert char to lower or upper
```python
char.upper()
char.lower()
```

Priority Queue
---

```python
import heapq

# Create a priority queue
pq = []

# this is min heap, if you want max heap keep the priorities with negative value

# Add elements to the queue with their priorities one by one
heapq.heappush(pq, (2, "Task 2"))
heapq.heappush(pq, (1, "Task 1"))
heapq.heappush(pq, (3, "Task 3"))

# Else if you have an array directly do a heapify after inserting everything to priority queue
for key, value in freq.items():
    pq.append((-value, key))
heapq.heapify(pq)

# Pop elements from the queue in priority order
while pq:
    priority, task = heapq.heappop(pq)
    print(f"Priority: {priority}, Task: {task}")
```

Techniques
---

### Prefix Sum Array:
The prefix sum array is an auxiliary array where each element at index `i` represents the sum of all elements from the start of the array up to index `i`.
This method is used in problems like product of array except self, sum of array except self
If you have an array `arr = [a0, a1, a2, ..., an-1]`, the prefix sum array `prefix_sum` is defined as:

- `prefix_sum[0] = arr[0]`
- `prefix_sum[i] = arr[0] + arr[1] + ... + arr[i]` for `i > 0`.

This allows us to compute the sum of any subarray (i.e., a range of consecutive elements) efficiently.
