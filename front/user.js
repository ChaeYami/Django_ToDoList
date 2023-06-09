
async function handleUserUpdate() {
    const user_id = getUserId();
    const password = document.getElementById("password").value;
    const name = document.getElementById("name").value;
    const gender = document.getElementById("gender").value;
    const age = document.getElementById("age").value;
    const introduction = document.getElementById("introduction").value;
  
    const response = await fetch(`http://127.0.0.1:8000/users/${user_id}/`, {
      headers: {
        'content-type' : 'application/json',
        "authorization" : "Bearer "+ localStorage.getItem("access") // access token 헤더에
      },
      method: 'PATCH',
      body: JSON.stringify({
        "password":password,
        "name" : name,
        "gender" : gender,
        "age" : age,
        "introduction":introduction
      }),
    });
  
    if (response.status === 200) {
      alert("수정이 완료되었습니다.");
      window.location.reload();
    } else {
      alert("입력값을 확인하세요.");
    };
  };
  

function getUserId() {
    const payloadStr = localStorage.getItem("payload");
    if (!payloadStr) {
        return null;
    }
    const payload = JSON.parse(payloadStr);
    return payload.user_id;
}
