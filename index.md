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
  padding: 40px;
  text-align: center;
  background: #FFFFFF;
  font-size: 30px;
  color: black;
  height: 220px;
  <!--background-image: url('headerBackground.jpg');
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
  <!-- height: 300px; /* Should be removed. Only for demonstration */ -->
}

/*collaspible*/
.collapsible {
  background-color: #E6E6E6;
  color: black;
  cursor: pointer;
  padding: 30px;
  width: 100%;
  border: none;
  text-align: center;
  outline: none;
  font-size: 20px;
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
  background-color: #F7F7F7;
}
/*each skill box*/
.box {
  border-radius: 10px;
  width: 130px;
  color: black;
  background: #D4D4D4;
  border: 1px solid #969696;
  text-align: center;
}

/*Projects*/
.projects{
  padding: 0 100px;
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.2s ease-out;
  background-color: #F7F7F7;
}
</style>
</head>
<body>



<div class="header">
  <h1>Emily S Pfau</h1>
  <div class="about">
    <div class="column">
      <p>
        <a style="font-size:30px;" href="https://github.com/epfau22">
          <img style="width:35px;height:35px;" src="git.jpg">
        </a>
      </p>
    </div>
    <div class="column">
      <p>
        <a style="font-size:30px;" href="https://www.linkedin.com/in/emily-pfau-411669186/"> 
          <img style="width:35px;height:35px;" src="linked.jpg">
        </a>
      </p>
    </div>
  </div>
</div>
<!-- short summary about me and what I am interested in -->
<div class="about">
  <div class="column" style="background-color:#FFFFF;">
    <h2>About Me</h2>
    <p>Highly motivated, passionate computer scientist with a foundation in math, algorithmic logic, dynamic programming and leadership. Seeking to work in Cyber Security and/or Web Development.</p>
  </div>
  <div class="column" style="background-color:#FFFFF;">
    <img src="picResume.jpg">
  </div>
</div>


<!-- once clicked my my skills (computer lanagues and other things) I have done will be shown -->
<button class="collapsible" style="font-size: 30px;">Skills</button>
<div class="skills">
  <h2>Computer Languages</h2>
  <div class="about">
    <div class="column"><p class="box">Python</p></div>
    <div class="column"><p class="box">HTML</p></div>
    <div class="column"><p class="box">CSS</p></div>
    <div class="column"><p class="box">HTML5</p></div>
  </div>
  <div class="about">
    <div class="column"><p class="box">C</p></div>
    <div class="column"><p class="box">C++</p></div>
    <div class="column"><p class="box">C#</p></div>
    <div class="column"><p class="box">Java</p></div>
  </div>
  <div class="about">
    <div class="column"><p class="box">Swift</p></div>
    <div class="column"><p class="box">JavaScript</p></div>
    <div class="column"><p class="box">Assembly Language</p></div>
    <div class="column"><p class="box">Haskell</p></div>
  </div>                  
  <h2>Other Skills</h2>
  <div class="about">
    <div class="column"><p class="box">Pytorch</p></div>
    <div class="column"><p class="box">Wireshark</p></div>
    <div class="column"><p class="box">WebGL</p></div>
    <div class="column"><p class="box">HTC Vive</p></div>
    <div class="column"><p class="box">LaTeX</p></div>
  </div>
  <div class="about">
    <div class="column"><p class="box">Adobe Photoshop</p></div>
    <div class="column"><p class="box">Adobe Illustrator</p></div>
    <div class="column"><p class="box">WACOM Tablets</p></div>
    <div class="column"><p class="box">WordPress</p></div>
    <div class="column"><p class="box">Blender</p></div>
  </div>
  <div class="about">
    <div class="column"><p class="box">creation of AI</p></div>
    <div class="column"><p class="box">Highly skilled in Unity</p></div>
    <div class="column"><p class="box">Face to Face customer service</p></div>
    <div class="column"><p class="box">machine learning and Deep learning</p></div>
    <div class="column"><p class="box">Interacting in multicultural environment</p></div>
  </div> 
  <div class="about">
    <div class="column"><p class="box">Github</p></div>
    <div class="column"><p class="box">Gatekeeper</p></div>
  </div> 
</div>

<!-- once clicked links to other pages that show my programs I have made will be shown -->
<button class="collapsible" style="font-size: 30px;">Projects</button>
<div class="projects">
  <div class="about">
    <div class="column;" style="font-size: 30px;"><a href="error">Project 1</a></div>
    <div class="column">
    
      <p style="text-align: right;">This is my first project explanation </p>
    </div>
  </div>
  <div class="about">
    <div class="column;" style="font-size: 30px;"><a href="error">Project 2</a></div>
    <div class="column">
      <p style="text-align: right;">This is my second project explanation</p>
    </div>
  </div>
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



