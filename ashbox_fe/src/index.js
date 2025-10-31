import { fetchUsers } from "./api/ashboxApi.js";

const app = document.getElementById("app");

app.innerHTML = `
    <h2>서버 통신 테스트</h2>
    <button id="getBtn">GET 요청</button>
    <button id="postBtn">POST 요청</button>
    <p id="result">결과: </p>
`;

document.getElementById("getBtn").addEventListener("click", async () => {
    try {
        const data = await fetchUsers("GET");
        document.getElementById("result").innerText = `결과: ${data.message}`;
    } catch (err) {
        document.getElementById("result").innerText = `오류: ${err.message}`;
    }
});

document.getElementById("postBtn")?.addEventListener("click", async () => {
    try {
        const data = await fetchUsers("POST");
        document.getElementById("result").innerText = `결과: ${data.message}`;
    } catch (err) {
        document.getElementById("result").innerText = `오류: ${err.message}`;
    }
});