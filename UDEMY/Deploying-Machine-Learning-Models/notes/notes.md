# Train  a model and transform to a service

### Flask Basics:



Get vs POST -- > Get passes the parameter through URL

```python
#hostname/addParam?a=20&b=90
from flask import Flask,request

@app.route('/addParamGet',methods=['GET'])
def add_param():
    a = request.args.get('a')
	b = request.args.get('b')
    
    return str(int(a)+int(b))

@app.route('/addParamPost',methods=['POST'])
def add_param():
    a = request.form['a']
	b =  request.form['b']
    
    return str(int(a)+int(b))


```

```html
<form action="localhost/addParamPost" method="POST">
    <div>
        <label>A</label>
        <input type="text" id="a" name="a" placeholder="EnterA">
    </div>
    <div>
        <label>B</label>
        <input type="text" id="b" name="b" placeholder="EnterB">
    </div>
</form>
```

### Machine Learning:

---

```python
# balanced data

value_count()
astype()

# Feature Engineering
isnull().sum()

# Normalization
```

outliers
**correlation**

Grid Search best parameters

Best parameters confusion matrix

Pickle as model

You need to normalize the input

----

## Docker

projects

## Streamlit


