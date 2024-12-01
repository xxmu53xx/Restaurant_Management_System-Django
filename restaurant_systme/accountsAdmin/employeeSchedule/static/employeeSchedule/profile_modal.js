document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('profileModal-1');
    const userProfileLink = document.querySelector('.dropdown a[href=""]');
    const closeBtn = document.querySelector('.modal-close-1');
    const cancelBtn = document.getElementById('cancelBtn-1');
    const saveBtn = document.getElementById('saveBtn-1');
    const form = document.getElementById('profileEditForm-1');

    // Function to open modal
    function openModal() {
        modal.style.display = 'flex';
        resetForm();
        fetchUserRole();
    }

    // Function to close modal
    function closeModal() {
        modal.style.display = 'none';
    }

    // Function to reset form to original state
    function resetForm() {
        const inputs = document.querySelectorAll('#profileEditForm-1 input');
        inputs.forEach(input => {
            input.value = input.getAttribute('data-original');
            input.disabled = true;

            const toggle = input.nextElementSibling;
            if (toggle && toggle.classList.contains('edit-toggle-1')) {
                const icon = toggle.querySelector('i');
                icon.classList.remove('fa-check');
                icon.classList.add('fa-edit');
            }
        });
    }

    // Fetch user role and update it in the modal
    function fetchUserRole() {
        const roleField = document.getElementById('currentRole-1');

        roleField.value = "Loading...";

        $.ajax({
            url: "{% url 'get_user_role' %}",
            method: 'GET',
            success: function (data) {
                if (data.success) {
                    roleField.value = data.role;
                    roleField.disabled = true;
                } else {
                    console.error('Error fetching role:', data.message);
                    roleField.value = "Error loading role";
                }
            },
            error: function (error) {
                console.error('Error:', error);
                roleField.value = "Error loading role";
            }
        });
    }

    // Open modal when User Profile is clicked
    userProfileLink.addEventListener('click', (e) => {
        e.preventDefault();
        openModal();
    });

    // Close modal when close button is clicked
    closeBtn.addEventListener('click', closeModal);

    // Close modal when cancel button is clicked
    cancelBtn.addEventListener('click', () => {
        resetForm();
        closeModal();
    });

    // Close modal if clicked outside of the modal content
    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            resetForm();
            closeModal();
        }
    });

    // Add original values as data attributes for reset
    form.querySelectorAll('input').forEach(input => {
        input.setAttribute('data-original', input.value);
    });

    // Edit toggle handler
    const editToggles = document.querySelectorAll('.edit-toggle-1');
    editToggles.forEach(toggle => {
        toggle.addEventListener('click', function () {
            const field = this.dataset.field;
            const input = document.getElementById(field);
            input.disabled = !input.disabled;

            const icon = this.querySelector('i');
            if (input.disabled) {
                icon.classList.remove('fa-check');
                icon.classList.add('fa-edit');
                input.value = input.getAttribute('data-original');
            } else {
                icon.classList.remove('fa-edit');
                icon.classList.add('fa-check');
            }
        });
    });

    // Save changes via AJAX
    saveBtn.addEventListener('click', (e) => {
        e.preventDefault();

        const formData = new FormData();
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        formData.append('csrfmiddlewaretoken', csrfToken);

        let hasChanges = false;
        const fieldsToCheck = [
            { id: 'username-1', name: 'username' },
            { id: 'firstName-1', name: 'first_name' },
            { id: 'lastName-1', name: 'last_name' },
            { id: 'email-1', name: 'email' }
        ];

        fieldsToCheck.forEach(field => {
            const input = document.getElementById(field.id);
            const originalValue = input.getAttribute('data-original');

            if (input.value !== originalValue) {
                formData.append(field.name, input.value);
                hasChanges = true;
            }
        });

        if (!hasChanges) {
            alert('No changes to save');
            return;
        }

        fetch("{% url 'update_profile' %}", {
            method: 'POST',
            body: formData,
            headers: { 'X-CSRFToken': csrfToken }
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Profile updated successfully!');

                    window.location.reload();
                    // Update username and role in the frontend
                    document.querySelector('.profile-info-1 h2').textContent = data.username;
                    document.getElementById('currentRole-1').value = data.role;

                    // Close the modal
                    closeModal();
                } else {
                    alert('Update failed: ' + data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred during update');
            });
    });
});