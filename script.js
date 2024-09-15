
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

