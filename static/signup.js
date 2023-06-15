const form = document.querySelector('.signup-form');

form.addEventListener('submit', (event) => {
	event.preventDefault();
	const name = document.querySelector('#name').value;
	const emailPhone = document.querySelector('#email-phone').value;
	const password = document.querySelector('#password').value;

	// Here you can add the code to submit the form data to a server or store it in local storage
});