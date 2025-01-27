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
