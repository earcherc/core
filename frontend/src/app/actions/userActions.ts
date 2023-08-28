'use server';

export async function updateUserDetails(formData: FormData) {
  'use server';

  const data = {
    firstName: formData.get('first-name'),
    lastName: formData.get('last-name'),
    email: formData.get('email'),
    username: formData.get('username'),
  };

  const params = new URLSearchParams();
  params.append('firstName', data.firstName as string);
  params.append('lastName', data.lastName as string);
  params.append('email', data.email as string);
  params.append('username', data.username as string);

  const res = await fetch('http://localhost:8002/user/update', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
      'x-api-key': process.env.API_KEY || '',
    },
    body: params,
  });

  if (!res.ok) {
    // Handle error
    const body = await res.json();
    console.error('Failed to update user:', body);
    return;
  }

  // Handle success
  const body = await res.json();
  console.log('Successfully updated user:', body);
}

export async function changePassword(formData: FormData) {
  'use server';

  const data = {
    currentPassword: formData.get('current_password'),
    newPassword: formData.get('new_password'),
    confirmPassword: formData.get('confirm_password'),
  };

  console.log('Changing password:', data);
}

export async function deleteAccount() {
  'use server';

  console.log('Deleting account');
}
