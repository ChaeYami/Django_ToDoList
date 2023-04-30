
async function handleUserUpdate() {
    const user_id = getUserId(); // Replace this with the function to get the user ID of the current user
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const name = document.getElementById("name").value;
    const gender = document.getElementById("gender").value;
    const age = document.getElementById("age").value;
    const introduction = document.getElementById("introduction").value;
  
    const response = await fetch(`http://127.0.0.1:8000/users/${user_id}/`, {
      headers: {
        'content-type': 'application/json',
      },
      method: 'PATCH',
      body: JSON.stringify({
        email: email,
        password: password,
        name: name,
        gender: gender,
        age: age,
        introduction: introduction,
      }),
    });
  
    if (response.status === 200) {
      alert("수정이 완료되었습니다.");
      window.location.reload();
    } else {
      alert("수정에 실패했습니다. 다시 시도해주세요.");
    }
  }
  