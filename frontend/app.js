// app.js

const apiUrl = 'http://localhost:5000/users';
const userTableBody = document.querySelector('#user-table tbody');
const userForm = document.getElementById('user-form');
const formTitle = document.getElementById('form-title');
const resetFormButton = document.getElementById('reset-form');
let editingUserId = null;  // To track if we're editing a user

// Fetch and display users
function fetchUsers() {
  fetch(apiUrl)
    .then(response => response.json())
    .then(users => {
      userTableBody.innerHTML = '';
      users.forEach(user => {
        const row = document.createElement('tr');
        row.innerHTML = `
          <td>${user.id}</td>
          <td>${user.name}</td>
          <td>${user.email}</td>
          <td>${user.role}</td>
          <td>
            <button onclick="editUser(${user.id})">Edit</button>
            <button onclick="deleteUser(${user.id})">Delete</button>
          </td>
        `;
        userTableBody.appendChild(row);
      });
    })
    .catch(error => console.error('Error fetching users:', error));
}

// Add a new user
function addUser(user) {
  fetch(apiUrl, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(user)
  })
    .then(() => fetchUsers())
    .catch(error => console.error('Error adding user:', error));
}

// Edit an existing user
function updateUser(user) {
  fetch(`${apiUrl}/${user.id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(user)
  })
    .then(() => fetchUsers())
    .catch(error => console.error('Error updating user:', error));
}

// Delete a user
function deleteUser(id) {
  if (confirm('Are you sure you want to delete this user?')) {
    fetch(`${apiUrl}/${id}`, { method: 'DELETE' })
      .then(() => fetchUsers())
      .catch(error => console.error('Error deleting user:', error));
  }
}

// Populate form for editing
function editUser(id) {
  fetch(`${apiUrl}/${id}`)
    .then(response => response.json())
    .then(user => {
      document.getElementById('name').value = user.name;
      document.getElementById('email').value = user.email;
      document.getElementById('role').value = user.role;
      editingUserId = user.id;
      formTitle.textContent = 'Edit User';
    })
    .catch(error => console.error('Error fetching user:', error));
}

// Handle form submission
userForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const user = {
    name: document.getElementById('name').value,
    email: document.getElementById('email').value,
    role: document.getElementById('role').value
  };

  if (editingUserId) {
    user.id = editingUserId;
    updateUser(user);
  } else {
    addUser(user);
  }

  userForm.reset();
  editingUserId = null;
  formTitle.textContent = 'Add User';
});

// Reset form when reset button is clicked
resetFormButton.addEventListener('click', () => {
  userForm.reset();
  editingUserId = null;
  formTitle.textContent = 'Add User';
});

// Fetch and display users on page load
fetchUsers();