// Gain access to the node.js file system api

const remote = require('electron').remote;
const fs = remote.require('fs');
var PythonShell = require('python-shell');
var cp = require("child_process");
const submitInformation = (ev) => {
    ev.preventDefault()
    let mDirect = {
      musDirectory: document.getElementById('mdirectory').mdir,
      yypDirectory: document.getElementById('ydirectory').mdir,
    }
    document.getElementById("ydirectdisplay").innerHTML = document.getElementById('ydirectory').mdir;
    document.getElementById("mdirectdisplay").innerHTML = document.getElementById('mdirectory').mdir;
    fs.writeFile('config.txt',JSON.stringify(mDirect),(err)=> {
        if(err) throw err;
        console.log("here!!!")
        cp.spawn("python",["test.py"])
    })
  }
 
  document.addEventListener('DOMContentLoaded',()=>{
    document.getElementById('btn').addEventListener('click',submitInformation);
  })