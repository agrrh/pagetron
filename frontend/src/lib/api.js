export const apiUrl = import.meta.env.DEV ? "http://localhost:3000" : (import.meta.env.VITE_API_URL || "/api");
