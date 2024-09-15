
function submitFunc(){
    var userInput = document.getElementById("username").value;

    if (userInput == 'student'){
        window.location.href="student_home.html"
    } else if (userInput == 'teacher'){
        window.location.href="teacher_home.html"
    } else {
        alert("No Account with that Username")
    }
}

function closeAssignment(){
    document.getElementById("createAssignmentsPopUp").style.visibility = "hidden";
}

function closeRewards(){
    document.getElementById("rewardsPopUp").style.visibility = "hidden";
}

function createAssignment(){
    document.getElementById("createAssignmentsPopUp").style.visibility = "visible";
}

function rewardBtn(){
    document.getElementById("rewardsPopUp").style.visibility = "visible";
}

var XP = 0;

function finishAssignment(clicked){
    XP += 5;
    document.getElementById(clicked).style.backgroundColor = "#36ba81";
    document.getElementById(clicked).style.textDecoration = "line-through";

    document.getElementById('xpBar').style.width = document.getElementById('xpBar').offsetWidth + 5 + "px";

    document.getElementById("XP").innerHTML = "XP: " + XP + "/100";

    setTimeout(removeAssignments, 2000, clicked);
}

function removeAssignments(theID){
    document.getElementById(theID).remove();
}

function openClass(){
    window.location.href="teacher_class.html"
}

function selectStudent(clicked){
    document.getElementById(clicked).style.border = "solid #83c9ad 5px"
}

function rewardStudent(){
    document.getElementById("rewardsPopUp").style.visibility = "hidden";
    
    alert("John Doe has been rewarded a pokeball!")
}