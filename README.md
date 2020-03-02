# Py3-References
## Methods and Usage

File Read Write Methods

```python
# 'w' write, 'r' read, 'r+' read & write, 'a' append,'b' binary
with open('/tmp/test.txt','w') as myfile:
    myfile.write('Test Data')
    myfile.close()
```

```python
# write lines
lines_file = open('/tmp/lines_file.txt','w')
lines_file.writelines('first line')
lines_file.writelines('second line')
lines_file.close()
```

```python
# read lines
lines_file = open('/tmp/lines_file.txt','r')
lines_file.readline() 
lines_file.readline() 
lines_file.readline()
lines_file.close()

# alternatively
lines = open('/tmp/lines_file.txt','r').readlines()
lines
```

```python
# common formula use case
with open('/tmp/fewlines.txt') as myfile:
    for line in myfile:
        print(line.strip())
```

Dictionary Methods

```python
# basic usage
bugs = {'ant':10,'bee':3}
bugs['fly'] = 5 #add to list
bugs.update({'spider':22}) #similar to extend
bugs.get('fly') #retrive value
del bugs['spider']

```

## Examples
###List Comprehension
Remove Empty Strings
```python
test_list = ["", "I", "", "am","","the","", "best", ""] 

test_list1 = [i for i in test_list if i]   

print ("Original list is : " + str(test_list)) 
print ("Modified list is : " + str(test_list1)) 
```