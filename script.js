var user;

function submitFunc(){
    if (user == 'student'){
        window.location.href="student_home.html"
    } else {
        window.location.href="teacher_home.html"
    }
}