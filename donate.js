// JavaScript for form validation
document.addEventListener('DOMContentLoaded', function () {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation');

    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
        .forEach(function (form) {
            form.addEventListener('submit', function (event) {
                if (!form.checkValidity()) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
});

// JavaScript for smooth scrolling
document.addEventListener("DOMContentLoaded", function () {
    var scrollLinks = document.querySelectorAll('a[href^="#"]');
    for (var i = 0; i < scrollLinks.length; i++) {
        scrollLinks[i].addEventListener('click', smoothScroll);
    }
});

function smoothScroll(e) {
    e.preventDefault();
    var targetId = this.getAttribute("href");
    document.querySelector(targetId).scrollIntoView({
        behavior: 'smooth',
        block: 'start'
    });
}

// Additional JavaScript functionality can be added as needed
