# Flatten-JSON
The flattenJSON.py script flattens the JSON object in a way that is shown below:

Input:
```
{
    "a": 1,
    "b": true,
    "c": {
        "d": 3,
        "e": "test"
    }
}
```
Output:
```
{
    "a": 1,
    "b": true,
    "c.d": 3,
    "c.e": "test"
}
```
# Requirements
 - Python 3
 
 Tested on :
  - Windows 10, Python 3.8.0
  - (VM) Ubuntu 20.04, Python 3.8.5

# How to run it
You can run the script from directory of your choosing by providing the path to the script.
### Windows:
Run this to flatten test.json and print the output to command line:
``` 
type test.json | py flattenJSON.py
```

Run this to to flatten test.json and write the output to flattened.json:
```
type test.json | py flattenJSON.py > flattened.json
```

### Linux:
Run this to flatten test.json and print the output to command line:
```
cat  test.json | python3 flattenJSON.py
```
Run this to flatten test.json and write the output to flattened.json:
```
cat test.json | python3 flattenJSON.py > flattened.json
```
# Tests
You can find test data and scripts in ```test``` directory. Test script runs flattten method on 5 samples of JSON files and compares the results with already flattened versions of the files. This includes edge case of empty ``` {} ``` JSON object. The flattened versions of sample files were generated by using [@mongodb-js/flat](https://www.npmjs.com/package/@mongodb-js/flat). Test script also checks the handling of invalid input and  pipes by runnig the scripts in ```test/scripts``` directory. You can run the test script from directory of your choosing by providing the path to the test script:

**Windows:**
```
py testFlattenJSON.py
```
**Linux:**
You need to at first set executable permission of bash script in ```test/scripts```.
```
chmod +x test/scripts/test_cli.sh
```
Now you can run.
```
python3 testFlattenJSON.py
```
