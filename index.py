from flask import Flask,request,render_template
app=Flask(__name__)
k=0
def checked(m,f):
    k=0
    m=m
    f=f
    a=[char for char in m] 
    b=[char for char in f]
    for i in range(0,len(a)):
        for j in range(0,len(b)):
            if(a[i]==b[j]):
                a[i]=0
                b[j]=0
    for i in a:
        if(i!=0):
            k=k+1
    for i in b:
        if(i!=0):
            k=k+1
    s=['friend','love','attraction','marriage','enemy','siblings']
    for i in range(5,0,-1):
       n=k 
       g=n%i
       if g>=0:
        right=s[g+1:]
        left=s[:g]
        s=right+left
       else:
        s=s[:len(s)-1]
    return s[0]
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/check',methods=['post'])
def check():
    l=request.form['name1']
    i=request.form['name2']
    r=checked(l,i)
    return r

if __name__=="__main__":
    app.run(debug=True)
