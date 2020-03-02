# Py3-References

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
