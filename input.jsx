<script>
const submitInformation = (ev) => {
  ev.preventDefault()
  let mDirect = {
    thisDirectory: document.getElementById('mdirectory').value,
    yypDirectory: document.getElementById('ydirectory').value
  }
}
localStorage.setItem("Directories",[thisDirectory,yypDirectory])
document.getEventListener('DOMContentLoaded',()=>{
  document.getElementById('btn').addEventListener('click',submitInformation);
})
</script>