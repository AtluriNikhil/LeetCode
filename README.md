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

Techniques
---

### Prefix Sum Array:
The prefix sum array is an auxiliary array where each element at index `i` represents the sum of all elements from the start of the array up to index `i`.
This method is used in problems like product of array except self, sum of array except self
If you have an array `arr = [a0, a1, a2, ..., an-1]`, the prefix sum array `prefix_sum` is defined as:

- `prefix_sum[0] = arr[0]`
- `prefix_sum[i] = arr[0] + arr[1] + ... + arr[i]` for `i > 0`.

This allows us to compute the sum of any subarray (i.e., a range of consecutive elements) efficiently.
