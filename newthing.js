function getfolder(e) {
    var files = e.target.files;
    var path = files[0].webkitRelativePath;
    var Folder = path.split("/");
    console.log(document.getElementById('mdirectory'))
    return Folder[0];
}