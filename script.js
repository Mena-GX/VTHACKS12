var user;

function submitFunc(){
    if (user == 'student'){
        window.location.href="student_home.html"
    } else {
        window.location.href="teacher_home.html"
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