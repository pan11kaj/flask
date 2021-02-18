from flask import Flask,jsonify,request;

app = Flask(__name__)

contacts = [
    {
        'contact':"9522223643",
        'name':"pankaj Sahu",
        "done":False,
        "id":1
    },{
        'contact':"6264066172",
        'name':"Gandhi",
        "done":False,
        "id":2
    }

]
@app.route('/add-data',methods = ["POST"])
def adding():
    if not request.json:
        return jsonify({
            "message":"please provide a data",
            "status":"error!"
        },400)
    contact = {
        'contact':request.json['title'],
        'name':request.json.get("name",""),
        'id': id[-1]['id']+1,
        'done':False
    }
    contacts.append(contact)
    return jsonify({
        "message":"contact added successfully!",
        "status":"success"
    })

if __name__ == "__main__":
    app.run()