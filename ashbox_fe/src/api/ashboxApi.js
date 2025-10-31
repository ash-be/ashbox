const API_BASE_URL = 'http://localhost:8000/api';

export async function fetchUsers(method = "GET") {
    const response = await fetch(`${API_BASE_URL}/v1/users/`, {
        method,
        headers: { "Content-Type": "application/json" },
    });
    
    if (!response.ok) throw new Error("서버 통신 오류");
    return response.json();
}