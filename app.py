from flask import Flask,render_template,request,url_for,redirect
app=Flask(__name__)

Student_list = [{"Name": "Mahalakshmi", "Age": 24, "Roll_NO": 101, "Marks": [90, 75, 80, 98, 75]},
                {"Name": "Nijanthan", "Age": 23, "Roll_NO": 102, "Marks": [90, 75, 80, 98, 65]},
                {"Name": "Selva", "Age": 22, "Roll_NO": 103, "Marks": [90, 75, 80, 78, 99]},
                {"Name": "Preethi", "Age": 22, "Roll_NO": 104, "Marks": [94, 75, 80, 88, 35]},
                {"Name": "Ajay", "Age": 23, "Roll_NO": 105, "Marks": [70, 85, 80, 98, 35]},
                {"Name": "Anand", "Age": 26, "Roll_NO": 106, "Marks": [90, 75, 85, 98, 35]},
                {"Name": "Pavitran", "Age": 21, "Roll_NO": 107, "Marks": [80, 98, 35, 90, 75]},
                {"Name": "Kumar", "Age": 25, "Roll_NO": 108, "Marks": [90, 80, 98, 35, 75]},
                {"Name": "Saranya", "Age": 26, "Roll_NO": 109, "Marks": [75, 80, 90, 98, 35]},
                {"Name": "Jeffin", "Age": 22, "Roll_NO": 110, "Marks": [98, 35, 90, 75, 80]}]

@app.route("/",methods=["POST","GET"])

def func1():
    if request.method=="POST":
        name=request.form.get("name")
        age=request.form.get("age")
        rollNo=request.form.get("rollNo")
        mark1=request.form.get("mark1")
        mark2=request.form.get("mark2")
        mark3=request.form.get("mark3")
        mark4=request.form.get("mark4")
        mark5=request.form.get("mark5")
        studentDict={}
        marks=[]
        marks.append(mark1)
        marks.append(mark2)
        marks.append(mark3)
        marks.append(mark4)
        marks.append(mark5)
        studentDict.update({"Name":name})
        studentDict.update({"Age":age})
        studentDict.update({"Roll_NO":rollNo})
        studentDict.update({"Marks":marks})
        Student_list.append(studentDict)
    return render_template("index.html",studentList=Student_list) 

@app.route("/<string:item>")

def deleteItem(item):
   Student_list.pop(int(item)-1)
   return redirect(url_for('func1')) 

@app.route("/edit<string:item>",methods=["POST","GET"])

def editItem(item):
  
   student=Student_list[int(item)-1]

   if request.method=="POST":
      name=request.form.get("name")
      age=request.form.get("age")
      rollNo=request.form.get("rollNo")
      mark1=request.form.get("mark1")
      mark2=request.form.get("mark2")
      mark3=request.form.get("mark3")
      mark4=request.form.get("mark4")
      mark5=request.form.get("mark5")
      student["Name"]=name
      student["Age"]=age
      student["Roll_NO"]=rollNo
      student["Marks"][0]=mark1
      student["Marks"][1]=mark2
      student["Marks"][2]=mark3
      student["Marks"][3]=mark4
      student["Marks"][4]=mark5
      # Student_list[int(item)-1]["Name"]=name
      # Student_list[int(item)-1]["Age"]=age
      # Student_list[int(item)-1]["Roll_NO"]=rollNo
      # Student_list[int(item)-1]["Marks"][0]=mark1
      # Student_list[int(item)-1]["Marks"][1]=mark2
      # Student_list[int(item)-1]["Marks"][2]=mark3
      # Student_list[int(item)-1]["Marks"][3]=mark4
      # Student_list[int(item)-1]["Marks"][4]=mark5
      return redirect(url_for('func1')) 
   return render_template("edit.html",s=student)   



if "__main__"==__name__:
 app.run(debug=True) 



