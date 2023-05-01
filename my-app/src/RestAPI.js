import React, { useState } from "react";
import axios from "axios";

function RestAPI() {
    const [text, setText] = useState([]);
    const [title, setTitle] = useState("");

    return (
        <>

            <h1>Todolist</h1>

            <div className="signup">

                <botton
                    onClick={() => {
                        axios.post('http://127.0.0.1:8000/user/signup/', {
                            email: ' ',
                            password: ' '
                        })
                            .then(response => {
                                console.log(response);
                            })
                            .catch(error => {
                                console.error(error);
                            });
                    }}
                >회원가입</botton>
            </div>

            <div className="login">

                <botton
                    onClick={() => {
                        axios.post('http://127.0.0.1:8000/user/api/token/', {
                            email: ' ',
                            password: ' '
                        })
                            .then(response => {
                                console.log(response);
                                // 발급된 인증 토큰을 localStorage에 저장하거나, 애플리케이션 상태에 저장합니다.
                            })
                            .catch(error => {
                                console.error(error);
                            });
                    }}
                >로그인</botton>
            </div>



            <div className="btn-primary">
                <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} />

                <button
                    onClick={() => {
                        axios
                            .post("http://127.0.0.1:8000/todo/", {
                                title: title,
                            }, {
                                headers: {
                                    Authorization: `Token <발급받은 인증 토큰>`,
                                },
                            })
                            .then(function (response) {
                                console.log(response);
                            })
                            .catch(function (error) {
                                console.log(error);
                            });
                    }}
                >
                    할일 등록
                </button>
                <p>
                    <button
                        onClick={() => {
                            axios
                                .get("http://127.0.0.1:8000/todo/")
                                .then((response) => {
                                    setText([...response.data]);
                                    console.log(response.data);
                                })
                                .catch(function (error) {
                                    console.log(error);
                                });
                        }}
                    >
                        리스트 불러오기
                    </button>
                </p>
            </div>
            {text.map((e) => (
                <div>
                    {" "}
                    <div className="list">
                        <span>
                            <p>{e.title}</p> 완료일 : {e.completed_at}
                        </span>

                        <button
                            className="btn-delete"
                            onClick={() => {
                                axios.delete(`http://127.0.0.1:8000/review/${e.id}`);
                                setText(text.filter((text) => text.id !== e.id));
                            }}
                        >
                            삭제
                        </button>{" "}
                    </div>
                </div>
            ))}
        </>
    );
}

export default RestAPI;