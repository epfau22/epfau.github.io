<!-- <!DOCTYPE html> -->
<html lang="en">
<head>
<title>Page Title</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
/* Style the body */
body {
  font-family: Arial;
  margin: 0;
}

/* Header/Logo Title */
.header {
  padding: 60px;
  text-align: center;
  background: #FFFFFF;
  font-size: 30px;
  color: black;
  <!--background-image: url('headerBackground.jpg');
  height: 362px;
  width: 850px; 
  background-repeat: no-repeat;
  background-size: 850px 362px; -->
}

/* about Me */
.about {
  display: flex;
}
.column {
  flex: 50%;
  padding: 10px;
  height: 300px; /* Should be removed. Only for demonstration */
}

/*collaspible*/
.collapsible {
  background-color: #777;
  color: white;
  cursor: pointer;
  padding: 18px;
  width: 100%;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;
}

.active, .collapsible:hover {
  background-color: #555;
}

/*Skills*/
.skills{
  padding: 0 18px;
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.2s ease-out;
  background-color: #f1f1f1;
}

/*Projects*/
.projects{
  padding: 0 18px;
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.2s ease-out;
  background-color: #f1f1f1;
}
</style>
</head>
<body>



<div class="header" style= "width: 100%;">
  <h1>Emily S Pfau</h1>
  <a href="https://github.com/epfau22">github</a>
  <a href="https://github.com/epfau22">LinkedIn</a>
</div>

<!-- short summary about me and what I am interested in -->
<div class="about">
  <div class="column" style="background-color:#FFFFF;">
    <h2>About Me</h2>
    <p>Highly motivated, passionate computer scientist with a foundation in math, algorithmic logic, dynamic programming and leadership. Seeking to work in Cyber Security and/or Web Development.</p>
  </div>
  <div class="column" style="background-color:#FFFFF;">
    <p>picture here</p>
  </div>
</div>


<!-- once clicked my my skills (computer lanagues and other things) I have done will be shown -->
<button class="collapsible">Skills</button>
<div class="skills">
  <p>I will be puting my skills here </p>
</div>

<!-- once clicked links to other pages that show my programs I have made will be shown -->
<button class="collapsible">Projects</button>
<div class="projects">
  <p>I will be puting my projects here </p>
</div>

<!-- other image -->
<!-- <img src="headerBackground.jpg" alt="mind" class="center"> -->

<!-- end -->
<div><a href="https://github.com/epfau22">Visit my github site</a></div>


<script>
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.maxHeight){
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    } 
  });
}
</script>
</body>
</html>


