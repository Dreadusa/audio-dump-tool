directories = document.getElementsByClassName('folderGetter')
for (let iv of directories){
    iv.onchange = function getFolder(e) {
        var files = e.target.files;
        var path = files[0].path;
        var Folder = path.split("\\");
        var newPath = "";
        for (var i = 0; i < Folder.length-1; i++) {
            if (i >= 1) {
                newPath += "\\" + Folder[i];
            } else {
                newPath += Folder[i];
            }
        }
        console.log(iv.id)
        if (iv.id == "ydirectory") {
            console.log("here")
        document.getElementById("ydirectdisplay").innerHTML = newPath
        }
        if (iv.id == "mdirectory") {
            document.getElementById("mdirectdisplay").innerHTML = newPath
        }     
        iv.mdir = newPath
    }
}