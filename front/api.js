window.onload = () =>{
    console.log("로딩")
}

// 회원가입
async function handleSignin(){

    const email = document.getElementById("email").value
    const password = document.getElementById("password").value
    const name = document.getElementById("name").value
    const gender = document.getElementById("gender").value
    const age = document.getElementById("age").value
    const introduction = document.getElementById("introduction").value


    console.log(email,password)

    const response = await fetch('http://127.0.0.1:8000/users/signup/',{
        headers:{
            'content-type' : 'application/json',

        },
        method:'POST',
        body: JSON.stringify({
            "email" : email,
            "password":password,
            "name" : name,
            "gender" : gender,
            "age" : age,
            "introduction":introduction
        })
    });

    console.log(response)
}

// 로그인
async function handleLogin(){
    const email = document.getElementById("email").value
    const password = document.getElementById("password").value

    console.log(email,password)

    const response = await fetch('http://127.0.0.1:8000/users/api/token/',{
        headers:{
            'content-type' : 'application/json',

        },
        method:'POST',
        body: JSON.stringify({

            "email" : email,
            "password":password
            
        })
    });

    const respons_json = await response.json()

    console.log(respons_json)

    localStorage.setItem("access", respons_json.access);
    localStorage.setItem("refresh", respons_json.refresh);

    // payload 저장하기
    const base64Url = respons_json.access.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c){
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    localStorage.setItem("payload", jsonPayload);

}

// // 로그인 인증 api (식별)
// async function handleMock(){
    
//     const response = await fetch('http://127.0.0.1:8000/users/mock/',{
//         headers:{
//             "authorization" : "Bearer "+ localStorage.getItem("access") // access token 헤더에
//         },
//         method:'GET',
//     });

//     console.log(response)
// }

// 로그아웃
async function handlelogout(){
    localStorage.removeItem("access")
    localStorage.removeItem("refresh")
    localStorage.removeItem("payload")
}